# PROJECT_STRUCTURE.md - VMS Platform
**Version:** 1.0.0  
**Status:** IMMUTABLE - Any changes require version bump and approval  
**Last Updated:** December 2024

## 🔴 CRITICAL RULES
1. This file is the SINGLE SOURCE OF TRUTH for directory structure
2. ANY deviation from this structure is a BUG
3. AI assistants MUST follow this structure exactly
4. Changes require version bump in PROJECT_STRUCTURE_CHANGELOG.md

## 📁 Complete Directory Structure

```
vms-platform/
├── services/                           # Microservices
│   ├── auth-service/
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── main.py               # FastAPI app entry
│   │   │   ├── models.py             # Pydantic/SQLAlchemy models
│   │   │   ├── schemas.py            # Request/Response schemas
│   │   │   ├── routes.py             # API endpoints
│   │   │   ├── dependencies.py       # Shared dependencies
│   │   │   ├── config.py             # Service configuration
│   │   │   └── utils.py              # Helper functions
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_routes.py
│   │   │   ├── test_models.py
│   │   │   └── conftest.py
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── .env.example
│   │   └── README.md
│   │
│   ├── tenant-service/                # Customer & license management
│   │   └── [same structure as auth-service]
│   │
│   ├── camera-service/                # Camera CRUD, discovery, PTZ
│   │   └── [same structure as auth-service]
│   │
│   ├── edge-manager-service/          # Edge server orchestration
│   │   └── [same structure as auth-service]
│   │
│   ├── calculator-service/            # DIY cost calculator
│   │   └── [same structure as auth-service]
│   │
│   ├── ingestion-service/             # Video stream ingestion
│   │   └── [same structure as auth-service]
│   │
│   ├── streaming-service/             # WebRTC/HLS streaming
│   │   └── [same structure as auth-service]
│   │
│   ├── ai-pipeline-service/           # AI model orchestration
│   │   └── [same structure as auth-service]
│   │
│   ├── event-service/                 # Event processing
│   │   └── [same structure as auth-service]
│   │
│   ├── notification-service/          # Multi-channel alerts
│   │   └── [same structure as auth-service]
│   │
│   ├── ticketing-service/             # Ticket management
│   │   └── [same structure as auth-service]
│   │
│   ├── storage-service/               # Video storage management
│   │   └── [same structure as auth-service]
│   │
│   ├── watchdog-service/              # Health monitoring & SLA
│   │   └── [same structure as auth-service]
│   │
│   ├── config-service/                # Centralized configuration
│   │   └── [same structure as auth-service]
│   │
│   └── sync-service/                  # Edge-cloud synchronization
│       └── [same structure as auth-service]
│
├── edge-server/                        # Edge server components
│   ├── agent/
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   ├── sync_manager.py       # Config & license sync
│   │   │   ├── heartbeat.py          # Health reporting
│   │   │   └── cluster_manager.py    # Peer coordination
│   │   ├── tests/
│   │   └── requirements.txt
│   │
│   ├── ingestion/
│   │   ├── adapters/
│   │   │   ├── __init__.py
│   │   │   ├── base_adapter.py       # Abstract base class
│   │   │   ├── onvif_adapter.py      # ONVIF protocol
│   │   │   ├── rtsp_adapter.py       # RTSP streams
│   │   │   ├── hikvision_adapter.py  # Hikvision SDK
│   │   │   └── dahua_adapter.py      # Dahua SDK
│   │   ├── normalizer/
│   │   │   ├── __init__.py
│   │   │   ├── video_normalizer.py   # Resolution/FPS normalization
│   │   │   └── codec_converter.py    # Codec conversion
│   │   ├── segmenter/
│   │   │   ├── __init__.py
│   │   │   ├── stream_segmenter.py   # 5s chunks with overlap
│   │   │   └── segment_buffer.py     # Buffer management
│   │   ├── job_maker/
│   │   │   ├── __init__.py
│   │   │   ├── job_creator.py        # VideoJob creation
│   │   │   └── priority_router.py    # Route to correct queue
│   │   └── load_balancer/
│   │       ├── __init__.py
│   │       └── stream_distributor.py # Distribute across workers
│   │
│   ├── ai-workers/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── intrusion_detection.py
│   │   │   ├── fire_smoke_detection.py
│   │   │   ├── anpr.py
│   │   │   └── [other 7 models].py
│   │   ├── consumers/
│   │   │   ├── __init__.py
│   │   │   ├── base_consumer.py      # Base Kafka consumer
│   │   │   ├── priority_consumer.py  # High-priority queue
│   │   │   └── standard_consumer.py  # Standard queue
│   │   └── gpu_manager/
│   │       ├── __init__.py
│   │       ├── resource_allocator.py # GPU resource management
│   │       └── model_cache.py        # Model caching in GPU
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── video_buffer.py           # Local video buffering
│   │   ├── event_queue.py            # Event queue for upload
│   │   └── retention_manager.py      # Storage cleanup
│   │
│   └── config/
│       ├── edge-config.yaml          # Edge server configuration
│       └── models-config.yaml        # AI model configurations
│
├── shared/                            # Shared libraries
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # SQLAlchemy base
│   │   │   ├── customer.py          # Customer model
│   │   │   ├── camera.py            # Camera model
│   │   │   ├── user.py              # User model
│   │   │   ├── license.py           # License model
│   │   │   ├── edge_server.py       # Edge server model
│   │   │   └── event.py             # Event model
│   │   ├── mongodb/
│   │   │   ├── __init__.py
│   │   │   ├── schemas.py           # MongoDB schemas
│   │   │   └── connection.py        # MongoDB connection
│   │   └── migrations/
│   │       ├── alembic.ini
│   │       └── versions/
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── jwt_handler.py       # JWT utilities
│   │   │   ├── password.py          # Password hashing
│   │   │   └── permissions.py       # RBAC utilities
│   │   ├── video/
│   │   │   ├── __init__.py
│   │   │   ├── codec_utils.py       # Codec utilities
│   │   │   ├── frame_utils.py       # Frame processing
│   │   │   └── stream_utils.py      # Stream utilities
│   │   └── network/
│   │       ├── __init__.py
│   │       ├── diagnostics.py       # Network diagnostics
│   │       └── discovery.py         # Camera discovery
│   │
│   └── protocols/
│       ├── __init__.py
│       ├── onvif/
│       │   ├── __init__.py
│       │   ├── client.py            # ONVIF client
│       │   └── discovery.py         # ONVIF discovery
│       └── rtsp/
│           ├── __init__.py
│           └── client.py            # RTSP client
│
├── infrastructure/                    # Deployment & configuration
│   ├── docker/
│   │   ├── docker-compose.yml       # Full stack local dev
│   │   ├── docker-compose.dev.yml   # Development overrides
│   │   ├── docker-compose.test.yml  # Testing environment
│   │   ├── Dockerfile.base          # Base Python image
│   │   └── .env.example             # Environment template
│   │
│   ├── kubernetes/
│   │   ├── base/
│   │   │   ├── namespace.yaml       # Namespace definition
│   │   │   ├── rbac.yaml           # RBAC rules
│   │   │   └── network-policy.yaml  # Network policies
│   │   ├── configmaps/
│   │   │   ├── app-config.yaml     # Application config
│   │   │   ├── model-config.yaml   # AI model config
│   │   │   └── edge-config.yaml    # Edge server config
│   │   ├── secrets/
│   │   │   ├── .gitkeep            # Empty file for git
│   │   │   └── sealed-secrets.yaml  # Encrypted secrets
│   │   ├── deployments/
│   │   │   ├── auth-service.yaml
│   │   │   ├── tenant-service.yaml
│   │   │   ├── camera-service.yaml
│   │   │   └── [other services].yaml
│   │   ├── services/
│   │   │   ├── auth-service-svc.yaml
│   │   │   └── [other services]-svc.yaml
│   │   ├── ingress/
│   │   │   └── nginx-ingress.yaml
│   │   ├── istio/
│   │   │   ├── gateway.yaml
│   │   │   └── virtual-service.yaml
│   │   └── monitoring/
│   │       ├── prometheus.yaml
│   │       └── grafana.yaml
│   │
│   ├── helm/
│   │   └── vms-platform/
│   │       ├── Chart.yaml           # Helm chart definition
│   │       ├── values.yaml          # Default values
│   │       ├── values.dev.yaml      # Development values
│   │       ├── values.prod.yaml     # Production values
│   │       └── templates/
│   │           └── [all templates]
│   │
│   └── terraform/
│       ├── modules/
│       │   ├── eks/                # EKS cluster module
│       │   ├── rds/                # RDS module
│       │   ├── s3/                 # S3 module
│       │   └── vpc/                # VPC module
│       ├── environments/
│       │   ├── dev/
│       │   ├── staging/
│       │   └── prod/
│       ├── main.tf                  # Main configuration
│       ├── variables.tf             # Variable definitions
│       ├── outputs.tf               # Output values
│       └── backend.tf               # State backend config
│
├── tests/                             # Integration & E2E tests
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_camera_flow.py
│   │   ├── test_event_pipeline.py
│   │   └── test_edge_sync.py
│   ├── e2e/
│   │   ├── __init__.py
│   │   └── test_full_pipeline.py
│   ├── load/
│   │   ├── locustfile.py           # Load testing with Locust
│   │   └── scenarios/
│   └── simulators/
│       ├── camera_simulator.py      # Camera simulator
│       ├── onvif_simulator.py      # ONVIF simulator
│       └── hikvision_simulator.py  # Hikvision simulator
│
├── docs/                              # Documentation
│   ├── PROJECT_CONTEXT.md           # Complete requirements
│   ├── PROJECT_STRUCTURE.md         # THIS FILE
│   ├── PROJECT_STRUCTURE_CHANGELOG.md
│   ├── API_SPECIFICATION.md         # OpenAPI specs
│   ├── DATABASE_SCHEMA.md           # Database design
│   ├── DEPLOYMENT_GUIDE.md          # Deployment instructions
│   ├── DEVELOPMENT_GUIDE.md         # Dev setup guide
│   └── architecture/
│       ├── system_design.md
│       ├── data_flow.md
│       └── diagrams/
│
├── scripts/                           # Utility scripts
│   ├── setup/
│   │   ├── setup_dev.sh            # Development setup
│   │   ├── setup_edge.sh           # Edge server setup
│   │   └── install_deps.sh         # Install dependencies
│   ├── deployment/
│   │   ├── deploy.sh                # Deployment script
│   │   └── rollback.sh             # Rollback script
│   ├── database/
│   │   ├── init_db.py              # Initialize database
│   │   └── seed_data.py            # Seed test data
│   └── validation/
│       ├── validate_structure.py    # Validate this structure
│       └── validate_config.py       # Validate configurations
│
├── .github/                           # GitHub specific
│   ├── workflows/
│   │   ├── ci.yml                   # Continuous Integration
│   │   ├── cd.yml                   # Continuous Deployment
│   │   ├── security.yml             # Security scanning
│   │   └── validate-structure.yml   # Structure validation
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── requirements/                      # Python dependencies
│   ├── base.txt                     # Core dependencies
│   ├── dev.txt                      # Development dependencies
│   ├── test.txt                     # Testing dependencies
│   └── prod.txt                     # Production dependencies
│
├── .gitignore
├── .dockerignore
├── .env.example                      # Environment variables template
├── Makefile                          # Common commands
├── README.md                         # Project overview
├── LICENSE
└── pyproject.toml                    # Python project config
```

