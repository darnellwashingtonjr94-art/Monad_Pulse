import os
import sys

def verify_all():
    required_files = ["docker-compose.yml", ".env.example", "README.md"]
    for f in required_files:
        if not os.path.exists(f):
            print(f"Missing mandatory project file: {f}")
            sys.exit(1)
    print("Project environment integrity verified successfully.")

if __name__ == "__main__":
    verify_all()
