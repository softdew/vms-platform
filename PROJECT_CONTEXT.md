# VMS Platform - Master Context Document
**Version:** 1.1  
**Last Updated:** December 2024  
**Git Repository:** https://github.com/softdew/vms-platform  
**Current Phase:** Requirements Finalized - Ready for Development

## 🚀 Code Generation Standards

### Documentation Requirements
```python
"""
Module: service_name
Purpose: Clear description
Dependencies: List all dependencies
Author: Developer name
Date: Creation date

Example:
    >>> from service import ClassName
    >>> instance = ClassName()
    >>> result = instance.method()
"""

class ExampleClass:
    """
    Class description.
    
    Attributes:
        attr1 (type): Description
        attr2 (type): Description
    
    Methods:
        method1: Brief description
        method2: Brief description
    """
    
    def method_name(self, param1: str, param2: int) -> dict:
        """
        Method description.
        
        Args:
            param1: Parameter description
            param2: Parameter description
            
        Returns:
            Description of return value
            
        Raises:
            ExceptionType: When this occurs
            
        Example:
            >>> result = instance.method_name("test", 123)
            >>> print(result)
            {'status': 'success'}
        """
        # Implementation with inline comments for complex logic
        pass
```

### API Documentation
- All endpoints must have OpenAPI decorators
- Request/response models with Pydantic
- Auto-generated Swagger UI at /docs
- Versioned APIs (/api/v1/, /api/v2/)

### Logging Standards
```python
import logging

logger = logging.getLogger(__name__)

# Use structured logging
logger.info("Processing segment", extra={
    "camera_id": camera_id,
    "segment_id": segment_id,
    "duration": duration
})
```

---

## 🎯 Project Overview

**Project Name:** Enterprise Video Management System with AI Analytics  
**Type:** Multi-tenant SaaS Platform  
**Architecture:** Microservices with Edge Computing  
**Deployment Model:** Hybrid (Cloud + On-Premise Edge Servers)

### Tech Stack (Finalized)
- **Backend Framework:** FastAPI (Python)
- **Databases:** 
  - SQL Server (Transactional data - customers, cameras, users, licenses)
  - MongoDB (Audit logs, event metadata, configuration history)
  - Redis (Caching, session management)
- **Message Queue:** Apache Kafka
- **Video Processing:** OpenCV + FFmpeg + GStreamer
- **Authentication:** JWT Tokens
- **Container Orchestration:** Docker/Kubernetes
- **ORM:** SQLAlchemy
- **Real-time Communication:** WebSocket/SignalR for events
- **Video Streaming:** WebRTC (default) + HLS/DASH fallback

---

## 📋 Finalized Requirements

### 1. Customer & License Management

**License Model**
- **Camera limits:** Customer-specific, defined in license
- **License validity:** Time-based expiration
- **AI Model licensing:** Customer purchases specific AI models from list of 10
- **Multi-tenant:** Single software instance serving multiple customers
- **No reseller model:** Flat customer structure

**User Hierarchy**
- Customer → Multiple Users
- **Roles:** Admin, Supervisor, Viewer (RBAC)
- **MFA Support:** Yes, required for all users
- **SSO Integration:** Phase 2 (future)

### 2. Camera Management

**Camera Discovery & Addition**
- **Automatic discovery:** IP range scanning + ONVIF discovery
- **Manual addition:** Supported via RTSP URL or SDK
- **Bulk import:** CSV/Excel upload supported (nice to have)

**Authentication Methods**
- Basic (username/password)
- Token-based authentication
- Certificate-based authentication
- Manufacturer-specific SDK authentication

**Camera Organization**
- **Nested hierarchy:** Building → Floor → Zone → Camera
- **Sites:** Multiple sites per customer
- **Grouping:** Flexible tagging and grouping

**PTZ Features**
- Manual control (pan/tilt/zoom)
- Presets management
- Tours/patterns
- Auto-tracking integration with AI events

**ONVIF Support**
- Profile S (Streaming)
- Profile G (Recording)
- Profile T (Advanced streaming)
- Profile A (Access control integration)