## 📌 Key Files That MUST Exist

### Root Level
- `PROJECT_CONTEXT.md` - Complete requirements (in docs/)
- `PROJECT_STRUCTURE.md` - This file (in docs/)
- `README.md` - Project overview
- `Makefile` - Common commands
- `.env.example` - Environment template

### Each Service Must Have
- `src/main.py` - Entry point
- `src/models.py` - Data models
- `src/routes.py` - API endpoints
- `src/config.py` - Configuration
- `Dockerfile` - Container definition
- `requirements.txt` - Dependencies
- `README.md` - Service documentation

### Infrastructure Must Have
- `docker-compose.yml` - Local development
- `kubernetes/base/namespace.yaml` - K8s namespace
- `terraform/main.tf` - Infrastructure as code

## 🚫 FORBIDDEN Actions

1. **NEVER** create directories outside this structure
2. **NEVER** place configs in service directories (use infrastructure/)
3. **NEVER** mix edge-server code with cloud services
4. **NEVER** put secrets in configmaps (use secrets/)
5. **NEVER** create new top-level directories without version bump

## ✅ Validation Command

Run this before EVERY commit:
```bash
python scripts/validation/validate_structure.py
```

## 📝 Change Process

To modify this structure:
1. Create PR with proposed changes
2. Update version in this file
3. Add entry to PROJECT_STRUCTURE_CHANGELOG.md
4. Get approval from tech lead
5. Update validation script
6. Merge and tag release

---
**This structure is LAW. Deviations are BUGS.**
