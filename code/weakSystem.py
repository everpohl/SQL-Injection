from mysql.connector import MySQLConnection

def prepare_query(table:str, id)->str:
    if table == "users":
        # Fault: Does not prepare query, just appends input
        query = ("SELECT username, role, email FROM users " +
                 "WHERE user_id = '" + str(id) + "'")
    elif table == "products":
        # Fault: Does not prepare query, just appends input
        query = ("SELECT name, price, description FROM products " +
                 "WHERE product_id = '" + str(id) + "'")
    return query

def execute_query(connection:MySQLConnection, query:str):
    cursor = connection.cursor()
    # Fault: Executes a non-prepared query
    cursor.execute(query)
    # Fault: does not limit/restrict query response
    response = cursor.fetchall()
    cursor.close()
    return response