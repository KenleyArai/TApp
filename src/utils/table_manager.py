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

        engine.execute("""
                DROP TABLE IF EXISTS
                    users,
                    leases,
                    tenants,
                    managers,
                    owners,
                    tenant_lease,
                    manager_lease,
                    owner_lease,
                    due_leases,
                    pending_leases CASCADE;
                """)

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

        engine.execute("""
                CREATE TABLE leases (
                    address TEXT,
                    monthly_rent NUMERIC (5, 2),
                    start_date DATE,
                    end_date DATE,
                    payment_day INT CHECK (payment_day <= 31),
                    lease_id SERIAL PRIMARY KEY);
            """)

    def create_tenants(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating tenants table...")

        engine.execute("""
                CREATE TABLE tenants (
                    user_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id));
            """)

    def create_managers(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating managers table...")

        engine.execute("""
                CREATE TABLE managers (
                    user_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id));
            """)

    def create_owners(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating owners table...")

        engine.execute("""
                CREATE TABLE owners (
                    user_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id));
            """)

    def create_tenant_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating tenant_lease relation table...")

        engine.execute("""
                CREATE TABLE tenant_lease (
                    user_id INT,
                    lease_id INT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (lease_id) REFERENCES leases(lease_id));
            """)

    def create_manager_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating manager_lease relation table...")

        engine.execute("""
                CREATE TABLE manager_lease (
                    user_id INT,
                    lease_id INT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (lease_id) REFERENCES leases(lease_id));
            """)

    def create_owner_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating owner lease relation table...")

        engine.execute("""
                CREATE TABLE owner_lease (
                    user_id INT,
                    lease_id INT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (lease_id) REFERENCES leases(lease_id));

            """)

    def create_due_leases(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating due leases relation table...")

        engine.execute("""
                CREATE TABLE due_leases (
                    user_id INTEGER,
                    lease_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (lease_id) REFERENCES leases(lease_id));
            """)

    def create_pending_lease(self, engine, log_level=0):
        if log_level == 1:
            print("\t\tCreating pending lease relation table...")

        engine.execute("""
                CREATE TABLE pending_leases (
                    user_id INTEGER,
                    lease_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (lease_id) REFERENCES leases(lease_id));
            """)