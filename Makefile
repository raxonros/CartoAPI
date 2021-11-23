start:
	docker-compose -f ./docker-compose.yml down
	docker build -t carto_docker .
	docker-compose -f ./docker-compose.yml up -d
	sleep 3
	docker exec -it carto_api python /carto_api/populate_database.py
