class Study:  # pylint: disable=too-few-public-methods
    __slots__ = ('test','_score','__fullname')
    def __init__(self, firstname, lastname):
       self.__fullname = firstname + ':' + lastname

    def cal(self):
        result = 0
        cc = range(1001)
        for i in cc:
            result += i
        #for i in range(8)
        print(result)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score= value
