from translate import Translator

_translator_en_ru = Translator(from_lang='en', to_lang='ru')
_translator_ru_en = Translator(from_lang='ru', to_lang='en')


def _trans_en_ru(word):
    return _translator_en_ru.translate(word)


def _trans_ru_en(word):
    return _translator_ru_en.translate(word)
