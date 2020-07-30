
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://techstepacademy.com/trial-of-the-stones")

#Riddle of Stone 
stoneInput = driver.find_element_by_css_selector("input#r1Input")
stoneInput.send_keys("rock")

stoneAnswerButton = driver.find_element_by_css_selector("button#r1Btn")
stoneAnswerButton.click()

riddleOfStoneBanner = driver.find_element_by_css_selector("div#passwordBanner h4")

#Riddle of Secrets 

riddleOfSecretsInput = driver.find_element_by_css_selector("input#r2Input")
riddleOfSecretsInput.send_keys("bamboo")

riddleButton = driver.find_element_by_css_selector("button#r2Butn")
riddleButton.click()

#The Two Merchants 

richiestMerchantInput = driver.find_element_by_id("r3Input")
richiestMerchantInput.send_keys("Jessica")

richiestMerchantButton = driver.find_element_by_css_selector("button#r3Butn")
richiestMerchantButton.click()
checkAnswerButton = driver.find_element_by_id("checkButn")
checkAnswerButton.click()

script = "alert('Trial Complete....Congratulation <Ksanchez>')"
driver.execute_async_script(script)