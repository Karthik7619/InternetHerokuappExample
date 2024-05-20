from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/abtest")
driver.maximize_window()
wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
expected_result = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."

try:
    # Wait until the first element is visible
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='A/B Test Variation 1']"))
    )
    print(element.text)

    # Wait until the paragraph element is visible
    element1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Also known as split testing. This is a way in whic')]"))
    )

    # Retrieve the text from the element
    element1_text = element1.text
    print(element1_text)

    # Compare the text with the expected result
    if expected_result in element1_text:
        print("Text is present and matches the expected result")
    else:
        print("Text does not match the expected result")

except TimeoutException:
    print("An error occurred")
finally:
    driver.quit()
