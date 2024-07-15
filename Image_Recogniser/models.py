import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras import layers
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import cv2

class FashionProductRecommender:
    def __init__(self, styles_path, images_path):
        self.styles_path = styles_path
        self.images_path = images_path
        self.styles = self.load_styles()
        self.label_encoders = self.initialize_label_encoders()

    def load_styles(self):
        styles = pd.read_csv(self.styles_path, on_bad_lines='skip')
        styles = styles.drop(["productDisplayName", "year"], axis=1)
        styles = styles[(styles.masterCategory == 'Apparel') | (styles.masterCategory == 'Footwear')]
        styles = styles.drop(styles[styles["subCategory"] == "Innerwear"].index)
        styles = styles.dropna()
        styles = self.df_drop(styles, "subCategory", ["Apparel Set", "Dress", "Loungewear and Nightwear", "Saree", "Socks"])
        styles["subCategory"] = styles["subCategory"].apply(lambda x: "Footwear" if x in ["Shoes", "Flip Flops", "Sandal"] else x)
        ids_to_drop = [39403, 39410, 39401, 39425, 12347]
        styles = styles[~styles.id.isin(ids_to_drop)]
        self.group_color(styles)
        return styles

    def group_color(self, styles):
        styles["colorgroup"] = -1
        styles.loc[styles.baseColour.isin(['Red', 'Brown', 'Coffee Brown', 'Maroon', 'Rust', 'Burgundy', 'Mushroom Brown']), "colorgroup"] = 0
        styles.loc[styles.baseColour == 'Copper', "colorgroup"] = 1
        styles.loc[styles.baseColour.isin(['Orange', 'Bronze', 'Skin', 'Nude']), "colorgroup"] = 2
        styles.loc[styles.baseColour.isin(['Gold', 'Khaki', 'Beige', 'Mustard', 'Tan', 'Metallic']), "colorgroup"] = 3
        styles.loc[styles.baseColour == 'Yellow', "colorgroup"] = 4
        styles.loc[styles.baseColour == 'Lime Green', "colorgroup"] = 5
        styles.loc[styles.baseColour.isin(['Green', 'Sea Green', 'Fluorescent Green', 'Olive']), "colorgroup"] = 6
        styles.loc[styles.baseColour.isin(['Teal', 'Turquoise Blue']), "colorgroup"] = 7
        styles.loc[styles.baseColour == 'Blue', "colorgroup"] = 8
        styles.loc[styles.baseColour == 'Navy Blue', "colorgroup"] = 9
        styles.loc[styles.baseColour.isin(['Purple', 'Lavender']), "colorgroup"] = 10
        styles.loc[styles.baseColour.isin(['Pink', 'Magenta', 'Peach', 'Rose', 'Mauve']), "colorgroup"] = 11
        styles.loc[styles.baseColour.isin(['Black', 'Charcoal']), "colorgroup"] = 12
        styles.loc[styles.baseColour.isin(['White', 'Off White', 'Cream']), "colorgroup"] = 13
        styles.loc[styles.baseColour.isin(['Grey', 'Silver', 'Taupe', 'Grey Melange']), "colorgroup"] = 14
        styles.loc[styles.baseColour == 'Multi', "colorgroup"] = 15

    def df_drop(self, styles, col, items):
        for item in items:
            styles = styles.drop(styles[styles[col] == item].index)
        return styles

    def initialize_label_encoders(self):
        return {
            "articleType": LabelEncoder(),
            "gender": LabelEncoder(),
            "baseColour": LabelEncoder(),
            "season": LabelEncoder(),
            "usage": LabelEncoder()
        }

    def encode_labels(self, styles):
        for col, le in self.label_encoders.items():
            styles[col] = le.fit_transform(styles[col])
        return styles

    def get_filtered_df(self, subCategory):
        styles = self.load_styles()
        styles = styles[styles.subCategory == subCategory]
        self.group_color(styles)
        styles.baseColour = styles.colorgroup
        styles = self.encode_labels(styles)
        return styles

    def make_input_array(self, df):
        train_images = np.zeros((len(df.id), 80, 60, 3))
        for i in range(len(df.id)):
            ID = df.id.iloc[i]
            path = f"{self.images_path}/{ID}.jpg"
            img = cv2.imread(path)
            if img.shape != (80, 60, 3):
                img = image.load_img(path, target_size=(80, 60, 3))
            train_images[i] = img
        data = tf.data.Dataset.from_tensor_slices(
            (
                {"images": train_images},
                {col: df[[col]] for col in self.label_encoders.keys()}
            )
        )
        return data

    def make_branch(self, res_input, n_out, act_type, name):
        z = layers.Dense(512, activation="relu")(res_input)
        z = layers.Dense(256, activation='relu')(z)
        z = layers.Dense(128, activation='relu')(z)
        z = layers.Dense(64, activation='relu')(z)
        z = layers.Dense(n_out)(z)
        z = layers.Activation(act_type, name=name)(z)
        return z

    def build_model(self, width, height):
        res50 = keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(80, 60, 3))
        res50.trainable = False
        inputs = keras.Input(shape=(width, height, 3), name="images")
        x = res50(inputs, training=False)
        x = layers.Flatten()(x)
        x = layers.Dense(1024, activation='relu')(x)
        branches = [self.make_branch(x, len(le.classes_), 'softmax', name) for name, le in self.label_encoders.items()]
        model = keras.Model(inputs=inputs, outputs=branches)
        return model

    def prepare_data(self, x):
        x_input = x.shuffle(buffer_size=len(x))
        x_train_size = int(0.6 * len(x_input))
        x_val_size = int(0.2 * len(x_input))
        x_train = x_input.take(x_train_size).batch(2)
        x_val = x_input.skip(x_train_size).take(x_val_size).batch(2)
        x_test = x_input.skip(x_train_size + x_val_size).batch(2)
        return x_train, x_val, x_test

    def train_and_save_model(self, subCategory, epochs, steps_per_epoch, save_path):
        df = self.get_filtered_df(subCategory)
        data = self.make_input_array(df)
        train, val, test = self.prepare_data(data)
        model = self.build_model(80, 60)
        model.summary()
        model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        history = model.fit(train, epochs=epochs, steps_per_epoch=steps_per_epoch, validation_data=val)
        model.evaluate(test)
        model.save(save_path)
        return history

if __name__ == "__main__":
    styles_path = r"data\styles.csv"
    images_path = r"data\images"

    recommender = FashionProductRecommender(styles_path, images_path)

    recommender.train_and_save_model("Topwear", epochs=10, steps_per_epoch=500, save_path="/models/model_top")
    recommender.train_and_save_model("Bottomwear", epochs=15, steps_per_epoch=50, save_path="/models/model_bottom")
    recommender.train_and_save_model("Footwear", epochs=5, steps_per_epoch=2000, save_path="/models/model_foot")
