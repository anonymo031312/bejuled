from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Start the WebDriver and open the web page
driver = webdriver.Chrome()
driver.get("file:///C:\Users\lab_exam\main.html")  # Replace with the path to your HTML file

try:
    # Test navigation to different sections
    nav_links = driver.find_elements_by_class_name("nav__link")
    for link in nav_links:
        link.click()
        time.sleep(1)  # Wait for page to load
        assert "active" in link.get_attribute("class"), "Navigation link is not active"

    # Test button click
    button = driver.find_element_by_class_name("button")
    button.click()
    time.sleep(1)  # Wait for page to load

    # Test social media links
    social_links = driver.find_elements_by_class_name("footer__icon")
    for link in social_links:
        link.click()
        time.sleep(1)  # Wait for page to load
        assert "active" in link.get_attribute("class"), "Social media link is not active"

finally:
    # Close the WebDriver
    driver.quit()

