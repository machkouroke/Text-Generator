from collections import defaultdict
from random import choice, choices
from Filter import StartSentenceFilter, EndSentenceFilter

from nltk import bigrams

from .AbstractPhraseMaker import AbstractPhraseMaker


class BigramPhraseMaker(AbstractPhraseMaker):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.ngrams_organize(self.to_bigrams())

    def phrase_maker(self):
        prev: str = choice(
            list(
                filter(
                    StartSentenceFilter.not_end_by_punctuation,
                    filter(StartSentenceFilter.is_capitalized, self.n_grams.keys())
                )
            )
        )
        sentence: list[str] = [prev]
        while True:
            next_word: str = \
                choices(population=list(self.n_grams[prev].keys()), weights=list(self.n_grams[prev].values()))[0]
            sentence += [next_word]
            if len(sentence) >= 5 and EndSentenceFilter.end_by_punctuation(next_word):
                break
            prev = next_word

        self.sentence_list += [" ".join(sentence)]

    def to_bigrams(self) -> list[tuple[str, str]]:
        """
        Return a list of bigrams from the list of tokens
        :return: List of bigrams
        """
        return list(bigrams(self.tokens))

    def ngrams_organize(self, bigrams: list[tuple[str, str]]):
        """
        Return a dictionary of ngrams where the keys are the first word of the bigram and the values are the second word
        of the bigram
        :param bigrams: The list of bigrams
        :return: A dictionary of bigrams
        """
        bigrams_dict: defaultdict[str, dict[str, int]] = defaultdict(dict)
        for head, tail in bigrams:
            bigrams_dict[head].setdefault(tail, 0)
            bigrams_dict[head][tail] += 1
        self.n_grams = dict(bigrams_dict)
