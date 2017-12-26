class Person:
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def cry(self):
        print("i'm {0}, i'm crying".format(self._name))
        print("i'm {name}, i'm crying".format(name=self._name))
