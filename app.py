import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Intelligence Panel", layout="wide", page_icon="🛍️")

st.title("🛍️ E-Commerce Customer Analytics & Revenue Dashboard")
st.markdown("---")

@st.cache_data
def load_clean_data():
    try:
        df = pd.read_csv("clean_transactions.csv")
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
        return df
    except FileNotFoundError:
        st.error("⚠️ Data files are missing! Please execute data_generator.py and data_pipeline.py inside your console first.")
        return None

df = load_clean_data()

if df is not None:
    # --- Top KPIs Panel ---
    total_revenue = df['TotalRevenue'].sum()
    total_orders = df['InvoiceNo'].nunique()
    aov = total_revenue / total_orders
    
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Enterprise Revenue", f"${total_revenue:,.2f}")
    kpi2.metric("Total Successful Orders", f"{total_orders:,}")
    kpi3.metric("Average Order Value (AOV)", f"${aov:.2f}")
    
    st.markdown("### Market Segment Explorations")
    col_left, col_right = st.columns(2)
    
    # --- Graph 1: Category Streams ---
    cat_df = df.groupby('Category')['TotalRevenue'].sum().reset_index()
    fig_cat = px.bar(
        cat_df, x='Category', y='TotalRevenue',
        title='Revenue Streams Across Product Categories',
        labels={'TotalRevenue': 'Revenue ($)'},
        text_auto='.2s', template='plotly_dark'
    )
    fig_cat.update_traces(marker_color='#00CC96')
    col_left.plotly_chart(fig_cat, use_container_width=True)
    
    # --- Graph 2: Hourly Sales Density ---
    hourly_df = df.groupby('HourOfDay')['TotalRevenue'].sum().reset_index()
    fig_hour = px.line(
        hourly_df, x='HourOfDay', y='TotalRevenue',
        title='Hourly Conversion Densities (Target Marketing)',
        labels={'TotalRevenue': 'Sales Invoiced ($)'},
        template='plotly_dark'
    )
    fig_hour.update_traces(line_color='#AB63FA', line_width=3)
    col_right.plotly_chart(fig_hour, use_container_width=True)