### 3. Network & Connectivity

**DDNS Support**
- No-IP
- Dynu
- DuckDNS
- Cloudflare
- Custom providers (configurable hostname/URL)

**NAT Traversal**
- Basic port forwarding configuration
- STUN/TURN server support for complex scenarios
- UPnP support

**Network Diagnostics**
- Bandwidth testing per camera
- Latency monitoring
- Connectivity health checks
- Stream quality monitoring
- Packet loss detection

### 4. Storage Architecture

**Storage Hierarchy & Priority**
1. Primary: RTSP stream (default)
2. Fallback 1: SD card
3. Fallback 2: Cloud storage
4. Note: NVR typically excludes cloud storage

**Recording Modes**
- Continuous recording
- Motion-triggered recording
- Event-based recording
- Schedule-based recording

**Retention Policies**
- System default settings
- Customer-level override capability
- Camera-level override capability
- Event-type specific retention periods

**Edge Server Storage**
- Local video buffering
- Configurable retention (system setting, customer override)
- Automatic cleanup based on storage threshold

### 5. Video Processing

**Supported Codecs**
- H.264 (mandatory)
- H.265/HEVC (mandatory)
- MJPEG (mandatory)
- Manufacturer-specific formats (plugin-based)

**Streaming Capabilities**
- WebRTC for low-latency live viewing (default)
- HLS/DASH for compatibility fallback
- Adaptive bitrate streaming based on bandwidth
- Multi-stream support (main + sub streams)

### 6. Video Processing Pipeline

**Stream Normalization**
- **Decoding:** Support for H.264, H.265, MJPEG streams
- **Standardized Output:** 
  - Resolution: 640x480 (configurable)
  - Color space: RGB
  - Frame rate: 15 fps (configurable)
- **Aspect Ratio Handling:** Letterboxing/cropping without distortion
- **Timestamp Synchronization:** NTP-synchronized timestamps on each frame
- **Target Latency:** < 500ms from camera to AI pipeline

**Stream Segmentation & Job Structure**
- **Time-Based Segmentation:** 
  - Default: 5-second segments (configurable)
  - Overlap: Configurable globally and per-model
- **Model Requirements Validation:**
  - Each model specifies: min_resolution, min_bitrate, min_duration, required_overlap
  - Validation at camera configuration time (incompatible models disabled)
  - Runtime warnings if camera settings degraded after configuration
- **VideoJob Object Structure:**
  ```
  {
    jobId: UUID
    customerId: UUID
    cameraId: UUID
    segmentSequence: Number
    timestamp: UTC Timestamp
    videoSegment: Byte Array
    metadata: {
      resolution: string
      bitrate: number
      duration: seconds
      frameCount: number
      enabledModels: array
      priority: HIGH|MEDIUM|STANDARD
      sourceQuality: {
        resolution: string
        bitrate: number
        fps: number
        codec: string
      }
    }
  }
  ```

**Kafka Queue Architecture**
- **Priority-Based Topics:**
  - `video-jobs-critical`: Configurable critical models
  - `video-jobs-high`: High priority models  
  - `video-jobs-standard`: Standard priority models
- **Partition Strategy:** cameraId as partition key for ordered processing
- **Fan-out Pattern:** Multiple consumer groups for same segment
- **Reliability:** Message durability with offset management

### 7. AI Analytics

**AI Models (10 Total)**
Each model has configurable priority and requirements:

| Model | Default Priority | Min Resolution | Min Bitrate | Min Duration | Overlap |
|-------|-----------------|----------------|-------------|--------------|---------|
| 1. Intrusion Detection | MEDIUM | 480p | 1 Mbps | 3s | 1s |
| 2. Advanced Motion Detection | STANDARD | 360p | 512 Kbps | 2s | 0.5s |
| 3. Camera Tampering | HIGH | 360p | 512 Kbps | 2s | 0s |
| 4. Fire & Smoke Detection | CRITICAL | 720p | 2 Mbps | 5s | 2s |
| 5. Crowd Detection | MEDIUM | 720p | 2 Mbps | 5s | 1s |
| 6. Missing Object Detection | STANDARD | 480p | 1 Mbps | 10s | 2s |
| 7. Abnormal Behavior | HIGH | 720p | 2 Mbps | 5s | 1s |
| 8. Fallen Detection | HIGH | 480p | 1 Mbps | 3s | 1s |
| 9. Tailgating | MEDIUM | 720p | 2 Mbps | 3s | 1s |
| 10. ANPR | MEDIUM | 1080p | 3 Mbps | 2s | 0.5s |

