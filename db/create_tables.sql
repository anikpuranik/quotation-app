CREATE TABLE all_tables_details (
	Table_Name TEXT,
	Table_Level INT
);

CREATE TABLE morning_quotes (
	Quote TEXT
);
INSERT INTO all_tables_details (Table_Name, Table_Level) VALUES ('morning_quotes', 1);

CREATE TABLE anime_quotes (
	Series_Name TEXT,
	Character_Name TEXT,
	Quote TEXT
);
INSERT INTO all_tables_details (Table_Name, Table_Level) VALUES ('anime_quotes', 3);