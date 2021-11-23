# CartoAPI

Python API implementation (3.8) to obtain payments and coordinates in a specific area. The FastAPI Framework for python and a PostgreSQL database have been used.

## Previous requirements
To build this project on docker you need `docker` and  `docker-compose`.

## Funcionality

The following Endpoints have been implemented.

- This EP calculate total payment. Accept optional range date and postal code to calcualte result

```
@router.get("/payment/total",)
async def get_total():

```

- This EP calculate total payment for each postal code. Accept optional range date

```
@router.get("/payment/total/postal-codes")
async def get_total_by_postal_code():

```

- This EP calculate payment by age and gender. Accept optional range date and postal code

```
@router.get("/payment/{gender}/{age}",)
async def get_age_gender(gender, age):

```

## Things to improve
- The EP to get the WKB data has not been implemented.
- No login or auth mechanism has been implemented.
- A cache has not been implemented.
- No tests have been implemented

## Deploy with Docker
If you have docker and docker compose it is only necessary to execute the command `make start`. With this command the image of the docker api will be created, the containers will be raised and the database will be populated with the csv data.

## Local Deploy
If you only want to run the back in local env (without docker) you need `python 3.8` and install the different packages with the command `pip install -r requirements.txt`

You need to modify the config file and move it into the carto_api folder


