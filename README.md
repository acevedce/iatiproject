# Code Challenge

Has the company should get millons of request, my idea is to provide a docker ready to deploy on cloud or cluster to scalate.
I divided the source as:
views: where all the business logic is done (this is a 1st step), the idea is to split the database controller into a different utility source and comsume from api controllers and logic
models: as we want to have micro features, the 1st one is the search feature, but maybe in the future we would like to have adding, searching, updating, deleting and cross referencing to other products of the company, add a new feature should be as simple as registering a blueprint
urls: the definition of the endpoints and resources

OBS: this API POC has CORS de-activated just for debug and developing purposes DO NOT DEPLOY to PROD ENV



To achive this, the easier way to handle a POC is with a small database as MySQL with a simple table (we can use another kind of DB as noSQL too, such as tinyDB)

Please check th ER-Diagram file: 

```
projectERDiagram.png
```



## Running the Service
The service will be delivered via Docker. Running the following command will 
start a PostgreSQL database, load sample data into it and start the Python 
service. 

In order to develop a better solution, I take the freedom to use a DB to handle data instead of a json file with the structure you can find at init-db.sql file


```
docker-compose up --build
```

You can populate the database using the default manage loaddata from django.

Get a docker list:

```
docker ps
```

Connect to the docker__web:

```
docker exec -it DOCKER_ID  /bin/bash
```

Load data

```
python manage.py loaddata /shop/fixture/shop.json
```






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
apps = ["shop","orders"]

cd /{apps}
```


Run Tests:

```
pytest -vv -s
```