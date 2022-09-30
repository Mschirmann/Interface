from os import access
import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.name)
            return conn
        except Error as e:
            print(e)

        return conn

    def close_connection(self, conn):
        try:
            conn.close()
        except:
            pass

    def run_command(self, conn, sql_command):
        try:
            c = conn.cursor()
            c.execute(sql_command)
        except Error as e:
            print(e)

    def create_users_table(self):
        return """
                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL 
                );
            """

    def create_os_table(self):
        return """
                CREATE TABLE IF NOT EXISTS os(

                    id INTEGER NOT NULL PRIMARY KEY,
                    status TEXT DEFAULT 'Aberta',
                    created_at DATETIME NOT NULL,
                    closed_at DATETIME,
                    customer TEXT NOT NULL,
                    technical_manager TEXT NOT NULL,
                    service_start_dt DATETIME NOT NULL,
                    service_end_dt DATETIME NOT NULL,
                    service_description TEXT,
                    service_type TEXT NOT NULL,
                    equip_inventory_number VARCHAR(20),
                    equip_brand TEXT,
                    equip_name TEXT,
                    equip_model TEXT,
                    equip_props TEXT,
                    equip_defect TEXT,
                    equip_obs TEXT,
                    parts_used TEXT,
                    part_type TEXT,
                    part_quantity INTEGER,
                    part_unit_price FLOAT,
                    part_total FLOAT
                );
            """

    def main(self):
        conn = self.create_connection()
        if conn is not None:
            self.run_command(conn, self.create_users_table())
            self.run_command(conn, self.create_os_table())
            self.close_connection(conn)
        else:
            print("Não foi possível conectar com o banco de dados.")
