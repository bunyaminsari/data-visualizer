# Sales Data Visualizer

This Streamlit app allows users to upload CSV or Excel files containing sales data and generates various visualizations to provide insights into the data.

## Features

- File upload for CSV and Excel files
- Display of raw data
- Visualizations:
  1. Total Revenue by Product Category
  2. Customer Age Distribution
  3. Revenue Trend Over Time
  4. Top 10 Products by Profit
  5. Revenue by Country

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/sales-data-visualizer.git
   cd sales-data-visualizer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Use the file uploader to select your CSV or Excel file.

4. The app will display the raw data and generate visualizations based on the uploaded file.

## Data Format

The app expects the following columns in your CSV or Excel file:

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
