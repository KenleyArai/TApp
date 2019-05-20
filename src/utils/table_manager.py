class TableManager:

    def create_all_tables(self, engine, log_level=0):

        if log_level == 1:
            print("\tCreating all tables...")

        # Main tables
        self.create_users(engine, log_level)
        self.create_leases(engine, log_level)

        # Category tables
        self.create_tenants(engine, log_level)
        self.create_managers(engine, log_level)
        self.create_owners(engine, log_level)

        # Who belongs which lease
        self.create_tenant_lease(engine, log_level)
        self.create_manager_lease(engine, log_level)
        self.create_owner_lease(engine, log_level)

        # Leases that are active
        self.create_due_leases(engine, log_level)
        self.create_pending_lease(engine, log_level)
        if log_level == 1:
            print("\tDone creating all tables...")

    def drop_all_tables(self, engine, log_level=0):
        if log_level == 1:
            print("\tDropping all tables...")

        engine.execute("DROP TABLE IF EXISTS users, leases, tenants, managers, owners, due_leases, pending_leases;")
        if log_level == 1:
            print("\tDone droppping all tables...")

    def create_users(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating users table...")

        engine.execute("""
            CREATE TABLE users (
            firstname TEXT,
            lastname TEXT,
            email TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL,
            user_id SERIAL PRIMARY KEY);
        """)

    def create_leases(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating leases table...")


    def create_tenants(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating tenants table...")

    def create_managers(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating managers table...")

    def create_owners(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating owners table...")

    def create_tenant_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating tenant_lease relation table...")

    def create_manager_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating manager_lease relation table...")

    def create_owner_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating owner lease relation table...")

    def create_due_leases(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating due leases relation table...")

    def create_pending_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating pending lease relation table...")