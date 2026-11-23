#Strong System
#Check if input matches the expected data type (ID->int, name->string, etc.)
#Prepare query, bind parameter, execute, and fetch instead of appending
#Limit query response to 1 row so a full table cannot be returned

from mysql.connector import MySQLConnection

tables = ["users", "products"]

def prepare_query(table: str, id)->tuple[str, tuple]:
    if table not in tables:
        raise ValueError("Invalid Table")
    try:
        int(id)
    except:
        raise ValueError("Invalid ID")
    # Strength: Each query is limited to only 1 return result, additionally input is parameterized, which prevents any of the input from functioning as a sql statement
    if table == tables[0]:
        query = "SELECT username, role, email FROM users WHERE user_id = %s LIMIT 1"
    elif table == tables[1]:
        query = "SELECT name, price, description FROM products WHERE product_id = %s LIMIT 1"
    return query, (id,)

def execute_query(connection, query: str, id: tuple):
    # Strength: Uses a prepared cursor, which separates the user data from the SQL command
    cursor = connection.cursor(prepared = True)
    #Strength: Query is parameterized
    cursor.execute(query, id)
    # Strength: fetchone() will only return one result
    response = cursor.fetchone()
    cursor.close()
    return response