**AI Consumer Architecture**
- **Dedicated Microservice per Model:** 
  - Independent scaling and deployment
  - Isolated failure domains
  - Model-specific optimization
- **Parallel Processing:**
  - Thread pools for concurrent segment processing
  - Configurable pool size based on hardware
- **GPU Resource Management:**
  - **Dynamic + Priority-based allocation**
  - **GPU Sharing:** Multiple consumers share GPU resources
  - **Model Caching:** Keep frequently used models in GPU memory
  - **Batch Processing:** For non-critical models to improve efficiency
  - **Priority Queue:** Critical models get GPU priority

**Event Processing Pipeline**
- **Confidence Threshold Filtering:** 
  - Per-model configurable thresholds
  - System default with customer/camera overrides
- **Event Correlation:** 
  - Cross-segment correlation for continuous events
  - Cross-camera correlation for zone transitions
  - Deduplication within time windows
- **False Positive Reduction:**
  - Post-processing heuristics
  - Minimum duration requirements
  - Object persistence validation
- **Event Generation Structure:**
  ```
  {
    eventId: UUID
    customerId: UUID
    cameraId: UUID
    eventType: enum
    confidence: float (0.0-1.0)
    timestamp: UTC
    detectionMetadata: {
      boundingBox: coordinates
      objectClass: string
      trackingId: UUID (for correlation)
    }
    clipUrl: string (20s clip: 10s pre + 10s post)
    priority: CRITICAL|HIGH|MEDIUM|STANDARD
    status: NEW|ACKNOWLEDGED|RESOLVED|FALSE_POSITIVE
  }
  ```

**Event Management Features**
- **User Actions:**
  - Acknowledge event
  - Export clip (MP4)
  - Tag/categorize (False Alarm, Critical, etc.)
  - Add notes/comments
  - Escalate to ticket
- **Event Storage:**
  - Local buffer on edge before cloud upload
  - Event queue for reliable delivery
  - Cloud storage with CDN for clips

### 7. Multi-Tenancy & Scaling

**Database Design**
- Shared tables with tenant_id (row-level security)
- Tenant isolation at application layer
- Separate storage buckets per tenant

**Edge Server Architecture**
- **Large customers:** Dedicated on-premise edge servers
- **Small customers (1-2 cameras):** Cloud-based processing
- **One edge server** serves single customer
- **Multiple edge servers** per customer supported (clustering)

**Scalability Targets**
- Hundreds of customers
- 500+ cameras per customer
- 24x7 concurrent streams
- Cluster support for load distribution

**Example Use Case**
- 580 TNG sites + 110 MSC sites
- ~6k cameras total
  - 2.6k new cameras (immediate)
  - 3.4k EOL cameras to replace (1-2 years)
  - 1.8k existing to integrate

### 7. Notifications & Integrations

**Notification Channels**
- Push notifications (mobile app)
- SMS
- WhatsApp
- Email

**Ticketing System**
- Custom ticketing module (default)
- ServiceNow integration (configurable)
- Jira integration (configurable)
- Auto-generated tickets for AI events
- Manual ticket creation supported

**Additional Integrations**
- Access control systems
- Alarm systems with acknowledgment
- Third-party VMS integration
- Webhook support for custom integrations

### 8. Configuration & Cache Management

**Hierarchical Configuration System**
Configuration priority (lowest to highest):
1. **System Defaults:** Global baseline settings
2. **Customer-Level:** Account-wide overrides
3. **Site-Level:** Location-specific settings
4. **Camera-Level:** Individual camera overrides

