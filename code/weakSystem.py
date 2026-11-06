import mysql.connector as conn

def prepare_query(name:str)->str:
    if name == "":
        raise ValueError("Please enter a name.")
    query = "SELECT * FROM table WHERE name = " + name
    return query

def execute_query(connection:conn.MySQLConnection, query:str)->list:
    cursor = connection.cursor()
    cursor.execute(query)
    response = cursor.fetchall()
    cursor.close()
    return response

def read_response(response:list):
    for row in response:
        print(row)