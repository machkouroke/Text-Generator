from abc import ABC, abstractmethod

from nltk import regexp_tokenize


class AbstractPhraseMaker(ABC):
    def __init__(self, file_name: str):
        self.tokens: list[str] = self.token_read(file_name)
        self.sentence_list: list[str] = []
        self.n_grams: dict[str, dict[str, int]] = {}

    @staticmethod
    def find_punctuation(word: str) -> int:
        if punc := set(word) & set(".?!"):
            return min(word.index(p) for p in punc)
        return 0

    @staticmethod
    def token_read(file_name: str) -> list[str]:
        """
        Read a file and return a list of tokens
        :param file_name: File from which we will read the tokens
        :return: A list of tokens. We suppose that the tokens are separated by spaces only.
        """
        with open(file_name, encoding="UTF-8") as corpus:
            text: str = corpus.read()
            tokens: list = regexp_tokenize(text, r"[\S]+")
        return tokens

    @abstractmethod
    def ngrams_organize(self, bigrams: list[tuple[str, str]]) -> dict[str, dict[str, int]]:
        pass

    @property
    def paragraph(self) -> str:
        return "\n".join(self.sentence_list)

    def make_paragraph(self, n: int = 10) -> None:
        for _ in range(n):
            self.phrase_maker()
