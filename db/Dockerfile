# Downloading Image
FROM postgres

# Displaying Ports
EXPOSE 5432

# Copying Files
COPY categories.sql  /docker-entrypoint-initdb.d/categories.sql
COPY morning.sql  /docker-entrypoint-initdb.d/morning.sql
COPY anime_quotes.sql  /docker-entrypoint-initdb.d/anime_quotes.sql
#COPY family_data.sql /docker-entrypoint-initdb.d/family_data.sql

# Creating Tables
RUN chmod +x docker-entrypoint-initdb.d/categories.sql
RUN chmod +x docker-entrypoint-initdb.d/morning.sql
RUN chmod +x docker-entrypoint-initdb.d/anime_quotes.sql

# Adding Data
#RUN chmod +x docker-entrypoint-initdb.d/family_data.sql