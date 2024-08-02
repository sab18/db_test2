import sqlite3


def initialize_database(db_title,table_name,*args):
    conn = sqlite3.connect(db_title)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table_name} {args}")

    conn.commit()
    cursor.close()
    conn.close()

db_title='src/db_test.db'
table_name='table_test'


initialize_database(db_title,table_name, 'name','col2')