import os
from pathlib import Path

notebooks_dir = Path(r"c:\Users\Faheem\Desktop\Github\bot\FYP2025-Fraud-Detection\notebooks")
notebooks = [
    "02_data_preprocessing.ipynb",
    "03_imbalance_handling.ipynb",
    "04_baseline_models.ipynb",
    "05_advanced_models.ipynb",
    "06_neural_network.ipynb",
    "08_explainability.ipynb",
    "09_comprehensive_diagnostics.ipynb",
    "ProblemAnalysis.ipynb"
]

target_str = "PROCESSED_DIR = Path('../data/processed')"
replacement_str = "PROCESSED_DIR = Path('../data/processed/new_analysis')"

for nb_name in notebooks:
    nb_path = notebooks_dir / nb_name
    if nb_path.exists():
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target_str in content:
                new_content = content.replace(target_str, replacement_str)
                with open(nb_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {nb_name}")
            else:
                print(f"Target string not found in {nb_name}")
        except Exception as e:
            print(f"Error updating {nb_name}: {e}")
    else:
        print(f"File not found: {nb_name}")
