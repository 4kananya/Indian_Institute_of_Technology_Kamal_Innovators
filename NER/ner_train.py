from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from flair.visual.training_curves import Plotter

class NERTrainer:
    def __init__(self, data_folder, train_file, test_file, dev_file, model_output_folder):
        self.data_folder = data_folder
        self.train_file = train_file
        self.test_file = test_file
        self.dev_file = dev_file
        self.model_output_folder = model_output_folder
        self.columns = {0: 'text', 1: 'ner'}
        
    def prepare_corpus(self):
        self.corpus = ColumnCorpus(
            self.data_folder, 
            self.columns,
            train_file=self.train_file,
            test_file=self.test_file,
            dev_file=self.dev_file
        )
        self.label_dict = self.corpus.make_label_dictionary(label_type='ner')
        
    def create_embeddings(self):
        self.embedding_types = [
            WordEmbeddings('glove'),
            FlairEmbeddings('news-forward'),
            FlairEmbeddings('news-backward'),
        ]
        self.embeddings = StackedEmbeddings(embeddings=self.embedding_types)
        
    def initialize_tagger(self):
        self.tagger = SequenceTagger(
            hidden_size=256,
            embeddings=self.embeddings,
            tag_dictionary=self.label_dict,
            tag_type='ner',
            use_crf=True
        )
        
    def train_model(self, learning_rate=0.1, mini_batch_size=32, max_epochs=20):
        self.trainer = ModelTrainer(self.tagger, self.corpus)
        self.trainer.train(
            self.model_output_folder,
            learning_rate=learning_rate,
            mini_batch_size=mini_batch_size,
            max_epochs=max_epochs
        )
        
    def plot_training_curves(self):
        plotter = Plotter()
        plotter.plot_training_curves(f'{self.model_output_folder}/loss.tsv')

if __name__ == "__main__":
    data_folder = r'data'
    train_file = r'output_train.txt'
    test_file = r'output_test.txt'
    dev_file = r'output_dev.txt'
    model_output_folder = r'model'

    trainer = NERTrainer(data_folder, train_file, test_file, dev_file, model_output_folder)
    trainer.prepare_corpus()
    trainer.create_embeddings()
    trainer.initialize_tagger()
    trainer.train_model()
    trainer.plot_training_curves()
