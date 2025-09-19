import pandas as pd
import sys

def transform(input_path, output_path):
    df = pd.read_csv(input_path)

    # Example transformation: compute total value per order
    df["total_value"] = df["quantity"] * df["price"]

    # Aggregate by customer to get total spend
    aggregated = df.groupby("customer", as_index=False)["total_value"].sum()

    aggregated.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")

if __name__ == "__main__":
    transform(sys.argv[1], sys.argv[2])
