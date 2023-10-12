from ctypes import CDLL

class LenError(Exception): ...
class FlagError(Exception): ...


_users_base_path = "C:\\openbot\\bin\\users.dll"
_users_base = CDLL(_users_base_path)

class Users:
    FLAGS = {
        _users_base.hash_str(b"None"): "None",
        _users_base.hash_str(b"EN-RU"): "EN-RU",
        _users_base.hash_str(b"RU-EN"): "RU-EN"
    }

    @staticmethod 
    def hash_str(text: str) -> int:
        '''Возвращает хэш массива чаров
           по кастомной хэш-функции.
           Она подвержена множеству коллизий,
           ну а у меня что, флагов много что-ли (:'''
        
        if len(text) > 5:
            raise LenError(
                "Лучше уменьши длину хэшируемого текста, иначе могут быть траблы"
            )
        
        return _users_base.hash_str(text.encode())
    
    @staticmethod
    def check_username_id(_username: str, _id: int) -> None:
        '''Составляет валидный список пользователей
           и их настроек'''
        
        _users_base.check_username_id(_username.encode(), _id) 
    
    @staticmethod
    def get_id(_username: str) -> int:
        '''Возвращает TG_id пользователя по username'''

        return _users_base.get_id(_username.encode())
    
    @classmethod
    def get_act_flag(cls, _username: str) -> str:
        '''Возвращает флаг действий пользователя по username.
           Если пользователя не существует, то возвращает -1.
           В ином случае - 0'''

        hash_flag = _users_base.get_act_flag(_username.encode())
        return cls.FLAGS[hash_flag]
    
    @classmethod
    def set_act_flag(cls, _username: str, _flag: str) -> int:
        '''Изменяет флаг действий пользователя по username.
           Если пользователь не существует, то возвращает 1.
           В ином случае - 0'''
        
        hash_flag = cls.hash_str(_flag)

        if hash_flag not in cls.FLAGS:
            raise FlagError(f"Не существует флага действий {_flag}")
        
        return _users_base.set_act_flag(_username.encode(), hash_flag)
