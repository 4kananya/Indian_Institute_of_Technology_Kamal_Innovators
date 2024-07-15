import json
import re
import random

class DataProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = self.extract_descriptions_and_attributes()

    def extract_descriptions_and_attributes(self):
        try:
            with open(self.input_file, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File not found: {self.input_file}")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.input_file}")
            return []

    def label_words_with_attributes(self, description, entry):
        words = re.findall(r'\w+|[^\w\s]', description.lower())
        bio_tags = ['O'] * len(words)

        for attribute, value in entry.items():
            if attribute in ['description', 'url'] or value == 'Not specified':
                continue
            entity_phrase = str(value).lower()
            entity_type = attribute.upper()
            entity_words = re.findall(r'\w+|[^\w\s]', entity_phrase)
            entity_length = len(entity_words)

            for i in range(len(words) - entity_length + 1):
                if words[i:i + entity_length] == entity_words:
                    bio_tags[i] = f"B-{entity_type}"
                    for j in range(1, entity_length):
                        bio_tags[i + j] = f"I-{entity_type}"

            if entity_type == "TYPE":
                item = []
                for word in entity_words:
                    item.append(word)
                    item.append(word + "s")
                    item.append(word[:-1])
                entity_words = item
            for i in range(len(words)):
                if bio_tags[i] == "O":
                    flag = 0
                    while words[i] in entity_words:
                        if flag == 0:
                            bio_tags[i] = f"B-{entity_type}"
                            i += 1
                            flag = 1
                        else:
                            bio_tags[i] = f"I-{entity_type}"
                            i += 1
                        if i == len(words):
                            break

        return words, bio_tags

    def convert_to_conll(self, data):
        conll_data = []
        for entry in data:
            description = entry.get('description', '')
            words, bio_tags = self.label_words_with_attributes(description, entry)
            for word, tag in zip(words, bio_tags):
                conll_data.append(f"{word} {tag}")
            conll_data.append("")
        return conll_data

    def save_conll(self, conll_data, output_file):
        try:
            with open(output_file, 'w') as file:
                for line in conll_data:
                    file.write(line + '\n')
            print(f"Data successfully written to {output_file}")
        except IOError as e:
            print(f"An error occurred while writing to the file {output_file}: {e}")

    def split_and_save_data(self, train_ratio=0.7, dev_ratio=0.175):
        random.shuffle(self.data)
        total_data = len(self.data)
        train_size = int(total_data * train_ratio)
        dev_size = int(total_data * dev_ratio)

        train_data = self.data[:train_size]
        dev_data = self.data[train_size:train_size + dev_size]
        test_data = self.data[train_size + dev_size:]

        train_conll = self.convert_to_conll(train_data)
        dev_conll = self.convert_to_conll(dev_data)
        test_conll = self.convert_to_conll(test_data)

        self.save_conll(train_conll, r'data\output_train.txt')
        self.save_conll(dev_conll, r'data\output_dev.txt')
        self.save_conll(test_conll, r'data\output_test.txt')

        print("Data has been split and saved into output_train.txt, output_dev.txt, and output_test.txt.")

if __name__ == "__main__":
    processor = DataProcessor(r'data\converted_data.json')
    processor.split_and_save_data()