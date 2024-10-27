import streamlit as st
import pandas as pd
import plotly.express as px

EXPECTED_COLUMNS = {
    'Date': 'Date',
    'Customer_Age': 'Customer Age',
    'Country': 'Country',
    'Product_Category': 'Product Category',
    'Product': 'Product',
    'Revenue': 'Revenue',
    'Profit': 'Profit'
}

def suggest_column_mapping(df):
    suggestions = {}
    for expected_col, display_name in EXPECTED_COLUMNS.items():
        if expected_col not in df.columns:
            similar_columns = df.columns[df.columns.str.lower().str.contains(expected_col.lower())]
            if len(similar_columns) > 0:
                suggestions[expected_col] = st.selectbox(
                    f"Select column for {display_name}",
                    options=[''] + list(similar_columns),
                    format_func=lambda x: f"{x} (suggested)" if x == similar_columns[0] else x
                )
            else:
                suggestions[expected_col] = st.selectbox(
                    f"Select column for {display_name}",
                    options=[''] + list(df.columns)
                )
        else:
            suggestions[expected_col] = expected_col
    return suggestions

def main():
    st.title("Sales Data Visualizer")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Display the raw data
        st.subheader("Raw Data")
        st.write(df)

        column_mapping = suggest_column_mapping(df)

        if st.button("Create Visualizations"):
            # Rename columns based on user selection
            df_mapped = df.rename(columns={v: k for k, v in column_mapping.items() if v})

            # Check if all required columns are present
            if all(col in df_mapped.columns for col in EXPECTED_COLUMNS.keys()):
                create_visualizations(df_mapped)
            else:
                st.error("Please map all required columns to create visualizations.")

def create_visualizations(df):
    # 1. Total Revenue by Product Category
    st.subheader("Total Revenue by Product Category")
    category_revenue = df.groupby('Product_Category')['Revenue'].sum().reset_index()
    fig1 = px.bar(category_revenue, x='Product_Category', y='Revenue', 
                  title='Total Revenue by Product Category')
    st.plotly_chart(fig1)

    # 2. Customer Age Distribution
    st.subheader("Customer Age Distribution")
    fig2 = px.histogram(df, x='Customer_Age', nbins=20, 
                        title='Customer Age Distribution')
    st.plotly_chart(fig2)

    # 3. Revenue Trend Over Time
    st.subheader("Revenue Trend Over Time")
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_revenue = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
    monthly_revenue['Date'] = monthly_revenue['Date'].dt.to_timestamp()
    fig3 = px.line(monthly_revenue, x='Date', y='Revenue', 
                   title='Monthly Revenue Trend')
    st.plotly_chart(fig3)

    # 4. Top 10 Products by Profit
    st.subheader("Top 10 Products by Profit")
    top_products = df.groupby('Product')['Profit'].sum().nlargest(10).reset_index()
    fig4 = px.bar(top_products, x='Product', y='Profit', 
                  title='Top 10 Products by Profit')
    st.plotly_chart(fig4)

    # 5. Revenue by Country
    st.subheader("Revenue by Country")
    country_revenue = df.groupby('Country')['Revenue'].sum().reset_index()
    fig5 = px.choropleth(country_revenue, locations='Country', 
                         locationmode='country names', color='Revenue', 
                         title='Revenue by Country')
    st.plotly_chart(fig5)

if __name__ == "__main__":
    main()
