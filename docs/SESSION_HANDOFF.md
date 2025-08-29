# SESSION_HANDOFF.md

## Starting New Session Checklist:
1. ✅ Provide GitHub repo URL
2. ✅ State: "Use PROJECT_STRUCTURE.md as the ONLY source of truth for directories"
3. ✅ State: "Any file creation must match PROJECT_STRUCTURE.md exactly"
4. ✅ Current working directory: [specify exact path]
5. ✅ Files being modified: [list exact files]

## Example:
"Continue VMS project: https://github.com/softdew/vms-platform
Follow PROJECT_STRUCTURE.md STRICTLY for all paths.
Working on: /services/camera-service/
Creating: src/main.py, src/models.py, tests/test_camera.py"

-------------------------------------------------------------------------------------------------
# AI_INSTRUCTIONS.md

## STRICT RULES FOR AI ASSISTANT:

1. **NEVER create directories outside PROJECT_STRUCTURE.md**
2. **ALWAYS ask before creating new directories**
3. **If structure seems wrong, STOP and clarify**
4. **Use these EXACT paths:**
   - Configs: infrastructure/kubernetes/configmaps/
   - Deployments: infrastructure/kubernetes/deployments/
   - Docker: infrastructure/docker/
   - Services: services/{service-name}/
   
5. **When creating files, show full path:**
   ❌ "Create config.yaml"
   ✅ "Create infrastructure/kubernetes/configmaps/app-config.yaml"

-------------------------------------------------------------------------------------
   For EVERY new session, start with:
      
   "Continue VMS project: https://github.com/softdew/vms-platform
STRICT RULE: Follow docs/PROJECT_STRUCTURE.md exactly for all file paths.
Never create directories outside this structure.
Current task: [specify]"

   

7. **If confused about location, ASK don't ASSUME**

-----------------------------------------------------------------

"Continue VMS project: https://github.com/softdew/vms-platform
Using PROJECT_STRUCTURE.md v1.1.0 with 16 services including api-gateway.
Ready to implement [specify task]"

------------------------------------------------------------------------------------------------------


I'm building a VMS (Video Management System) platform with AI analytics. 

GitHub repo: https://github.com/softdew/vms-platform

Here are my two core documents:

[PASTE PROJECT_CONTEXT.md HERE - the complete requirements document]

[PASTE PROJECT_STRUCTURE.md v2.0.0 HERE - the final directory structure]

CRITICAL RULES:
1. Follow PROJECT_STRUCTURE.md v2.0.0 EXACTLY for all file locations
2. This structure is immutable - any deviation is a bug
3. We have 16 backend services + frontend apps + edge server components

I want to start with: [SPECIFY YOUR TASK]
- Option A: Design complete database schema (SQL Server + MongoDB)
- Option B: Implement api-gateway service
- Option C: Implement camera-service
- Option D: Create edge server ingestion pipeline
- Option E: [Your specific choice]

Please acknowledge you've understood the structure and requirements before we begin.

