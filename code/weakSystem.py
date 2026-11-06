import mysql.connector as conn

def prepare_query(name:str)->str:
    # Fault: Checks for non-empty input but not for potential injection
    if name == "":
        raise ValueError("Please enter a name.")
    # Fault: Does not prepare query, just appends input
    query = "SELECT * FROM table WHERE name = " + name
    return query

def execute_query(connection:conn.MySQLConnection, query:str)->list:
    cursor = connection.cursor()
    # Fault: Executes a non-prepared query
    cursor.execute(query)
    # Fault: does not limit/restrict query response
    response = cursor.fetchall()
    cursor.close()
    return response

def read_response(response:list):
    for row in response:
        print(row)