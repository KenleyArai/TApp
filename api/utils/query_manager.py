from hashlib import sha384

class QueryManager:

    @staticmethod
    def find_user(engine, email):
        query = "SELECT email FROM users WHERE email='{}'".format(email)
        result = engine.execute(query).fetchall()
        return result != []

    @staticmethod
    def create_user(engine, firstname, lastname, email, password):
        password = sha384(password.encode()).hexdigest()
        query = "INSERT INTO users(firstname, lastname, email, password) VALUES('{}', '{}', '{}', '{}');".format(firstname, lastname, email, password)
        engine.execute(query)