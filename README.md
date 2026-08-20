# IceStream

IceStream is a real-time lakehouse observability prototype for monitoring streaming data quality and protecting downstream analytics from bad data.

## Features

- Mock e-commerce transaction streaming
- Data quality monitoring
- NULL value detection
- Error-rate calculation
- 2% circuit breaker threshold
- Bad-data quarantine
- Dead Letter Queue concept
- Pipeline status monitoring
- Streamlit observability dashboard

## Technology

- Python
- Streamlit
- Pandas
- Apache Kafka architecture concept
- Apache Flink architecture concept
- Apache Iceberg architecture concept

## Project Structure

```text
IceStream/
├── app.py
├── data_generator.py
├── quality_rules.py
├── pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
