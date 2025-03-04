import sqlite3

def ler_comandos_sql(path):
    with open(path, 'r') as file:
        return file.read()

with sqlite3.connect("../sample.db") as connection:
    c = connection.cursor()
    comados_sql = ler_comandos_sql("sql.sql")
    c.executescript(comados_sql)