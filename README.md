# FYP2025 Fraud Detection

Research-grade credit card fraud detection pipeline for MSc/Final Year Project. Focuses on reproducibility, ethical/ explainable ML, and imbalanced data handling using Python + Jupyter.

## Folder Structure
- `data/raw/` — original dataset (`credit_card_fraud_dataset.csv`)
- `data/processed/` — scaled/split/resampled datasets
- `notebooks/` — ordered workflow notebooks (01–08)
- `models/saved_models/` — serialized models/checkpoints
- `results/figures/` and `results/metrics/` — plots and metric exports
- `venv/` — project virtual environment

## Setup & Reproducibility
1) Create and activate the virtual environment (PowerShell):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2) Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3) Launch Jupyter Lab/Notebook from the project root with the venv active:
   ```
   jupyter notebook
   ```

## Notebook Workflow (all work happens in notebooks)
1. `01_data_loading_and_eda.ipynb` — load raw data, EDA only (no preprocessing).
2. `02_data_preprocessing.ipynb` — stratified split, scaling, save processed data.
3. `03_imbalance_handling.ipynb` — SMOTE, undersampling, class weights (train-only).
4. `04_baseline_models.ipynb` — logistic regression, decision tree baselines.
5. `05_advanced_models.ipynb` — random forest, XGBoost/LightGBM with tuning.
6. `06_neural_network.ipynb` — TensorFlow/Keras NN with dropout + early stopping.
7. `07_model_evaluation.ipynb` — aggregate metrics, threshold tuning, model selection.
8. `08_explainability.ipynb` — SHAP + LIME transparency and ethics discussion.

> README remains draft/iterable. Add results and conclusions later once experiments are run.