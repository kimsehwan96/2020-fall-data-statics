import abc

class StaticHelperBaseClass(abc.ABCMeta):
    def __init__(self):
        self.command_map = [
            'mean',
            'devat',
            'diff'
        ]

    @abc.abstractmethod
    def mean(self):
        raise NotImplementedError

    @abc.abstractmethod
    def devat(self):
        raise NotImplementedError

    @abc.abstractmethod
    def diff(self):
        raise NotImplementedError
