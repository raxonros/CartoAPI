from fastapi import FastAPI
from routes import payment, geometries

import uvicorn

app = FastAPI(
    title="Users API",
    description="a REST API using python and postgreSQL",
    version="0.0.1",
)


app.include_router(payment.router)
app.include_router(geometries.router)

if __name__ == '__main__':
    uvicorn.run(app)
