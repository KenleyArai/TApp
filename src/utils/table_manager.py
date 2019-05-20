class TableManager:

    def create_all_tables(self, engine):
        print("Create")
        # Main tables
        self.create_users(engine)
        self.create_leases(engine)

        # Category tables
        self.create_tenants(engine)
        self.create_managers(engine)
        self.create_owners(engine)

        # Who belongs which lease
        self.create_tenant_lease(engine)
        self.create_manager_lease(engine)
        self.create_owner_lease(engine)

        # Leases that are active
        self.create_due_leases(engine)
        self.create_pending_lease(engine)

    def drop_all_tables(self, engine):
        print("Drop")
        pass

    def create_users(self, engine):
        pass

    def create_leases(self, engine):
        pass

    def create_tenants(self, engine):
        pass

    def create_managers(self, engine):
        pass

    def create_owners(self, engine):
        pass

    def create_tenant_lease(self, engine):
        pass

    def create_manager_lease(self, engine):
        pass

    def create_owner_lease(self, engine):
        pass

    def create_due_leases(self, engine):
        pass

    def create_pending_lease(self, engine):
        pass