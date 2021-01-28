from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.gismeteo.ru")
driver.get_screenshot_as_file("img.png")
driver.quit()

