from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Target URL
driver.get("https://github.com/kristinca/")
driver.set_window_size(1532, 820)
driver.find_element(By.CSS_SELECTOR, ".mb-3:nth-child(1) .repo").click()
driver.find_element(By.LINK_TEXT, "hello-world").click()

# print(driver.title)

# get text -> from element id
print(driver.find_element(By.ID, "readme").text)

# # Printing the whole body text
# print(driver.find_element_by_xpath("/html/body").text)

# Closing the driver
driver.close()


# get all text from a web page
#
# # WebDriver Chrome
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# # Target URL
# driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
#
# # print(driver.title)
#
# # Printing the whole body text
# print(driver.find_element_by_xpath("/html/body").text)
#
# # Closing the driver
# driver.close()
