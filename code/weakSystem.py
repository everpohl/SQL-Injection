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
    else:
        # Fault: Does not utilize SQL's prepare, just appends input
        query = ("SELECT B.username, A.title, A.secret_value FROM private_records A " +
                 "LEFT JOIN users B ON A.user_id = B.user_id " +
                 "WHERE record_id = '" + str(id) + "'")
    return query

def execute_query(connection:MySQLConnection, query:str):
    cursor = connection.cursor()
    # Fault: Executes a non-prepared query
    cursor.execute(query)
    # Fault: does not limit/restrict query response
    response = cursor.fetchall()
    cursor.close()
    return response