from collections import defaultdict
from random import choice, choices
from Filter import StartSentenceFilter, EndSentenceFilter

from nltk import trigrams

from AbstractPhraseMaker import AbstractPhraseMaker


class TrigramPhraseMaker(AbstractPhraseMaker):
    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.ngrams_organize(self.to_trigrams())

    def to_trigrams(self) -> list[tuple[str, str]]:
        """
        Return a list of trigrams from the list of tokens
        :return: List of trigrams
        """
        return list(trigrams(self.tokens))

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
            if len(" ".join(sentence).split()) >= 5 and (position := self.find_punctuation(next_word)) != 0:
                sentence[-1] = sentence[-1][:position + 1]
                break
            prev = f"{prev.split(' ')[-1]} {next_word}"

        self.sentence_list += [" ".join(sentence)]

    def ngrams_organize(self, trigrams: list[tuple[str, str]]):
        """
        Return a dictionary of ngrams where the keys are the first word of the bigram and the values are the second word
        of the bigram
        :param trigrams: The list of bigrams
        :return: A dictionary of bigrams
        """
        trigrams_dict: defaultdict[str, dict[str, int]] = defaultdict(dict)
        for head, middle, tail in trigrams:
            prev = f"{head} {middle}"
            trigrams_dict[prev].setdefault(tail, 0)
            trigrams_dict[prev][tail] += 1
        self.n_grams = dict(trigrams_dict)
