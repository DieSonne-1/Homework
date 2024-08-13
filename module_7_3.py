import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for p in punctuation:
                        line = line.replace(p, '')
                    words.extend(line.split())
                    all_words[file_name] = words
                return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                return {file_name: words.index(word)+1}
            else:
                return result

    def count(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего