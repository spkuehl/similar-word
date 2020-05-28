from nltk.stem.snowball import EnglishStemmer
from collections import Counter


class WordComparison(object):
    def __init__(self, prompt):
        self.prompt = prompt
        self.user_submissions = dict()

    def get_unique_words_by_stemming(self):
        """Compare a starting word and a group of user submitted words.
           Return a list unique words, with matching user.
        """
        stemmer = EnglishStemmer()

        #Make starting list
        list_of_words = list(self.user_submissions.values())
        #Lower case all words for comparison
        list_of_words = [word.lower() for word in list_of_words]
        #Add starting word to list.
        list_of_words.append(self.prompt)
        #Remove identical unique_words.
        counter_of_words = Counter(list_of_words)
        list_of_words = []
        for word in counter_of_words:
            if counter_of_words[word] == 1:
                list_of_words.append(word)

        stemmed_dict = dict()
        for word in list_of_words:
            stemmed_dict[word] = stemmer.stem(word)

        unique_words = [key for key, value in stemmed_dict.items()
                        if list(stemmed_dict.values()).count(value) == 1]
        if self.prompt in unique_words:
            unique_words.remove(self.prompt)
        return unique_words

    def get_unique_words_by_letter_matching(self):
        pass
