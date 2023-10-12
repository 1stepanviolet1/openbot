from typing import TypeVar
from users import Users


_CONST = TypeVar('_CONST', str, None)


class CREATE_ACT_FLAG:
    @staticmethod
    def get(_username:  str):
        return Users.get_act_flag(_username)
    
    @staticmethod
    def set(_username:  str, flag: str) -> int:
        return Users.set_act_flag(_username, flag)
    
    def __eq__(self, __value: str) -> bool:
        return self.get() == __value
