# 🛍️ E-Commerce Customer Analytics & Revenue Optimization Engine

A modular, production-grade data analytics pipeline and interactive dashboard built to sanitize, parse, and analyze messy corporate transaction logs.

## 📂 Project Architecture
* **`data_generator.py`**: Simulates messy tracking database tables containing string injections and missing elements.
* **`data_pipeline.py`**: A processing pipeline that cleans anomalies and engineers high-value business parameters (AOV, hourly density tracking).
* **`app.py`**: Interactive visual front-end dashboard powered by Streamlit and Plotly layouts.

## 🛠️ Technology Stack
* **Language:** Python
* **Data Processing & Analytics:** Pandas, NumPy
* **Interface & Visualizations:** Streamlit, Plotly (Dynamic Dark-Mode Charts)

## 🚀 How to Execution Pipeline Locally
1. Run data generator: `python data_generator.py`
2. Execute data tracking pipeline: `python data_pipeline.py`
3. Launch live dashboard: `python -m streamlit run app.py`
