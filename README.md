# ACCPP Archive-Viewer

This project is a web application that visualizes the directory tree of an archive. It is built with Flask, Flask-CORS, and pandas.

## Prerequisites

Before you begin, ensure you have met the following requirements:

1. **Windows Operating System**: This guide assumes you are using a Windows environment.
2. **Python**: You need to have Python installed on your machine. You can download and install Python from [python.org](https://www.python.org/downloads/).

## Installation

Follow these steps to get your project up and running:

1. **Clone the repository**: First, clone the repository to your local machine. Open a terminal or command prompt and run the following command:
    ```sh
    git clone https://github.com/immortalbob/Archive-Viewer/
    ```
   Replace `<repository_url>` with the URL of your repository.

2. **Navigate to the project directory**:
    ```sh
    cd path/to/your/project
    ```

3. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

4. **Install the required dependencies**:
    ```sh
    pip install Flask Flask-CORS pandas
    ```

5. **Prepare the CSV data**: Ensure you have a CSV file named `directory.csv` in the project directory. This file should contain the data you want to visualize.

## Running the Application

1. **Start the Flask application**:
    ```sh
    python archive_viewer.py
    ```

2. **Open your web browser**: Once the server is running, open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

   You should see the ACCPP Archive File Tree application up and running.

## File Structure

Here is a brief overview of the important files in this project:

- **archive_viewer.py**: The main Flask application file.
- **templates/index.html**: The HTML template for the web application.
- **static/styles.css**: The CSS stylesheet for the web application.
- **directory.csv**: The CSV file containing the archive data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
