<!-- Workspace-specific Copilot instructions for blockchain-hospital-network -->

- [x] Create project structure
- [ ] Install Python dependencies
- [ ] Install Node dependencies  
- [ ] Configure environment variables
- [ ] Start Docker Compose stack
- [ ] Test API endpoints
- [ ] Implement Hyperledger Fabric integration
- [ ] Complete database migrations
- [ ] Add API authentication routes
- [ ] Implement patient record endpoints
- [ ] Complete React components
- [ ] Set up monitoring dashboards

## Project Overview

This is a production-ready hospital blockchain network using Hyperledger Fabric, FastAPI, React, PostgreSQL, Docker, and Kubernetes.

## Key Technologies

- Blockchain: Hyperledger Fabric
- Backend: Python FastAPI
- Frontend: React + Tailwind CSS
- Database: PostgreSQL
- Auth: JWT / OAuth 2.0
- Deployment: Docker + Kubernetes
- Monitoring: Prometheus + Grafana

## Quick Start

1. Navigate to project: `cd d:\blockchain-hospital-network`
2. Configure environments: `cp backend/.env.example backend/.env`
3. Start services: `docker-compose -f docker/docker-compose.yml up`
4. Access UI: http://localhost:3000

## Important Files

- `README.md` - Full documentation
- `docker/docker-compose.yml` - Local development setup
- `k8s/` - Kubernetes deployment files
- `backend/requirements.txt` - Python dependencies
- `frontend/package.json` - Node dependencies

## Development Guidelines

- Python: Follow PEP 8, use FastAPI patterns
- JavaScript: ESLint, use React hooks, Tailwind for styling
- Database: Use SQLAlchemy ORM, avoid raw SQL
- Blockchain: Use Fabric SDK for chaincode interaction
- Security: Always use JWT, validate inputs, use HTTPS
