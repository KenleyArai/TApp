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

    @staticmethod
    def create_owner(engine, user_id, log_level=0):
        if log_level == 1:
            print("\tCreating owner with user_id: {}".format(user_id))

        query = "INSERT INTO owners (user_id) VALUES ({})".format(user_id)
        engine.execute(query)

    @staticmethod
    def create_manager(engine, user_id, log_level=0):
        if log_level == 1:
            print("\tCreating manager with user_id: {}".format(user_id))

        query = "INSERT INTO managers (user_id) VALUES ({})".format(user_id)
        engine.execute(query)

    @staticmethod
    def create_tenant(engine, user_id, log_level=0):
        if log_level == 1:
            print("\tCreating tenant with user_id: {}".format(user_id))

        query = "INSERT INTO tenants (user_id) VALUES ({})".format(user_id)
        engine.execute(query)

    @staticmethod
    def get_roles(engine, user_id, log_level=0):
        if log_level == 1:
            print("\tFinding roles for user_id: {}".format(user_id))

        query = """
                SELECT
                    t.user_id as tenant,
                    m.user_id as manager,
                    o.user_id as owner
                FROM
                    users AS u
                LEFT OUTER JOIN
                    tenants AS t
                ON u.user_id = t.user_id
                LEFT OUTER JOIN
                    managers as m
                ON u.user_id = m.user_id
                LEFT OUTER JOIN
                    owners as o
                ON u.user_id = o.user_id
                WHERE u.user_id = {};
            """.format(user_id)
        roles = engine.execute(query).fetchone()
        if log_level == 1:
            print("\tFound roles: {}".format(roles))

        return roles