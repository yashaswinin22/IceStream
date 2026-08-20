import pandas as pd


def check_quality(df):

    tax_nulls = df["Tax_Amount"].isna().sum()

    transaction_nulls = (
        df["Transaction_ID"].isna().sum()
    )

    amount_nulls = df["Amount"].isna().sum()

    return pd.DataFrame({
        "Quality Check": [
            "Tax Amount NULL Check",
            "Transaction ID NULL Check",
            "Amount NULL Check"
        ],
        "Invalid Records": [
            tax_nulls,
            transaction_nulls,
            amount_nulls
        ],
        "Status": [
            "FAILED" if tax_nulls > 0 else "PASSED",
            "FAILED" if transaction_nulls > 0 else "PASSED",
            "FAILED" if amount_nulls > 0 else "PASSED"
        ]
    })


def get_invalid_records(df):

    return df[
        df["Tax_Amount"].isna()
        | df["Transaction_ID"].isna()
        | df["Amount"].isna()
    ].copy()


def get_valid_records(df):

    return df[
        df["Tax_Amount"].notna()
        & df["Transaction_ID"].notna()
        & df["Amount"].notna()
    ].copy()
