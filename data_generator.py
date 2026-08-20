import random
import pandas as pd


def generate_data(rows=100):

    records = []

    for i in range(rows):

        tax_amount = round(
            random.uniform(5, 500),
            2
        )

        if random.random() < 0.10:
            tax_amount = None

        records.append({
            "Transaction_ID": f"TXN{i + 1:04d}",
            "Customer_ID": f"CUST{random.randint(100, 999)}",
            "Product": random.choice([
                "Laptop",
                "Mobile",
                "Headphones",
                "Keyboard",
                "Monitor"
            ]),
            "Quantity": random.randint(1, 5),
            "Tax_Amount": tax_amount,
            "Amount": round(
                random.uniform(100, 5000),
                2
            )
        })

    return pd.DataFrame(records)
