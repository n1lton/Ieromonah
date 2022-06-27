import sqlite3


class DataBase:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
           cls.__instance = super().__new__(cls)
        return cls.__instance


    def __del__(self):
        self.__instance = None


    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()