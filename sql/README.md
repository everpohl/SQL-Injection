# SQL setup for the group demo

Open a local MySQL administrator connection in Workbench (MySQL 8.0.18 or newer). On a fresh server/schema, execute 01_database.sql, then 02_accounts.sql once. Stop on any error. Save the passwords shown by CREATE USER in the two result grids. The scripts expect the database and account names to be available.

Create two localhost Workbench connections using the generated credentials. Run 03_demo.sql in the weak connection. The first query returns Notebook, the vulnerable query returns DEMO-V00-LOCKER, the bound attack input returns zero rows, and the bound ID 1 returns Notebook. The strong account can read the fields used by the app's searches across all three tables. It cannot modify rows or schema objects.

For the current Python app set DB_NAME=course_sql_demo_v00, DB_USER to the chosen database account and DB_PASSWORD to its generated password in the launching environment. DB_HOST defaults to localhost and DB_PORT to 3306. Run streamlit run code/main.py from the repository root. Restart with the other credentials to change database accounts. The radio button alone only changes query code.

The current app searches IDs. Its weak function compares text to an integer before querying, and the strong function requires an integer while Streamlit supplies text. These need app-side work for the live form demo. The app uses one database account for both radio choices, so the team needs to switch connections when demonstrating least privilege. If login is added, grant its verifier only the extra columns it needs. The fictional users maya, owen and riley share the lab password DemoLogin42!. Stored hashes use PBKDF2-HMAC-SHA256 with 600000 iterations, hex salt, and hex digest in algorithm$iterations$salt$digest format.

The four suffixes sum to 304, giving seed 0 modulo 16. With no TA mapping supplied, our group convention uses the two-digit seed in the schema name and fictional secret, and targets record ID seed + 1 (record 1 for this group). Keep the SQL-generation prompt and your verification notes for the course AI appendix.
