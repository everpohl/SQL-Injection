USE course_sql_demo_v00;
-- Run under either account. Expected: Notebook.
SELECT name, price, description FROM products WHERE product_id = '1';
-- Weak query after interpolation. Run under the weak account. Expected: Maya's marker.
SELECT name, price, description FROM products WHERE product_id = '0' UNION ALL SELECT title, 0, secret_value FROM private_records WHERE record_id = 1 -- '
;
-- The same input, bound as data. Use an exact string comparison to avoid numeric coercion.
PREPARE lookup FROM 'SELECT name, price, description FROM products WHERE CAST(product_id AS CHAR) = ?';
SET @input = '0'' UNION ALL SELECT title, 0, secret_value FROM private_records WHERE record_id = 1 -- ';
EXECUTE lookup USING @input;
SET @input = '1';
EXECUTE lookup USING @input;
DEALLOCATE PREPARE lookup;
