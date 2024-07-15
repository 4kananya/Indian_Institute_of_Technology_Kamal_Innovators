import pandas as pd
import random

class OutfitGenerator:
    def __init__(self, top_file = r"database\top.csv", bottom_file = r"database\bottom.csv", shoes_file = r"database\footwear.csv"):
        self.top_df = pd.read_csv(top_file)
        self.bottom_df = pd.read_csv(bottom_file)
        self.shoes_df = pd.read_csv(shoes_file)

    def generate_outfit(self, item_id):
        selected_top = None
        selected_bottom = None
        selected_shoes = None

        if item_id in self.top_df['id'].values:
            selected_item = self.top_df[self.top_df['id'] == item_id].iloc[0]
            selected_top = selected_item
        elif item_id in self.bottom_df['id'].values:
            selected_item = self.bottom_df[self.bottom_df['id'] == item_id].iloc[0]
            selected_bottom = selected_item
        elif item_id in self.shoes_df['id'].values:
            selected_item = self.shoes_df[self.shoes_df['id'] == item_id].iloc[0]
            selected_shoes = selected_item
        else:
            raise ValueError("Item ID not found in any category")

        season = selected_item['season']

        top_options = self.top_df[self.top_df['season'] == season]
        bottom_options = self.bottom_df[self.bottom_df['season'] == season]
        shoes_options = self.shoes_df[self.shoes_df['season'] == season]

        if selected_top is not None:
            bottom_colour_group, footwear_colour_group = self.find_combo_by_top(selected_top['colorgroup'])
            bottom_options = bottom_options[bottom_options['colorgroup'] == bottom_colour_group]
            shoes_options = shoes_options[shoes_options['colorgroup'] == footwear_colour_group]
        if selected_bottom is not None:
            top_colour_group, footwear_colour_group = self.find_combo_by_bottom(selected_bottom['colorgroup'])
            top_options = top_options[top_options['colorgroup'] == top_colour_group]
            shoes_options = shoes_options[shoes_options['colorgroup'] == footwear_colour_group]
        if selected_shoes is not None:
            top_colour_group, bottom_colour_group = self.find_combo_by_foot(selected_shoes['colorgroup'])
            top_options = top_options[top_options['colorgroup'] == top_colour_group]
            bottom_options = bottom_options[bottom_options['colorgroup'] == bottom_colour_group]

        if selected_top is None:
            selected_top = top_options.sample().iloc[0] if not top_options.empty else self.top_df.sample().iloc[0]
        if selected_bottom is None:
            selected_bottom = bottom_options.sample().iloc[0] if not bottom_options.empty else self.bottom_df.sample().iloc[0]
        if selected_shoes is None:
            selected_shoes = shoes_options.sample().iloc[0] if not shoes_options.empty else self.shoes_df.sample().iloc[0]

        return {
            'top': selected_top.to_dict(),
            'bottom': selected_bottom.to_dict(),
            'shoes': selected_shoes.to_dict()
        }

    @staticmethod
    def find_combo_by_bottom(bottom_color_group):
        combotype = OutfitGenerator.find_combotype_by_color_group(bottom_color_group)
        co = int(combotype / 30)

        if bottom_color_group == 15:
            top_color_group = random.choice([12, 13, 14])
            shoes_color_group = 13 if top_color_group == 12 else random.choice([12, 13, 14])
        elif bottom_color_group in [12, 13, 14]:
            top_color_group = random.choice([12, 13])
            shoes_color_group = 13 if top_color_group == 12 else random.choice([12, 13])
        else:
            top_color_group = random.choice([bottom_color_group - co, bottom_color_group + co])
            shoes_color_group = bottom_color_group + co if top_color_group == bottom_color_group - co else bottom_color_group - co

        return top_color_group, shoes_color_group

    @staticmethod
    def find_combo_by_foot(shoes_color_group):
        combotype = OutfitGenerator.find_combotype_by_color_group(shoes_color_group)
        co = int(combotype / 30)

        if shoes_color_group == 15:
            top_color_group = random.choice([12, 13, 14])
            bottom_color_group = 13 if top_color_group == 12 else random.choice([12, 13, 14])
        elif shoes_color_group in [12, 13, 14]:
            top_color_group = random.choice([12, 13])
            bottom_color_group = 13 if top_color_group == 12 else random.choice([12, 13])
        else:
            top_color_group = random.choice([shoes_color_group - co, shoes_color_group + co])
            bottom_color_group = shoes_color_group + co if top_color_group == shoes_color_group - co else shoes_color_group - co

        return top_color_group, bottom_color_group

    @staticmethod
    def find_combo_by_top(top_color_group):
        combotype = OutfitGenerator.find_combotype_by_color_group(top_color_group)
        co = int(combotype / 30)

        if top_color_group == 15:
            bottom_color_group = random.choice([12, 13, 14])
            shoes_color_group = 13 if bottom_color_group == 12 else random.choice([12, 13, 14])
        elif top_color_group in [12, 13, 14]:
            bottom_color_group = random.choice([12, 13])
            shoes_color_group = 13 if bottom_color_group == 12 else random.choice([12, 13])
        else:
            bottom_color_group = random.choice([top_color_group - co, top_color_group + co])
            shoes_color_group = top_color_group + co if bottom_color_group == top_color_group - co else top_color_group - co

        return bottom_color_group, shoes_color_group

    @staticmethod
    def find_combotype_by_color_group(color_group):
        if color_group == 15:
            return 90
        elif color_group in [12, 13, 14]:
            return 0
        else:
            return (color_group % 12) * 30
