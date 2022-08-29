from string import punctuation


class StartSentenceFilter:
    @staticmethod
    def is_capitalized(word: str):
        return word[0].upper() == word[0]

    @staticmethod
    def not_end_by_punctuation(word: str):
        return word[-1] not in punctuation and not set('.!?') & set(word)


class EndSentenceFilter:
    @staticmethod
    def end_by_punctuation(word: str):
        return word[-1] in {".", "!", "?"} or "." in word