**Cache Strategy**
- **Technology:** Redis with configurable TTL
- **Default TTL:** 5 minutes for configuration cache
- **Cache Keys Structure:**
  - `config:system:*` - System defaults
  - `config:customer:{id}:*` - Customer settings
  - `config:camera:{id}:*` - Camera settings
  - `config:model:{id}:requirements` - Model requirements
- **Cache Invalidation:**
  - TTL-based expiration
  - Manual refresh button in UI
  - Automatic invalidation on configuration changes
  - Background refresh before TTL expiry for critical configs

**Configurable Parameters**
- **AI Model Settings:**
  - Priority level (CRITICAL|HIGH|MEDIUM|STANDARD)
  - Confidence thresholds
  - Model-specific parameters
  - Resource requirements (min resolution, bitrate, duration, overlap)
- **Video Processing:**
  - Segment size (1-10 seconds)
  - Overlap duration (0-5 seconds)
  - Normalization params
  - Buffer sizes
- **Notification Preferences:**
  - Channels per event type
  - Escalation rules
  - Quiet hours

**Change Management**
- Immutable audit log in MongoDB
- Track: who, when, what, old value, new value
- Configuration versioning
- Rollback capability

### 9. Service Level Management

**SLA Definitions**
- **High-Priority Models** (Fire/Smoke, Abnormal Behavior):
  - Response time: < 500ms
  - Availability: 99.9%
- **Standard Models:**
  - Response time: < 2000ms
  - Availability: 99.5%

**Performance Metrics**
- Response time per model
- Throughput (segments/minute)
- Accuracy metrics (true/false positive rates)
- Queue depth monitoring
- Consumer lag tracking

**Watchdog Service**
- **Performance Monitoring:** Real-time SLA tracking
- **Anomaly Detection:** Deviation from baseline performance
- **Alert Generation:** 
  - SLA breaches
  - Service failures
  - Resource exhaustion
- **Automated Remediation:**
  - Service restart on failure
  - Load rebalancing
  - Fallback activation

**Incident Management**
- Comprehensive incident logging:
  ```
  {
    incidentId: UUID
    timestamp: UTC
    customerId: UUID
    cameraId: UUID
    aiModel: string
    incidentType: LATENCY_BREACH|THROUGHPUT_DROP|SERVICE_FAILURE
    actualValue: number
    thresholdValue: number
    severity: CRITICAL|HIGH|MEDIUM|LOW
  }
  ```
- Dashboard integration for real-time monitoring
- Historical reporting and trend analysis

### 10. Monitoring, Statistics & Health

**System Monitoring**
- **Health Checks:**
  - Service heartbeat (every 30s)
  - Camera stream status
  - Edge server connectivity
  - Database connections
  - Queue depth monitoring
- **Performance Statistics:**
  - Real-time metrics dashboard
  - Historical trending
  - Per-model processing stats
  - Per-camera statistics

**Metrics Collection**
- **Prometheus Metrics:**
  - Request rates, latencies
  - Error rates by service
  - GPU utilization
  - Memory/CPU usage
  - Queue depths and consumer lag
- **Custom Business Metrics:**
  - Events per hour/day
  - False positive rates
  - Model accuracy trends
  - Customer usage patterns

**Statistics API**
```python
# Easy access to statistics via dedicated endpoints
GET /api/v1/statistics/system
GET /api/v1/statistics/customer/{id}
GET /api/v1/statistics/camera/{id}
GET /api/v1/statistics/model/{name}
GET /api/v1/statistics/events
```

**Health Monitoring Endpoints**
```python
# Standard health check endpoints for each service
GET /health           # Basic health
GET /health/ready    # Readiness probe
GET /health/live     # Liveness probe
GET /health/detailed # Detailed component status
```

**Watchdog Service Features**
- Performance monitoring against SLAs
- Anomaly detection
- Alert generation
- Automated remediation
- Incident logging

### 13. API & Authentication

