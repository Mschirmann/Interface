from sqlite3 import Error


class Users:
    def __init__(self, db_conn=None) -> None:
        self.connection = db_conn

    def insert_user(self, name, user, password, access):

        try:
            sql = 'INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)'
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, user, password, access))
            self.connection.commit()
        except AttributeError:
            self.connection.close()
            print("Faça a conexão.")

    def get_user(self, user=None):
        try:
            sql = 'SELECT * FROM users WHERE user="{}"'.format(user)
            cursor = self.connection.cursor()
            u = cursor.execute(sql)
            result = u.fetchone()
            if result is not None:
                return result
            else:
                return "Usuário não encontrado."
        except Error as e:
            return "Não foi possível executar a consulta. " + str(e)


    def check_user(self, user, password):
        sql = 'SELECT * FROM users'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)

            for linha in cursor.fetchall():
                if (
                    linha[2].upper() == user.upper()
                    and linha[3] == password
                    and linha[4] == "Administrador"
                ):
                    return "Administrador"
                elif (
                    linha[2].upper() == user.upper()
                    and linha[3] == password
                    and linha[4] == "Usuário"
                ):
                    return "user"
                else:
                    continue
            return "Sem acesso."
        except:
            pass
