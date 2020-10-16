## Django Rest Apis with PostgreSQL for ElectroPro App

### Installation Steps
#### Environment: Python3

 - To Install Postgres DB, follow [README.md](./resources/README.md)
 - To launch, follow the below commands:
    ```shell
    pip install -r requirements.txt  
    sh launch.sh
    ```

### Curl to register new users
```shell
curl --location --request POST 'http://localhost:8080/api/register' \
--form 'username=<user>' \
--form 'password=<password>' \
--form 'email=<email>'
```