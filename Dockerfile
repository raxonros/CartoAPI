FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR  /carto_api
COPY requirements.txt /carto_api/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./carto_api /carto_api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]