from flair.models import SequenceTagger
from flair.data import Sentence
import nltk

nltk.download('punkt')

class FashionTrendExtractor:
    MODEL_PATH = r'model\ner-model.pt' 
    
    def __init__(self):
        self.model = SequenceTagger.load(self.MODEL_PATH)
    
    def paragraph_to_sentences(self, paragraph):
        return nltk.sent_tokenize(paragraph)
    
    def combine_similar_types(self, fashion_trends):
        combined_trends = []
        for trend in fashion_trends:
            found = False
            for existing_trend in combined_trends:
                if any(t in existing_trend['TYPE'] for t in trend['TYPE']) or any(t in trend['TYPE'] for t in existing_trend['TYPE']):
                    for key in trend:
                        if key != 'TYPE' and trend[key]:
                            for item in trend[key]:
                                existing_trend[key].add(item)
                    found = True
                    break
            if not found:
                combined_trends.append(trend)
        return combined_trends
    
    def extract_fashion_trends(self, sentences):
        fashion_trends = []
        for sentence_text in sentences:
            sentence = Sentence(sentence_text)
            self.model.predict(sentence)
            trend_dict = {'TYPE': set(), 'MATERIAL': set(), 'STYLE': set(), 'DETAILS': set(), 'OCCASION': set(), 'COLOR': set(), 'GENDER': set()}
            for entity in sentence.get_spans('ner'):
                entity_text = entity.text.lower()
                if entity.tag in trend_dict:
                    trend_dict[entity.tag].add(entity_text)
            
            if trend_dict['TYPE']:
                fashion_trends.append(trend_dict)
        
        return fashion_trends
    
    def process_document(self, text_array):
        all_fashion_trends = []
        for text in text_array:
            sentences = self.paragraph_to_sentences(text)
            fashion_trends = self.extract_fashion_trends(sentences)
            all_fashion_trends.extend(fashion_trends)
        
        all_fashion_trends = self.combine_similar_types(all_fashion_trends)
        
        return all_fashion_trends