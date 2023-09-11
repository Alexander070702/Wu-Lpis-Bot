from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Description:
# This script automates the process of logging into the LPIS system of WU University and registering for a course.
# It waits until a specified time to refresh the page and click the registration button.

# Path to Chrome Driver
browser = webdriver.Chrome("/Users/alexanderhillisch/Desktop/Chrome/chromedriver")

# Open the LPIS website
browser.get('https://lpis.wu.ac.at/lpis')

# Wait for the page to load
time.sleep(1)

# Locate the student ID and password fields
matr_nr = browser.find_element(By.XPATH, '//*[@id="login"]/table/tbody/tr[1]/td[2]/input')
password = browser.find_element(By.XPATH, '//*[@id="login"]/table/tbody/tr[2]/td[2]/input')

# Enter login credentials (Please replace with your credentials)
matr_nr.send_keys('YOUR_MATRIKELNUMMER')
password.send_keys('YOUR_PASSWORD')

time.sleep(1)

# Click the login button
login_button = browser.find_element(By.XPATH, '//input[@value="Login"]')
login_button.click()
time.sleep(1)

# Select the course filter and desired course
filter = browser.find_element(By.XPATH, '//*[@id="ea_stupl"]/select')
filter.click()
time.sleep(1)
winf = browser.find_element(By.XPATH, '//*[@id="ea_stupl"]/select/option[6]')
winf.click()
anzeigen = browser.find_element(By.XPATH, '//*[@id="ea_stupl"]/input[4]')
anzeigen.click()
time.sleep(1)

# Function to refresh the page
def reload_page():
    browser.refresh()

# Set the time to refresh the page and register
reload_time = "15:59:59"

# Select the desired course (Change the XPath accordingly)
lv = browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[29]/td[1]/span[3]") 
lv.click()
time.sleep(1)

# Function to click the registration button (Change the XPath accordingly)
def click_anmeldebutton():
    lv_id = browser.find_element(By.XPATH, '//*[@id="SPAN_483168_247493"]/input[10]')
    print("Course ID found")
    lv_id.click()
    print("Course ID found and registered")
    time.sleep(1)
    return

# Set the Veranstaltung number (Change this value as needed)
veranstaltung_number = "4736"

# Main loop to wait for the specified time and register
try:
    while True:
        current_time = time.strftime("%H:%M:%S")
        
        if browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[1]/td[4]/div').text == "ABmelden":
            print("Already registered")
            time.sleep(1000)
    
        if current_time == reload_time:
            reload_page()
            click_anmeldebutton()
            if browser.find_element(By.XPATH, f"/html/body/div/div/b").text == f"Die Anmeldung zur Veranstaltung {veranstaltung_number} wurde durchgeführt.":
                print("Registration successful")
                time.sleep(20000)
                break
        elif current_time > reload_time:
            while True: 
                reload_page()
                click_anmeldebutton()
                time.sleep(20000)

# Close the browser in case of an error
except:
    while True:
        print("Final Error --> Going to sleep")
        time.sleep(600000)
        browser.close()
