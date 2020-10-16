DROP SCHEMA IF EXISTS testdb;
CREATE SCHEMA testdb;
SET search_path TO testdb;

GRANT USAGE
	ON SCHEMA testdb
	TO "productsrole";
