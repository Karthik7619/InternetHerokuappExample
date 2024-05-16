import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(5)

#Method 1
# JSAlert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
# alertwindow = driver.switch_to.alert
# alertwindow.accept()
# time.sleep(5)
# alertmsg="You successfully clicked an alert"
# result_message = driver.find_element(By.ID, "result")
# result_message_text=result_message.text
# print(result_message_text)
# if alertmsg == result_message_text:
#     print("JS Alert is clicked and message is displayed")
# else:
#     print("Does not click on JS alert")

#Method 2
JSAlert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
alert = WebDriverWait(driver,10).until(EC.alert_is_present())
alert.accept()
alertmsg="You successfully clicked an alert"
result_message = driver.find_element(By.ID, "result")
result_message_text=result_message.text
print(result_message_text)
if alertmsg == result_message_text:
    print("JS Alert is clicked and message is displayed")
else:
    print("Does not click on JS alert")




# # # JSAlertMsg = driver.find_element(By.ID,"result")
# # result_message = driver.find_element(By.ID,"result")
# # JSAlertMsgText = result_message.text
# # print(JSAlertMsgText)
# # alertmsg = "You successfully clicked an alert"
# #
# #
# # JSConfirm = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
# # JSConfirmMsg = driver.find_element(By.XPATH,"//p[@id='result']")
# # JSConfirmMsgText = JSConfirmMsg.text
# # print(JSConfirmMsgText)
# #
# #
# # JSPrompt = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
# # JSPromptMsg = driver.find_element(By.XPATH,"//p[@id='result']").text
# # alertmsgWelcome= "You entered: Welcome"
# #
# #
# #
# #
# #
# if alertmsg == JSAlertMsg:
#     print("JS Alert is clicked and message is displayed")
# else:
#     print("Does not click on JS alert")
# time.sleep(4)
#
# #JS Confirm
# JSConfirm.click()
# alertwindow1=driver.switch_to.alert
# time.sleep(5)
# alertwindow1.dismiss()
# print(alertmsgCancel)
# if alertmsgCancel.strip() == JSConfirmMsg.strip():
#     print("JS Confirm is cancelled")
# else:
#     print("JS Confirm is not Cancelled")
# time.sleep(5)
#
# JSPrompt.click()
# alertwindow2 = driver.switch_to.alert
# alertwindow2.send_keys("Welcome")
# time.sleep(5)
# alertwindow2.accept()
# time.sleep(5)
# JSPromptMsg = driver.find_element(By.XPATH,"//p[@id='result']").text
# print(alertmsgWelcome)
# print(JSPromptMsg)
# if alertmsgWelcome.strip() == JSPromptMsg.strip():
#     print("Message is entered in Prompt and Clicked OK")
# else:
#     print("Message is not entered")
#
# time.sleep(5)