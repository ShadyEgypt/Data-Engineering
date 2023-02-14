# Payroll Management System

Change directory into the challenge directory
```
cd <your-local-system>/Challenges/Payroll_Management_System
```

Run PostgreSQL DB with docker compose
```
docker-compose \
	-f db_docker_compose.yml \
	--project-name payroll_db \
	up -d
```
