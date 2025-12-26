# End-To-End-Data-Analysis-Project

This repository contains a modular Python-based ETL (Extract, Transform, Load) pipeline designed to automate data workflows from source to database.

## 🚀 Project Overview

The pipeline automates the retrieval of datasets, processes them for analysis, and ensures persistent storage in a SQL environment. It is built with a focus on modularity, allowing each stage of the data lifecycle to be managed independently.


<p align="center">
  <img width="900" height="500" alt="Screenshot 2025-12-27 at 4 25 46 AM"
       src="https://github.com/user-attachments/assets/e5d065c2-ff55-4ef4-b15d-47c3405df51c" />
</p>





#### Key Features

- Data Manipulation: Utilizes pandas for efficient data cleaning and transformation. 

- Automated Ingestion: Integrated with the kaggle API to programmatically fetch the latest data. 

- Database Connectivity: Employs sqlalchemy and pyodbc for robust connections to SQL databases. 

- Modular Architecture: Separates logic into dedicated modules for loading, extraction, and transformation.


## 📁 Project Structure

The repository is organized into specialized directories to maintain clean code standards:

- data_loading/: Scripts to download datasets via the Kaggle API.

- extraction/: Logic for unzipping and preparing raw data files.

- transformation/: Core logic for data cleaning and feature engineering using Pandas.

- database/: Scripts to handle SQL authentication and data loading.

- main.ipynb: The central orchestration notebook that executes the full pipeline.


## 🛠️ Installation & Setup

####  Clone the Repository
git clone https://github.com/Mustafa-Pario/End-To-End-Data-Analysis-Project.git
cd End-To-End-Data-Analysis-Project

####  Install Dependencies 
The project requires the following Python libraries:
pip install -r requirements.txt

#### Configure Kaggle API 
Ensure your kaggle.json credentials are placed in the ~/.kaggle/ directory to enable automated downloads.


## ⚙️ Execution Flow
The entire workflow is orchestrated in main.ipynb through the following sequence:

- download_data(): Fetches the raw dataset from Kaggle.

- extract_file(): Unpacks compressed files for processing.

- transform_data(): Performs data cleaning and returns a structured DataFrame.

- load_data(df): Uploads the processed data into the target SQL database.



## 🧰 Tech Stack

- Language: Python 3.13+

- Analysis: Pandas 

- Database: SQLAlchemy, pyodbc 

- API: Kaggle





