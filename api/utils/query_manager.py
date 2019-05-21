from hashlib import sha384

class QueryManager:

    @staticmethod
    def find_user(engine, email, log_level=0):
        if log_level == 1:
            print("Checking for user: {}".format(email))

        query = "SELECT * FROM users WHERE email='{}'".format(email)
        result = engine.execute(query).fetchone()
        if not result:
            return (None, None, None, None, None)
        return result

    @staticmethod
    def create_user(engine, firstname, lastname, email, password, log_level=0):
        if log_level == 1:
            print("\tCreating user: {}".format(email))
            print("\t\tfirstname: {}".format(firstname))
            print("\t\tlastname: {}".format(lastname))

        password = sha384(password.encode()).hexdigest()
        query = "INSERT INTO users(firstname, lastname, email, password) VALUES('{}', '{}', '{}', '{}');".format(firstname, lastname, email, password)
        engine.execute(query)