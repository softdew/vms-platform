# PROJECT_STRUCTURE.md (IMMUTABLE - Version Controlled)

## RULE: This file is THE ONLY source of truth for directory structure
## Any deviation from this structure is a BUG, not a feature

vms-platform/
├── infrastructure/
│   ├── docker/
│   │   ├── docker-compose.yml
│   │   ├── docker-compose.dev.yml
│   │   └── docker-compose.prod.yml
│   ├── kubernetes/
│   │   ├── base/
│   │   │   ├── namespace.yaml
│   │   │   └── rbac.yaml
│   │   ├── configmaps/
│   │   │   ├── app-config.yaml
│   │   │   └── model-config.yaml
│   │   ├── secrets/
│   │   │   └── .gitkeep (actual secrets not in git)
│   │   ├── deployments/
│   │   │   ├── auth-service.yaml
│   │   │   ├── camera-service.yaml
│   │   │   └── [other-services].yaml
│   │   └── helm/
│   │       └── vms-platform/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── services/
│   ├── [service-name]/
│   │   ├── src/
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── README.md
│   └── [repeat for each service]
├── edge-server/
│   ├── config/
│   │   └── edge-config.yaml
│   └── [edge components]
├── shared/
│   └── [shared libraries]
├── docs/
│   ├── PROJECT_CONTEXT.md
│   ├── PROJECT_STRUCTURE.md  # THIS FILE
│   └── API_SPECIFICATION.md
└── scripts/
    └── validate_structure.py  # Script to verify structure
