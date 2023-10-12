from var import _CONST


MESSAGE_START: _CONST = '''Привет! Я открытый многофункциональный бот.
Мои возможности дописываются и редактируются.
Более подробная информация: /help'''

MESSAGE_HELP: _CONST = '''Я Openbot!
Не имею определённого направления или функционала.
Мои возможности дописываются и редактируются по необходимости.
Вот что я умею на данный момент:

/id - ваш уникальный TelegramID
/translate - перевод слов
/crypto - информация об определённых криптовалютах'''

MESSAGE_UNKNOWN_TEXT: _CONST = '''Извини, со мной нельзя общаться.
Всё, что я умею, это отрабатывать команды.
С их списком можно ознакомиться, прописав /help'''

MESSAGE_SOME_FILE: _CONST = '''Ну и зачем мне это?
Понятия не имею, как с этим работать)'''

MESSAGE_TG_ID_GET: _CONST = "Your id: %i"

MESSAGE_TRANSLATE: _CONST = "Доступные варианты перевода: "

MESSAGE_SEND_TRANS_GET: _CONST = "Ок, вводишь слова, \nа я перевожу <b>%s</b>"

MESSAGE_END_TRANS: _CONST = "Ок, закончили"

MESSAGE_TRANS_ERROR: _CONST = "Извини, не смог перевести"

MESSAGE_TRANS: _CONST = MESSAGE_TRANS_ERROR # Переопределяется в options::trans при успешном переводе

MESSAGE_CRYPTO: _CONST = '''Ниже будет перечислен список с
информацией об определённых 
криптовалютах по версии
coinranking.com, соответствующей
следующему шаблону 
"<ticker> - <price> - <market_capitalization>":'''

MESSAGE_ABOUT_USDT: _CONST = '''К слову стоимость USDT сейчас
составляет {}, а его рыночная
капитализация - {}'''
