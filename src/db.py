from utils import TableManager

class DB:

    def __init__(self, engine):
        self.engine = engine
        self.tm = TableManager()

    def create_all_tables(self):
        self.tm.create_all_tables(self.engine)

    def drop_all_tables(self):
        self.tm.drop_all_tables(self.engine)