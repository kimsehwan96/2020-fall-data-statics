# for custom exception
import abc


class BaseException(Exception, abc.ABCMeta):
    def __str__(self):
        return "Error occured"
# custom error 구현 필요, BaseException 상속받아서.