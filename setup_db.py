import psycopg2
import os


def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ.get("DATABASE_HOST", "localhost"),
        database="movies_db",
        user="postgres",
        password="modric19"
    )
    return connection



def create_table(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY,
            title TEXT,
            year TEXT,
            rating TEXT,
            genres TEXT[],
            director TEXT[],
            writers TEXT[],
            stars TEXT[]
        )
    ''')

    connection.commit()
    cursor.close()


if __name__ == "__main__":
    connection = connect_to_db()
    create_table(connection)
    connection.close()
    print("Tabela criada com sucesso!!!")
