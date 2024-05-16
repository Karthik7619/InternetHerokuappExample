import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the browser
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
# Click the button to trigger the alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Wait for the alert to appear
# alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert

# Get the text of the alert
# alert_text = alert.text
# print(alert_text)

# Close the alert by accepting it
alert.accept()
result_message = driver.find_element(By.ID, "result")
# Get the text of the result message
result_message_text = result_message.text
print(result_message_text)
# Verify the result message
expected_message = "You successfully clicked an alert"
if result_message_text == expected_message:
    print("Result message matches the expected message:", result_message_text)
else:
    print("Result message does not match the expected message. Expected:", expected_message, "Actual:", result_message_text)



# Close the browser
driver.quit()
