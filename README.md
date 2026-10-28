# Hospital Blockchain Network

A secure, production-ready hospital records management system using **Hyperledger Fabric** blockchain technology.

## Tech Stack

- **Blockchain**: Hyperledger Fabric
- **Backend**: Python FastAPI
- **Frontend**: React with Tailwind CSS
- **Database**: PostgreSQL
- **Authentication**: JWT / OAuth 2.0
- **Security**: HTTPS / TLS
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud**: AWS
- **Monitoring**: Prometheus + Grafana

## Project Structure

```
blockchain-hospital-network/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application entry
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── security.py         # JWT authentication
│   ├── database.py         # Database configuration
│   ├── fabric_connector.py # Fabric blockchain integration
│   ├── config.py           # Application settings
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables template
│
├── frontend/                # React frontend
│   ├── src/
│   │   ├── App.jsx         # Main component
│   │   ├── index.jsx       # React entry point
│   │   └── index.css       # Global styles
│   ├── public/
│   │   └── index.html      # HTML template
│   ├── package.json        # Node dependencies
│   ├── tailwind.config.js  # Tailwind configuration
│   └── postcss.config.js   # PostCSS configuration
│
├── fabric/                  # Hyperledger Fabric
│   ├── docker-compose.yml  # Fabric network setup
│   └── README.md           # Fabric documentation
│
├── docker/                  # Docker configuration
│   ├── Dockerfile.backend  # Backend container
│   ├── Dockerfile.frontend # Frontend container
│   ├── docker-compose.yml  # Local development
│   └── prometheus.yml      # Prometheus config
│
├── k8s/                     # Kubernetes manifests
│   ├── configmap.yml       # Application config
│   ├── secret.yml          # Secrets management
│   ├── postgres.yml        # Database deployment
│   ├── backend.yml         # API deployment
│   ├── frontend.yml        # UI deployment
│   ├── prometheus.yml      # Monitoring
│   └── grafana.yml         # Dashboards
│
└── README.md               # This file
```

## Quick Start (Local Development)

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- PostgreSQL 15+

### 1. Clone and Setup

```bash
cd d:\blockchain-hospital-network
```

### 2. Configure Environment

```bash
# Backend
cp backend/.env.example backend/.env

# Update backend/.env with your settings
```

### 3. Start Local Stack with Docker

```bash
cd docker
docker-compose up -d
```

Services will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3001 (user: admin, password: admin)

### 4. Initialize Database

```bash
# Run migrations (to be implemented)
python backend/main.py
```

## API Endpoints

### Authentication
- `POST /token` - Login and get JWT token
- `POST /users` - Register new user

### Patient Records
- `POST /records/new` - Add patient record
- `GET /records/search` - Search records
- `GET /chain` - View full blockchain

### Health
- `GET /health` - Health check
- `GET /` - API status

## Security Features

- JWT token-based authentication
- Role-based access control (RBAC)
- TLS/HTTPS encryption
- SQL injection prevention via SQLAlchemy ORM
- CORS middleware configuration
- Audit logging for all actions
- Hyperledger Fabric network security

## Deployment

### Local Development
```bash
docker-compose -f docker/docker-compose.yml up
```

### Kubernetes Deployment
```bash
# Apply configurations
kubectl apply -f k8s/configmap.yml
kubectl apply -f k8s/secret.yml
kubectl apply -f k8s/postgres.yml
kubectl apply -f k8s/backend.yml
kubectl apply -f k8s/frontend.yml
kubectl apply -f k8s/prometheus.yml
kubectl apply -f k8s/grafana.yml

# Check deployments
kubectl get deployments
kubectl get services
```

### AWS Deployment
1. Set up AWS credentials in `.env`
2. Use AWS ECS for container orchestration
3. Use RDS for PostgreSQL database
4. Use Elastic Load Balancer for traffic distribution
5. Use CloudWatch for monitoring

## Monitoring

### Prometheus
- Access: http://localhost:9090
- Scrapes metrics from all services
- Retention: 15 days by default

### Grafana
- Access: http://localhost:3001
- Displays dashboards and alerts
- Connected to Prometheus data source

## Development

### Backend Development

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

### Frontend Development

```bash
cd frontend
npm install
npm start
```

## Features (Completed)

- [x] FastAPI backend scaffolding
- [x] React frontend with authentication UI
- [x] PostgreSQL database models
- [x] JWT authentication setup
- [x] Docker containerization
- [x] Kubernetes manifests
- [x] Monitoring with Prometheus/Grafana
- [x] Hyperledger Fabric integration structure

## Features (To Be Implemented)

- [ ] Complete Hyperledger Fabric network setup
- [ ] Chaincode (Smart Contracts) implementation
- [ ] Patient record CRUD operations via Fabric
- [ ] Advanced search and filtering
- [ ] Audit trail and compliance reporting
- [ ] Multi-hospital support with permissions
- [ ] Integration tests
- [ ] Performance optimization
- [ ] Production hardening

## Security Considerations

1. **Credentials Management**: Use AWS Secrets Manager or HashiCorp Vault
2. **Network Security**: Use VPC, security groups, and network policies
3. **Database**: Enable encryption at rest and in transit
4. **API**: Implement rate limiting and DDoS protection
5. **Monitoring**: Enable CloudWatch and CloudTrail logging
6. **Compliance**: Implement HIPAA-compliant audit logging

## Troubleshooting

### Database Connection Issues
```bash
# Check PostgreSQL container
docker logs hospital-postgres

# Reset database
docker volume rm docker_postgres_data
```

### Backend API Not Responding
```bash
# Check backend logs
docker logs hospital-backend

# Verify database URL in .env
```

### Frontend Build Issues
```bash
# Clear node_modules and reinstall
rm -rf frontend/node_modules
cd frontend
npm install
npm start
```

## Contributing

1. Create feature branches from `main`
2. Follow PEP 8 for Python code
3. Follow ESLint rules for JavaScript
4. Add tests for new features
5. Update documentation

## License

Proprietary - Hospital Blockchain Network

## Support

For issues and questions, contact the development team.

## Roadmap

- Q2 2024: MVP with Fabric integration
- Q3 2024: Multi-hospital support
- Q4 2024: Mobile app release
- Q1 2025: AI-powered analytics
