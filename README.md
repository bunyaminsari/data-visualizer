# Sales Data Visualizer

This Streamlit app allows users to upload CSV or Excel files containing sales data and generates various visualizations to provide insights into the data.

## Features

- File upload for CSV and Excel files
- Display of raw data
- Interactive visualizations:
  1. Total Revenue by Product Category
  2. Customer Age Distribution
  3. Revenue Trend Over Time
  4. Top 10 Products by Profit
  5. Revenue by Country (Choropleth Map)

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/bunyaminsari/data-visualizer.git
   cd data-visualizer
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
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

4. The app will display the raw data and generate interactive visualizations based on the uploaded file.

## Data Format

The app expects the following columns in your CSV or Excel file:

## Customization

You can customize the visualizations or add new ones by modifying the `app.py` file. The app uses Plotly for creating interactive charts, so refer to the [Plotly Python documentation](https://plotly.com/python/) for more chart types and options.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Plotly](https://plotly.com/) - Interactive graphing library

## Contact

Bunyamin Sari - [@bunyaminsari](https://github.com/bunyaminsari)

Project Link: [https://github.com/bunyaminsari/data-visualizer](https://github.com/bunyaminsari/data-visualizer)
