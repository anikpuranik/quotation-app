# Downloading Image
FROM postgres

# Displaying Ports
EXPOSE 5432

# Copying Files
COPY create_tables.sql  /docker-entrypoint-initdb.d/create_tables.sql
COPY categories.sql  /docker-entrypoint-initdb.d/categories.sql
COPY morning.sql  /docker-entrypoint-initdb.d/morning.sql
COPY onepiece_quotes.sql  /docker-entrypoint-initdb.d/onepiece_quotes.sql
COPY death_note_quotes.sql  /docker-entrypoint-initdb.d/death_note_quotes.sql

# Creating Tables
RUN chmod +x docker-entrypoint-initdb.d/create_tables.sql

# Adding data
RUN chmod +x docker-entrypoint-initdb.d/morning.sql
RUN chmod +x docker-entrypoint-initdb.d/categories.sql
RUN chmod +x docker-entrypoint-initdb.d/onepiece_quotes.sql
RUN chmod +x docker-entrypoint-initdb.d/death_note_quotes.sql