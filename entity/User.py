import pickle

import picle


class User:

    def __init__(self, auth, group):
        self.auth = auth
        self.group = group

#Сериализация в строку
def serialize(o):
    return pickle.dumps(o)

#Десериализация из строки
def deserialize(o):
    return pickle.loads(o)
