-- This file only gives an overview of what the tables should look like
-- The actually queries are executed in src/utils/table_manager.py
DROP TABLE IF EXISTS users, leases, tenants, managers, owners, due_leases, pending_leases;

CREATE TABLE users (
	firstname TEXT,
	lastname TEXT,
	email TEXT NOT NULL UNIQUE,
	PASSWORD TEXT NOT NULL,
	user_id SERIAL PRIMARY KEY);

CREATE TABLE leases (
	address TEXT,
	monthly_rent NUMERIC (5, 2),
	start_date DATE,
	end_date DATE,
	payment_day INT CHECK (payment_day <= 31),
	lease_id SERIAL PRIMARY KEY);

CREATE TABLE tenants (
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE managers (
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE owners (
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE due_leases (
    user_id INTEGER,
    lease_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (lease_id) REFERENCES leases(lease_id)
);

CREATE TABLE pending_leases (
    user_id INTEGER,
    lease_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (lease_id) REFERENCES leases(lease_id)
);