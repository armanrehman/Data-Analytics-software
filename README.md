# Data Analytics and Visualization Web App

## Project Overview
This project is a web-based data analytics and visualization tool built using Python, Django, Pandas, and ChartJS. The web app allows users to upload a CSV file, processes the data, and displays the results in an interactive format with data visualization charts. The app is designed to help users analyze the data from the uploaded file and view various charts representing key insights from the data. 

This project was built based on a demo **Software Requirements Specification (SRS)** document that outlined the specifications and instructions for developing this tool. The example CSV file for demonstrating functionality is attached.

## Technologies Used
- **Python**: Programming language used for backend logic.
- **Django**: Web framework for building the application.
- **Pandas**: Data manipulation and analysis library used to process the CSV data.
- **ChartJS**: Library used to create interactive visualizations and charts.
- **HTML**: Markup language used to structure the web pages.
- **CSS**: Styling language used to design and style the webpage.

## Project Description
The steps involved in the project are as follows:
1. **Development Environment Setup**: Setting up the required development environment on your machine, including installing Django and other dependencies.
2. **CSV File Handling**: The app allows users to upload a CSV file. The data from this file is processed and converted into a Pandas DataFrame for easy manipulation and analysis.
3. **Data Rendering**: The processed data is displayed in a tabular format on an HTML page.
4. **Data Visualization**: After analyzing the data using Pandas, the processed data is visualized using ChartJS and rendered as interactive charts on the webpage.

## Example Files
- **Test CSV File**: An example CSV file (`test.csv`) is provided, which can be uploaded into the app for testing and analysis.

## Installation
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    ```
2. **Navigate to the project directory**:
    ```bash
    cd <project-directory>
    ```
3. **Create and activate a virtual environment** :
    - For Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      python3 -m venv venv
      venv\Scripts\activate
      ```
4. **Install the required dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```
5. **Run database migrations**:
    ```bash
    python3 manage.py migrate
    ```
7. **Run the Django development server**:
    ```bash
    python3 manage.py runserver
    ```
8. **Open the app in your browser**:
    Open your browser and go to to the server link





