import mysql.connector


def connectionDB():
    try:
        connection=mysql.connector.connect(
            host ="localhost",
            user="root",
            passwd="admin123",
            database="app_empresa_db",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True
        )
        if connection.is_connected():
            return connection
    except mysql.connector.error as error:
        print(f"No se pudo conectar: {error}")