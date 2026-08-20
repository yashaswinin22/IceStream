import streamlit as st
import pandas as pd

from data_generator import generate_data
from quality_rules import check_quality
from pipeline import process_pipeline

st.set_page_config(
    page_title="IceStream",
    page_icon="❄️",
    layout="wide"
)

st.title("❄️ IceStream")
st.subheader("Real-Time Lakehouse Observability")

st.write(
    "Monitor streaming data quality and detect bad data "
    "before it reaches the analytics layer."
)

if "data" not in st.session_state:
    st.session_state.data = generate_data()

if "result" not in st.session_state:
    st.session_state.result = None

df = st.session_state.data

st.sidebar.header("Pipeline Controls")

error_threshold = st.sidebar.number_input(
    "Error Threshold (%)",
    min_value=1.0,
    max_value=20.0,
    value=2.0,
    step=1.0
)

if st.sidebar.button("Generate New Stream"):
    st.session_state.data = generate_data()
    st.session_state.result = None
    st.rerun()

if st.sidebar.button("Run Pipeline"):
    st.session_state.result = process_pipeline(
        st.session_state.data,
        error_threshold
    )

st.markdown("---")

st.header("🔄 Streaming Pipeline")

steps = [
    "📥 Ingest",
    "📡 Kafka",
    "⚙️ Flink",
    "🧊 Iceberg",
    "🔍 Quality Check"
]

cols = st.columns(len(steps))

for col, step in zip(cols, steps):
    col.info(step)

st.markdown("---")

if st.session_state.result is not None:

    result = st.session_state.result

    st.header("📊 Pipeline Status")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Records",
        result["total_records"]
    )

    col2.metric(
        "Invalid Records",
        result["invalid_records"]
    )

    col3.metric(
        "Error Rate",
        f"{result['error_rate']:.2f}%"
    )

    col4.metric(
        "Pipeline Status",
        result["status"]
    )

    if result["status"] == "RUNNING":

        st.success(
            "Pipeline is healthy. Valid data can continue "
            "to the analytics layer."
        )

    else:

        st.error(
            "Circuit breaker activated. The invalid data "
            "has been isolated from the main pipeline."
        )

    st.markdown("---")

    st.header("🔍 Data Quality Checks")

    quality_result = check_quality(df)

    st.dataframe(
        quality_result,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.header("📈 Data Quality Summary")

    col1, col2 = st.columns(2)

    col1.metric(
        "Valid Records",
        len(result["valid_data"])
    )

    col2.metric(
        "Quarantined / DLQ Records",
        len(result["quarantine"])
    )

    st.markdown("---")

    st.header("⚠️ Quarantine / Dead Letter Queue")

    if len(result["quarantine"]) > 0:

        st.warning(
            "Bad records detected. They have been isolated "
            "from the main data flow."
        )

        st.dataframe(
            result["quarantine"],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "No invalid records were detected."
        )

else:

    st.info(
        "Click 'Run Pipeline' to start real-time "
        "data quality monitoring."
    )

st.markdown("---")

st.header("📋 Streaming Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.header("🧭 Pipeline Architecture")

st.code(
    """
Mock E-commerce Stream
          ↓
        Kafka
          ↓
        Flink
          ↓
       Iceberg
          ↓
    Data Quality Rules
          ↓
     ┌───────────────┐
     │   Valid Data  │ → Analytics
     └───────────────┘

     ┌───────────────┐
     │   Bad Data    │
     └───────┬───────┘
             ↓
      Circuit Breaker
             ↓
        Quarantine
             ↓
            DLQ
""",
    language="text"
)

st.markdown("---")

st.caption(
    "IceStream | Real-Time Lakehouse Observability"
)