**API Architecture**
- RESTful APIs for CRUD operations
- WebSocket/SignalR for real-time events
- GraphQL consideration for complex queries (Phase 2)

**Authentication & Security**
- JWT token-based authentication
- Refresh token mechanism
- API rate limiting
- IP whitelisting option
- Encryption for sensitive data

---

## 🏗️ Project Structure

```
vms-platform/
├── services/
│   ├── auth-service/           # JWT auth, user management, MFA
│   ├── tenant-service/         # Customer & license management
│   ├── camera-service/         # Camera CRUD, discovery, PTZ control
│   ├── edge-manager-service/   # Edge server orchestration & assignment
│   ├── calculator-service/     # DIY cost & resource calculator
│   ├── ingestion-service/      # Multi-source video ingestion
│   ├── streaming-service/      # WebRTC/HLS streaming
│   ├── ai-pipeline-service/    # Kafka consumer, AI model orchestration
│   ├── event-service/          # Event processing & correlation
│   ├── notification-service/   # Multi-channel alerts
│   ├── ticketing-service/      # Ticket management & integration
│   ├── storage-service/        # Video storage & retention
│   ├── watchdog-service/       # Health monitoring & SLA
│   ├── config-service/         # Centralized configuration
│   └── sync-service/           # Edge-cloud synchronization
│
├── shared/
│   ├── database/
│   │   ├── models/            # SQLAlchemy models
│   │   ├── mongodb/           # MongoDB schemas
│   │   └── migrations/        # Alembic migrations
│   ├── utils/
│   │   ├── auth/             # JWT utilities
│   │   ├── video/            # Video processing utilities
│   │   └── network/          # Network diagnostics
│   └── protocols/
│       ├── onvif/            # ONVIF implementation
│       └── rtsp/             # RTSP client
│
├── edge-server/
│   ├── agent/                # Edge-cloud communication & sync
│   │   ├── sync_manager/     # Config & license sync
│   │   ├── heartbeat/        # Health reporting
│   │   └── cluster_manager/  # Peer coordination
│   ├── ingestion/
│   │   ├── adapters/         # Camera adapters (RTSP, ONVIF, SDK)
│   │   ├── normalizer/       # Stream normalization (resolution, fps, codec)
│   │   ├── segmenter/        # Stream segmentation (5s chunks with overlap)
│   │   ├── job_maker/        # VideoJob creation and routing
│   │   └── load_balancer/    # Distribute streams across workers
│   ├── ai-workers/
│   │   ├── models/           # AI model implementations
│   │   ├── consumers/        # Kafka consumers (priority-based)
│   │   └── gpu_manager/      # GPU resource optimization
│   └── storage/              # Local video buffer & event queue
│
├── infrastructure/
│   ├── docker/
│   │   ├── Dockerfile.service
│   │   └── docker-compose.yml
│   ├── kubernetes/
│   │   ├── deployments/
│   │   ├── services/
│   │   └── configmaps/
│   └── terraform/            # Infrastructure as Code
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── simulators/           # ONVIF camera simulators
│
├── docs/
│   ├── api/                  # OpenAPI/Swagger docs
│   ├── architecture/
│   └── deployment/
│
├── scripts/
│   ├── setup/
│   └── migration/
│
├── requirements/
│   ├── base.txt              # Core dependencies
│   ├── dev.txt               # Development dependencies
│   └── prod.txt              # Production dependencies
│
├── .github/
│   └── workflows/            # CI/CD pipelines
│
├── PROJECT_CONTEXT.md         # This document
├── README.md
├── .env.example
└── .gitignore
```

---

## 📝 Development Phases

### Phase 1: Foundation (Current - Week 1-2)
- [x] Finalize requirements
- [ ] Design complete database schema
- [ ] Set up project structure
- [ ] Create base models for:
  - [ ] Tenant management
  - [ ] Camera management
  - [ ] User management
  - [ ] License management

### Phase 2: Video Pipeline (Week 3-4)
- [ ] Video ingestion adapter layer
  - [ ] RTSP client
  - [ ] ONVIF discovery & client
  - [ ] Stream normalization
