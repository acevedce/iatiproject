# Code Challenge

Has the company should get millons of request, my idea is to provide a docker ready to deploy on cloud or cluster to scalate.
I divided the source as:
controllers: where all the business logic is done (this is a 1st step), the idea is to split the database controller into a different utility source and comsume from api controllers and logic
resources: as we want to have micro features, the 1st one is the search feature, but maybe in the future we would like to have adding, searching, updating, deleting and cross referencing to other products of the company, add a new feature should be as simple as registering a blueprint
views: the definition of the endpoints and resources

OBS: this API POC has CORS activated just for debug and developing purposes DO NOT DEPLOY to PROD ENV



To achive this, the easier way to handle a POC is with a small database as PosgreSQL with a simple table (we can use another kind of DB as noSQL too, such as tinyDB)


CREATE TABLE products (
  products_id TEXT PRIMARY KEY,
  prod_name TEXT,
  price FLOAT,
  avail_items INT
);

CREATE TABLE reservation (
  products_id TEXT REFERENCES products (products_id) ON UPDATE CASCADE ON DELETE CASCADE,
  reservation_id TEXT,
  number_of_items INT
);

## Running the Service
The service will be delivered via Docker. Running the following command will 
start a PostgreSQL database, load sample data into it and start the Python 
service. 

In order to develop a better solution, I take the freedom to use a DB to handle data instead of a json file with the structure you can find at init-db.sql file


```
docker-compose up --build
```

You can connect to the database using the default user `postgres` with no password.

If you change data in your database in a significant way ```rm -rf ./pg_data && docker-compose up --build```



## How to test endpoints

Once the docker is up:

We can use a Swagger service running on port 10000
http://localhost:10000/


## How to test -> test

Get a docker list:

```
docker ps
```

Connect to the docker:

```
docker exec -it DOCKER_ID  /bin/bash
```


Navigate to:

```
cd /myapp/tests/flaskapp/api/resources
```


Run Tests:

```
pytest -vv -s
```