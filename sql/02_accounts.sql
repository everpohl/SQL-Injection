-- Run once as administrator. Save each generated password from its result grid.
CREATE USER 'course_demo_v00_weak'@'localhost' IDENTIFIED BY 'weak';
CREATE USER 'course_demo_v00_strong'@'localhost' IDENTIFIED BY 'strong';
GRANT SELECT, INSERT, UPDATE, DELETE ON course_sql_demo_v00.* TO 'course_demo_v00_weak'@'localhost';
GRANT SELECT ON course_sql_demo_v00.products TO 'course_demo_v00_strong'@'localhost';
GRANT SELECT (user_id, username, email, role) ON course_sql_demo_v00.users TO 'course_demo_v00_strong'@'localhost';
GRANT SELECT (record_id, user_id, title, secret_value) ON course_sql_demo_v00.private_records TO 'course_demo_v00_strong'@'localhost';
