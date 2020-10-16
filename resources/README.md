## Docker Images

Dockerfiles are located here to quickly setup and run local instances of PostgreSQL for dev testing.  To install Docker, go to https://www.docker.com/.  The following steps assume Docker is installed, configured and running.

### PostgreSQL

<b>To build the Docker image:</b>
<code>cd REPO_PATH/resources
docker build -t prod-db-test -f postgres-dev/Dockerfile .</code>

<b>To completely rebuild the image:</b>
<code>docker build --no-cache=true -t docpub-db-test -f postgres-dev/Dockerfile .</code>

<b>To run the Docker image:</b>
<code>docker run --rm -p 5432:5432 prod-db-test</code>

That's it.  You now are running PostgreSQL locally!  The database should already be configured
with the user (productsrole:123Start), and the database will be setup and ready for use.