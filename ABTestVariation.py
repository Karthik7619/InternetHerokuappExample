from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/abtest")
driver.maximize_window()
wait = WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[Exception])
expected_result = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."

try:
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='A/B Test Variation 1']"))
    )
    print(element.text)


    # Wait until the text is present in the specified element
    element1 = wait.until(
        EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Also known as split testing. This is a way in whic')]"))
    )
    print(element1.text)
    if expected_result in element1:
        print("Text is present")
    else:
        print("Test is not present")

except TimeoutException:
    print("An error occurred")
finally:
    driver.quit()





