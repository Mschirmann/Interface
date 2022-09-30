from sqlite3 import Error


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
        except AttributeError:
            self.connection.close()
            print("Faça a conexão.")

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

    def get_all_os(self, os_id=None):
        try:
            sql = "SELECT * FROM os"
            cursor = self.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return list(results)
        except Error as e:
            return "Não foi possível executar a consulta. " + str(e)
