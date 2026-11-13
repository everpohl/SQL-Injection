import os

import mysql.connector
import streamlit as st

import weakSystem
import strongSystem


def connect_to_database():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )


def main():
    st.title("SQL Injection Demo")

    st.write(
        "Search for a user and compare how the weak and strong systems "
        "handle the same input."
    )

    system_choice = st.radio(
        "Choose a system:",
        ["Weak System", "Strong System"]
    )

    table_choice = st.radio(
        "Choose a table:",
        ["users", "products", "private_records"]
    )

    id = st.text_input("Enter a user/product/record ID:")

    if st.button("Search"):
        if id.strip() == "":
            st.warning("Please enter a user/product/record ID.")
            return

        connection = None

        try:
            connection = connect_to_database()

            if system_choice == "Weak System":
                query = weakSystem.prepare_query(table_choice, id)
                results = weakSystem.execute_query(connection, query)
            else:
                query = strongSystem.prepare_query(table_choice, id)
                results = strongSystem.execute_query(connection, query)

            if results:
                st.success("User information found.")

                st.dataframe(
                    results,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No matching user was found.")

        except KeyError:
            st.error(
                "The database username, password, or database name is missing."
            )

        except ValueError as error:
            st.error(str(error))

        except mysql.connector.Error as error:
            st.error(f"Database error: {error}")

        finally:
            if connection is not None and connection.is_connected():
                connection.close()


if __name__ == "__main__":
    main()
