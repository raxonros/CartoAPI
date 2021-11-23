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

When executing the `make start` command, an instance of the API on port 80 and an instance of Postgres on port 5432 are raised.

## Local Deploy
If you only want to run the back in local env (without docker) you need `python 3.8` and install the different packages with the command `pip install -r requirements.txt`

You need to modify the config file and move it into the carto_api folder

## Examples
These are some examples of the API calls that can be made.

Example Query
```
GET http://0.0.0.0:80/payment/F/<=24?postal_code=6055&date_init=2015-01-01&date_final=2015-01-02

```
Example result
```
{
    "age": "<=24",
    "gender": "F",
    "postal_code": 6055,
    "paid_amount": xxxx
}

```


Example Query
```
GET http://0.0.0.0:80/payment/F/2534?postal_code=6055&date_init=2015-01-01&date_final=2015-01-02

```
Example result
```
{
    "detail": "Incorrect format of gender or age"
}

```

Example Query
```
GET http://0.0.0.0:80/payment/total

```
Example result
```
{
    "total_payment": xxxx
}

```

Example Query
```
GET http://0.0.0.0:80/payment/total/postal-codes

```
Example result
```
[
    {
        "postal_code": 6070,
        "amount": 1189270.8405199999
    },
    {
        "postal_code": 6126,
        "amount": 3495925.1554300003
    },
    .
    .
    .

```



