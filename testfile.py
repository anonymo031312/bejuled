from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to perform functional test
def perform_functional_test():
    # Initialize the WebDriver (you need to install the corresponding browser driver, e.g., chromedriver for Chrome)
    driver = webdriver.Chrome()
    
    try:
        # Open the webpage
        driver.get("file:///C:/Users/reche/OneDrive/Desktop/PROG4-FOLIO/main.html")  # Replace with the path to your HTML file

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nav__logo")))

        # Find and click on the navigation menu toggle
        nav_toggle = driver.find_element(By.ID, "nav-toggle")
        nav_toggle.click()

        # Wait for the navigation menu to appear
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "nav-menu")))

        # Find and click on a navigation link (e.g., "About")
        about_link = driver.find_element(By.XPATH, "//a[@href='#about']")
        about_link.click()

        # Wait for the "About" section to appear
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "about")))

        # Assert that the "About" section title is correct
        about_title = driver.find_element(By.XPATH, "//h2[@class='section-title']")
        assert about_title.text == "About"

        print("Functional test completed successfully.")

    finally:
        # Close the WebDriver
        driver.quit()

# Call the function to perform the functional test
perform_functional_test()
