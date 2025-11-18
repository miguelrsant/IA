kill-ports:
	-lsof -t -i:3030 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:3000 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:8000 | xargs -r kill -9 2>/dev/null || true
	-lsof -t -i:5432 | xargs -r kill -9 2>/dev/null || true

	-docker stop $$(docker ps -q --filter "publish=3030") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=3000") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=8000") 2>/dev/null || true
	-docker stop $$(docker ps -q --filter "publish=5432") 2>/dev/null || true


# =====================================
# DEV MODE
# =====================================
dev: kill-ports
	cp .env.dev .env

	# Sobe o banco
	docker compose -f docker-compose.yml up -d --build db

	# Espera o Postgres responder antes das migrations
	@echo "⏳ Waiting for Postgres..."
	@sleep 4

	# Roda as migrations automaticamente
	@echo "📦 Running migrations..."
	cd backend && flask --app main.py db upgrade -d migrations

	# Inicia o backend
	@echo "🚀 Starting backend..."
	cd backend && pdm run gunicorn main:app -b 0.0.0.0:8000 &

	# Inicia o frontend
	@echo "🎨 Starting frontend..."
	cd frontend && npm run dev


# =====================================
# BUILD MODE (Produção)
# =====================================
build: kill-ports
	cp .env.build .env
	docker compose down --remove-orphans
	docker compose build --no-cache
	docker compose up -d