- [ ] Storage service
- [ ] Basic streaming service (WebRTC)

### Phase 3: Core Services (Week 5-6)
- [ ] Authentication service (JWT)
- [ ] Configuration service
- [ ] Watchdog service
- [ ] RESTful APIs for all services

### Phase 4: AI Integration (Week 7-8)
- [ ] Kafka setup
- [ ] AI pipeline service
- [ ] Event service
- [ ] Event correlation logic

### Phase 5: Notifications & UI Support (Week 9-10)
- [ ] Notification service
- [ ] Ticketing service
- [ ] WebSocket/SignalR implementation
- [ ] Dashboard APIs

### Phase 6: Testing & Deployment (Week 11-12)
- [ ] Integration testing
- [ ] Performance testing
- [ ] Docker containerization
- [ ] Kubernetes deployment scripts

---

## 🔑 Key Design Decisions

1. **Multi-Database Strategy:** SQL Server for transactional, MongoDB for logs/events, Redis for cache
2. **Row-Level Security:** Shared tables with tenant_id for multi-tenancy
3. **Hybrid Deployment:** Cloud for small customers, on-premise edge for enterprise
4. **WebRTC First:** Low-latency streaming with HLS fallback
5. **Microservices:** FastAPI-based independent services
6. **Event-Driven:** Kafka for AI pipeline, WebSocket for real-time updates

---

## 🚀 Quick Start Commands

```bash
# Clone repository
git clone https://github.com/softdew/vms-platform.git
cd vms-platform

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies (after we create requirements.txt)
pip install -r requirements/base.txt

# Set up databases
docker-compose up -d sqlserver mongodb redis kafka

# Run database migrations (after we create them)
alembic upgrade head

# Start a service (example)
cd services/camera-service
uvicorn main:app --reload --port 8001
```

---

## 📌 Environment Variables

```env
# Database
SQLSERVER_HOST=localhost
SQLSERVER_PORT=1433
SQLSERVER_DB=vms_platform
SQLSERVER_USER=sa
SQLSERVER_PASSWORD=YourStrong!Password

MONGODB_URL=mongodb://localhost:27017/vms_logs

REDIS_URL=redis://localhost:6379/0

# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# JWT
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Services
AUTH_SERVICE_URL=http://localhost:8000
CAMERA_SERVICE_URL=http://localhost:8001

# Storage
VIDEO_STORAGE_PATH=/var/vms/videos
```

---

## 📅 Testing Environment & Tools

**Simulators**
- **ONVIF Simulator:** For initial development
- **Hikvision Simulator:** 
  - Support multiple concurrent instances
  - Configurable streams (resolution, fps, codec)
  - Event simulation capability
  - PTZ control simulation
- **Load Testing:**
  - Simulate 100+ camera streams
  - Variable network conditions
  - Event generation patterns

**Development Tools**
- **API Documentation:**
  - OpenAPI/Swagger auto-generation from code
  - Inline docstrings for all methods
  - Type hints for all parameters
  - Example requests/responses
- **Code Standards:**
  - Comprehensive inline comments
  - Docstring format: Google style
  - Type annotations throughout
  - Linting: Black, Flake8, MyPy

**Testing Strategy**
- Unit tests with pytest
- Integration tests for each service
- End-to-end testing with simulators
- Load testing with Locust
- GPU performance profiling

---

## 📞 Next Session Handoff

When starting a new session, share:
1. This document URL: `https://github.com/softdew/vms-platform/blob/main/PROJECT_CONTEXT.md`
2. Current task: "Continue with [SPECIFIC_MODULE]"
3. Last completed section
4. Any blocking issues

---

## 📝 Notes

- Start with customer management, camera management, and video ingestion (Phase 1)
- Edge server specs will vary based on camera count and AI models
- Consider GPU requirements: NVIDIA GPU for AI processing
- All settings have system defaults with customer override capability

---

**Version History:**
- v1.0: Initial requirements gathering
- v1.1: Complete requirements finalized with all answers

---

**Status:** Ready to begin Phase 1 development