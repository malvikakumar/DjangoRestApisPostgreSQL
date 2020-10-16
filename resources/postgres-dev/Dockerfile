FROM postgres:12.4
ENV POSTGRES_USER productsrole
ENV POSTGRES_PASSWORD 123Start
ENV POSTGRES_DB testdb
ADD sql/grantAccess.sql /docker-entrypoint-initdb.d/