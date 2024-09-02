import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name = "end_to_end_data_science_project"

list_of_files=[
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_monitoring.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/trainig_pipeline.py',
    f'src/{project_name}/pipeline/prediction_pipeline.py',
    f'src/{project_name}/exception.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/utils.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filename)
    
    # This logic is used to make folders only
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    #File created
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")



