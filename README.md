# SQL Injection
ITIS 3200 Group Project

Topic: SQL Injection Remediation for a Given Vulnerable Query Layer

Domain: Web Security

Group Members:
- Daniel Mendoza (dmendo11@charlotte.edu)
- Dev Patel (dpate217@charlotte.edu)
- Everett Pohl (epohl@charlotte.edu)
- Nikhil Vundela (nvundela@charlotte.edu)

Prerequisite: Install the Python/SQL Connector and Streamlit packages:

```
pip install mysql-connector-python
pip install streamlit
```

Prerequisite: Setup a MySQL Connection:

Make sure to set up MySQL on your device. Find more information at: https://dev.mysql.com/doc/refman/9.7/en/installing.html

For this demo, we used MySQL Workbench to handle the connection and database on our local computers. Find more
information at: https://dev.mysql.com/doc/workbench/en/wb-installing.html

Once you have set up MySQL, Workbench, and a localhost connection, you can create the demo database.
In Workbench, or your IDE of choice, run the SQL files located on the [SQL Folder](sql) in this order:

1. database.sql to set up the database
2. accounts.sql to set up connections
3. demo.sql to ensure queries can be executed

Running the Demonstration: Use the following command instead of a normal Python command:

```
streamlit run code/main.py
```

[Project Proposal](docs/course_proposal.pdf)

[Project Code](code)

[MySQL Workbench SQL scripts](sql)

[Project Final Report](N/A)
