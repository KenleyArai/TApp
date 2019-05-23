from utils import TableManager
from utils import QueryManager

class DBFactory:

    def __init__(self, engine, log_level=0):
        self.engine = engine
        self.tm = TableManager()
        self.qm = QueryManager()
        self.log_level = log_level

    def create_all_tables(self):
        self.tm.create_all_tables(self.engine, self.log_level)

    def drop_all_tables(self):
        self.tm.drop_all_tables(self.engine, self.log_level)

    def create_user(self, firstname, lastname, email, password):
        self.qm.create_user(self.engine, firstname, lastname, email, password, self.log_level)

    def find_user(self, email):
        return self.qm.find_user(self.engine, email, self.log_level)

    def create_owner(self, user_id):
        self.qm.create_owner(self.engine, user_id, self.log_level)

    def create_manager(self, user_id):
        self.qm.create_manager(self.engine, user_id, self.log_level)

    def create_tenant(self, user_id):
        self.qm.create_tenant(self.engine, user_id, self.log_level)
