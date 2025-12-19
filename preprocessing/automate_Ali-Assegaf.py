import pandas as pd
import os

def run_preprocessing(input_path, output_path):
    print(f"Memulai preprocessing data dari: {input_path}")
    
    # Cek apakah file raw ada
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} tidak ditemukan!")
        return

    # 1. Load Data
    column_names = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
    ]
    df = pd.read_csv(input_path, names=column_names, na_values='?')

    # 2. Cleaning Missing Values
    df = df.dropna()

    # 3. Simplify Target (Binary Classification)
    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

    # 4. Drop Duplicates
    df = df.drop_duplicates()

    # 5. Save Output
    df.to_csv(output_path, index=False)
    print(f"Selesai! Data bersih disimpan di: {output_path}")

if __name__ == "__main__":
    # Path disesuaikan: Mengacu langsung ke folder heart_disease_raw tanpa tanda ../
    raw_data = "heart_disease_raw/heart_disease.csv"
    clean_data = "heart_disease_preprocessed.csv"
    
    run_preprocessing(raw_data, clean_data)