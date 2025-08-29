# PROJECT_STRUCTURE_CHANGELOG.md

## Version 1.2.0 - December 2024
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
