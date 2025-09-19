import pandas as pd
import sys

def extract(input_path, output_path):
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print(f"Extracted {len(df)} rows to {output_path}")

if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])