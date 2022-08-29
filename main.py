from PhraseMaker.BigramPhraseMaker import BigramPhraseMaker
from PhraseMaker.TriGramPhraseMaker import TrigramPhraseMaker


def bigram_phrase_maker():
    filename: str = input()
    bigram_phrase_maker: BigramPhraseMaker = BigramPhraseMaker(filename)
    bigram_phrase_maker.make_paragraph()
    print(bigram_phrase_maker.paragraph)


def trigram_phrase_maker():
    filename: str = input()
    trigram_phrase_maker: TrigramPhraseMaker = TrigramPhraseMaker(filename)
    trigram_phrase_maker.make_paragraph()
    print(trigram_phrase_maker.paragraph)


if __name__ == '__main__':
    trigram_phrase_maker()