from utils import TableManager

class DBFactory:

    def __init__(self, engine):
        self.engine = engine
        self.tm = TableManager()

    def create_all_tables(self, log_level=0):
        self.tm.create_all_tables(self.engine, log_level)

    def drop_all_tables(self, log_level=0):
        self.tm.drop_all_tables(self.engine, log_level)