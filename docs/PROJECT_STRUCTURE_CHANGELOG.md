# PROJECT_STRUCTURE_CHANGELOG.md

## Version 1.3.0 - 29 Aug 2025
### Added

1. Frontend Applications ✅

Web app
Mobile app
Admin portal
Complete React/Vue structure

2. Message Schemas ✅

Kafka message definitions
Protobuf schemas
VideoJob structure

3. SDKs ✅

Python SDK for edge servers
JavaScript SDK for web
Mobile SDKs

4. Security & Certificates ✅

SSL/TLS certificates location
VPN configurations
Certificate management

5. Operations ✅

Backup/restore scripts
Monitoring dashboards
Runbooks

6. Load Balancer ✅

HAProxy configs
Nginx configs

7. Ansible ✅

Edge deployment automation

8. Data & Models ✅

ML model storage
Test data
Sample videos

9. Development Tools ✅

Code generators
Debug utilities
VS Code settings

10. Complete Testing ✅

Security testing
E2E with Cypress
Load testing

🎯 This Structure Now Covers:

Every file type has a home
Every component is placed
Every deployment scenario is covered
Every team member knows where things go

### Approved by: [Sharad]
### Date: 29 Aug 2025

## Version 1.2.0 - 28 Aug 2025
### Added
- api-gateway service as 16th microservice
- Central entry point for all UI requests
- Handles authentication, routing, aggregation
- WebSocket proxy for real-time features

### Rationale
- Single API endpoint for UI team
- Centralized cross-cutting concerns
- Better performance through aggregation
- Simplified frontend development

### Approved by: [Sharad]
### Date: 29 Aug 2025

## Version 1.1.0 - [28-Aug-2025] 
- Added: infrastructure/kubernetes/helm/
- Moved: helm charts from root to kubernetes/
- Reason: Better organization
- Approved by: [Sharad]

  
## Version 1.0.0 - [28-Aug-2025]
- Initial structure defined
- 15 services identified
- Infrastructure paths set



## RULE: Any structure change needs:
1. Version bump
2. Changelog entry
3. Update validation script
4. Team approval
