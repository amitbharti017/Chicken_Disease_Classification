import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "chicken_disease_classifier"
list_of_files = [
    ".github/workflows/.gitkeep",       #required during deployment to write CI/CD commands in YAML file
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != "": #to check if the variable have a directory name or not
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for the file : {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file : {file_path}")
    else:
        logging.info(f"{file_name} is already exist")

