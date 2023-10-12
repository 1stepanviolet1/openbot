from telebot import TeleBot
from options import (
    start,
    help,
    some_text,
    some_file,
    delete_some_file,
    get_tg_id,
    translate,
    send_trans,
    crypto_info
)
from constant.consts import (
    DATA_DELETE_FILE,
    LIST_OF_UNKNOWN_CONTENT_TYPES,
    TOKEN,
    DATA_TRANS
)


class Openbot(TeleBot):
    def __init__(self):
        super().__init__(TOKEN)

        self.message_handler(['start'])(self.__start)
        self.message_handler(['help'])(self.__help)
        self.message_handler(['id'])(self.__get_tg_id)
        self.message_handler(['translate'])(self.__translate)
        self.message_handler(['crypto'])(self.__crypto_info)

        self.message_handler(content_types=LIST_OF_UNKNOWN_CONTENT_TYPES)(self.__some_file)

        self.callback_query_handler(self.__is_data_delete_file)(self.__delete_some_file)
        self.callback_query_handler(self.__is_data_trans)(self.__send_trans)

        self.message_handler()(self.__some_text)

    def run(self):
        self.infinity_polling(timeout=None) # TODO: обработка истечения timeout'а

    @staticmethod
    def __is_data_delete_file(callback):
        return callback.data == DATA_DELETE_FILE
    
    @staticmethod
    def __is_data_trans(callback):
        return callback.data in DATA_TRANS
    
    def __start(self, session):
        start(self, session)
    
    def __help(self, session):
        help(self, session)
    
    def __some_text(self, session):
        some_text(self, session)
    
    def __some_file(self, session):
        some_file(self, session)
    
    def __delete_some_file(self, session):
        delete_some_file(self, session)
    
    def __get_tg_id(self, session):
        get_tg_id(self, session)
    
    def __translate(self, session):
        translate(self, session)
    
    def __send_trans(self, session):
        send_trans(self, session)
    
    def __crypto_info(self, session):
        crypto_info(self, session)
    

if __name__ == '__main__':
    Openbot().run()
