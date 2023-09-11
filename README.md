LPIS Course Registration Automation

This script automates the process of logging into the LPIS system of WU University and registering for a course. It waits until a specified time to refresh the page and click the registration button.

Features

Automated login to the LPIS system.
Waits for a specified time to refresh the page.
Automatically clicks the registration button for a specified course.
Handles errors and exceptions gracefully.
Prerequisites

Python 3.x
Selenium library for Python
ChromeDriver
Setup

Install the required Python libraries:
bash
Copy code
pip install selenium
Download the appropriate version of ChromeDriver and place it in a known directory.
Update the path to ChromeDriver in the script:
python
Copy code
browser = webdriver.Chrome("/path/to/your/chromedriver")
Replace 'YOUR_MATRIKELNUMMER' and 'YOUR_PASSWORD' in the script with your actual LPIS login credentials.
Adjust the veranstaltung_number variable in the script to the desired "Veranstaltung" number.
Usage

Run the script:

bash
Copy code
python your_script_name.py
The script will automatically open a Chrome browser window, log into the LPIS system, and wait until the specified time to refresh the page and register for the course.

Note

Ensure that you have a stable internet connection while the script is running.
Do not manually interfere with the browser window while the script is executing.
