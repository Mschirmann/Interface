class Users:
    def __init__(self, db_conn=None) -> None:
        self.connection = db_conn

    def insert_user(self, name, user, password, access):

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """

                INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)

            """,
                (name, user, password, access),
            )
            self.connection.commit()
        except AttributeError:
            self.connection.close()
            print("Faça a conexão.")

    def check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
    
                SELECT * FROM users;

            """
            )

            for linha in cursor.fetchall():
                if (
                    linha[2].upper() == user.upper()
                    and linha[3] == password
                    and linha[4] == "Administrador"
                ):
                    return "Administrador"
                    break
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
