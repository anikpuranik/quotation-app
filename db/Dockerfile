# Downloading Image
FROM postgres

# Displaying Ports
EXPOSE 5432

# Copying Files
COPY categories.sql  /docker-entrypoint-initdb.d/categories.sql
COPY morning.sql  /docker-entrypoint-initdb.d/morning.sql
COPY onepiece.sql  /docker-entrypoint-initdb.d/onepiece.sql
#COPY family_data.sql /docker-entrypoint-initdb.d/family_data.sql

# Creating Tables
RUN chmod +x docker-entrypoint-initdb.d/categories.sql
RUN chmod +x docker-entrypoint-initdb.d/morning.sql
RUN chmod +x docker-entrypoint-initdb.d/onepiece.sql

# Adding Data
#RUN chmod +x docker-entrypoint-initdb.d/family_data.sql