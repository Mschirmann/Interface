from sqlite3 import Error
import sqlite3


class Os:
    def __init__(self, db_conn=None) -> None:
        self.connection = db_conn

    def insert_os(self, os_data):
        try:
            sql = "INSERT INTO os (status, created_at, closed_at , customer, technical_manager, service_start_dt, service_end_dt, service_description, service_type, equip_inventory_number, equip_brand , equip_name , equip_model , equip_props , equip_defect , equip_obs, parts_used, part_type, part_quantity, part_unit_price , part_total, id) \
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            cursor = self.connection.cursor()
            cursor.execute(sql, os_data)
            self.connection.commit()
            return True, cursor.lastrowid
        except Error as e:
            print("Faça a conexão.")
            return False, "Erro: " + str(e)

    def update_os(self, os_data):
        try:
            # OS id must be the first arg from os_data tuple
            sql = """ 
            UPDATE os SET status = ?, 
                created_at = ?, 
                closed_at = ?, 
                customer = ?, 
                technical_manager = ?, 
                service_start_dt = ?, 
                service_end_dt = ?, 
                service_description = ?,
                service_type = ?, 
                equip_inventory_number = ?,
                equip_brand = ?, 
                equip_name = ?,
                equip_model = ?,
                equip_props = ?, 
                equip_defect = ?, 
                equip_obs = ?, 
                parts_used = ?, 
                part_type = ?, 
                part_quantity = ?,
                part_unit_price = ?,
                part_total = ?
            WHERE id=?
            """
            cursor = self.connection.cursor()
            cursor.execute(sql, os_data)
            self.connection.commit()
        except AttributeError:
            self.connection.close()
            print("Faça a conexão.")

    def delete_os(self, os_id):
        try:
            sql = "DELETE FROM os WHERE id=?"
            cursor = self.connection.cursor()
            cursor.execute(sql, (os_id,))

            self.connection.commit()
        except Error as e:
            return "Não foi possível executar a consulta. " + str(e)

    def get_all_os(
        self,
        id=None,
        equip_inventory_number=None,
        equip_name=None,
        customer=None,
        status=None,
        dt_start=None,
        dt_end=None,
    ):
        try:
            have_filters = (
                id
                or equip_inventory_number
                or equip_name
                or customer
                or status
                or dt_start
                or dt_end
            )
            sql = "SELECT * FROM os"
            if have_filters:
                sql += " WHERE "
                if id:
                    sql += "id=" + id + " AND "
                if equip_inventory_number:
                    sql += "equip_inventory_number=" + id + " AND "
                if equip_name:
                    sql += "equip_name='" + equip_name + "' AND "
                if customer:
                    sql += "customer='" + customer + "' AND "
                if status:
                    sql += "status='" + status + "' AND "
                if dt_start and dt_end:
                    sql += "created_at BETWEEN '" + dt_start + "' AND '" + dt_end + "'"
                if sql.endswith(" AND "):
                    sql = sql[:-5]

            self.connection.row_factory = sqlite3.Row
            cursor = self.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return list(map(lambda x: dict(x), results))
        except Error as e:
            return "Não foi possível executar a consulta. " + str(e)

    def get_os(self, os_id=None):
        try:
            sql = "SELECT * FROM os WHERE id=?"
            self.connection.row_factory = sqlite3.Row
            cursor = self.connection.cursor()
            cursor.execute(sql, (os_id,))
            result = cursor.fetchone()
            return dict(result)
        except Error as e:
            return "Não foi possível executar a consulta. " + str(e)

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
