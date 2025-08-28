# scripts/validate_structure.py
"""
Validates project structure against PROJECT_STRUCTURE.md
Run this before every commit
"""

import os
import sys

REQUIRED_STRUCTURE = {
    'infrastructure/docker': ['docker-compose.yml'],
    'infrastructure/kubernetes/base': ['namespace.yaml'],
    'infrastructure/kubernetes/configmaps': [],
    'infrastructure/kubernetes/deployments': [],
    'infrastructure/terraform': ['main.tf'],
    'services': [],
    'edge-server/config': ['edge-config.yaml'],
    'shared': [],
    'docs': ['PROJECT_CONTEXT.md', 'PROJECT_STRUCTURE.md'],
}

def validate_structure():
    errors = []
    for path, required_files in REQUIRED_STRUCTURE.items():
        if not os.path.exists(path):
            errors.append(f"Missing directory: {path}")
        else:
            for file in required_files:
                if not os.path.exists(os.path.join(path, file)):
                    errors.append(f"Missing file: {path}/{file}")
    
    if errors:
        print("❌ Structure validation failed:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✅ Structure validation passed")

if __name__ == "__main__":
    validate_structure()
