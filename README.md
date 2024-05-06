# Python Project with Selenium

This project automates intermittent qunit tests using Python and the Selenium library. It includes a virtual environment setup and a `requirements.txt` file for easy installation of dependencies.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **WebDriver**: Ensure you have the necessary WebDriver (e.g., `chromedriver` for Chrome) installed and available in your system's PATH.

## Setup Instructions

1. **Clone or Download the Project:**
   - Clone this repository or download it as a ZIP file and unzip it to a desired directory.

2. **Set Up a Virtual Environment:**
   - Open a terminal (macOS/Linux) or command prompt (Windows) and navigate to the project's root directory.
   - Create a virtual environment by running:

     ```bash
     python -m venv env
     ```

   - Activate the virtual environment:
     - **Windows**:
       ```cmd
       env\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source env/bin/activate
       ```

3. **Install Dependencies:**
   - With the virtual environment activated, install the required packages:

     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Project:**
   - Make sure the virtual environment is still activated.
   - Run the main Python script:

     ```bash
     python script.py
     ```

## Important Notes

- Make sure that the correct WebDriver (e.g., `chromedriver`) is installed and is compatible with your browser version. Follow the instructions on the Selenium documentation to download the latest version of your WebDriver.
- Adjust the WebDriver path or the browser profile options in the code if needed.
