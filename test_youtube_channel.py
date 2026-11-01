from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@tallavandana")
print(driver.title)
driver.quit()