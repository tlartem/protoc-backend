test:
	@docker info > /dev/null 2>&1 || (echo "Docker not running" && exit 1)
	@pytest --no-header

env:
	@if [ -f .env ]; then \
		echo "File .env already exists"; \
		exit 1; \
	fi
	@cp .env.example .env

up:
	docker compose up --build -d --force-recreate
	docker compose logs -f
down:
	docker compose down
clean:
	docker compose down 
	docker system prune -a --volumes -f
