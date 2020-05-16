from nltk.stem.snowball import EnglishStemmer


class WordComparison(object):
    def __init__(self, starting_word):
        self.starting_word = starting_word
        self.user_submissions = dict()

    def get_unique_words(self):
        """Compare a starting word and a group of user submitted words.
           Return a list unique words, with matching user.
        """
        stemmer = EnglishStemmer()

        #Make starting list
        list_of_words = list(self.user_submissions.values())
        #Lower case all words for comparison
        list_of_words = [word.lower() for word in list_of_words]
        list_of_words.append(self.starting_word)
        #TODO Remove identical unique_words.
        stemmed_dict = dict()
        for word in list_of_words:
            stemmed_dict[word] = stemmer.stem(word)

        unique_words = [key for key, value in stemmed_dict.items()
                        if list(stemmed_dict.values()).count(value) == 1]
        if self.starting_word in unique_words:
            unique_words.remove(self.starting_word)
        return unique_words
