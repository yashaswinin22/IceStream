from quality_rules import (
    get_invalid_records,
    get_valid_records
)


def process_pipeline(df, error_threshold=2.0):

    total_records = len(df)

    invalid_data = get_invalid_records(df)

    valid_data = get_valid_records(df)

    invalid_records = len(invalid_data)

    if total_records > 0:
        error_rate = (
            invalid_records / total_records
        ) * 100
    else:
        error_rate = 0

    if error_rate > error_threshold:
        status = "PAUSED"
    else:
        status = "RUNNING"

    return {
        "total_records": total_records,
        "invalid_records": invalid_records,
        "error_rate": error_rate,
        "status": status,
        "valid_data": valid_data,
        "quarantine": invalid_data
    }
