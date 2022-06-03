load:
	docker build -t python-loader .
	docker run --rm --network container:mongodb -it python-loader

start:
	docker compose up -d

stop:
	docker compose down -v
