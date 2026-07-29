# carisurg-portfolio
# Overview

This respository contains my work completed as part of the CariSurg MedTech Pathways Programme. It serves as a portfolio to showcase my code and projects that include data science, machine learning, research papers and healthcare analytics.

# What is this project?

This project predicts a patient's Emergency Severity Index (ESI, 1-5) at the moment of ED triage. Earlier weeks covered data cleaning, processing, exploratory data analysis, and visualization of clinical datasets, improving data quality through imputation, correcting inconsistent entries, and validating data ranges. Week 7 benchmarked six candidate models and selected a final one (see docs/model-selection.md). Week 8 refactored the notebook code into a reproducible src/ package driven by a single config.yaml (see HANDOVER.md).

# Who is it for?

This repository is intended for:

CariSurg mentors and instructors
Students learning healthcare data science and AI
Researchers interested in medical data preprocessing
Recruiters and employers reviewing my technical portfolio
Anyone interested in healthcare analytics using Python

# How do I install and run it?

1. Clone the repository
git clone https://github.com/varunegit/carisurg-portfolio.git
cd carisurg-portfolio
2. Install dependencies
pip install -r requirements.txt
3. Place the dataset in data/ (see Data Source below)
4. Train the pinned final model
python scripts/train.py --config config.yaml

Exploratory notebooks (Weeks 0-7) remain in notebooks/ and can still be run directly in Jupyter or Google Colab.

# Reproducibility

The random seed (42) is fixed in config.yaml and applied to the train/test split and every model. Re-running python scripts/train.py --config config.yaml on the same data should reproduce the same held-out metrics reported in docs/model-selection.md.

# Data Source

The data used an emergency department triage dataset for educational and research purposes. To protect from data leaks, the datasets were stored locally in the data/ folder and excluded from this public respoistory through .gitignore. Users wishing to reproduce the analyses should place the required dataset into data/ folder before running the notebooks.

# Author
Varune Joseph
Participant in the CariSurg MedTech Pathways Programme with interests in Artificial Intelligence and Machine Learning

# Contact

GitHub: https://github.com/varunegit
