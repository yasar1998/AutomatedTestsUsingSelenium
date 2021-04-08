from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('datafortest.csv') as csvfile:
	csvreader = reader(csvfile, delimiter=';')
	for row in csvreader:
		assert driver.find_element(*locator["contact_us_button"]).is_displayed()
		driver.find_element(*locator["contact_us_button"]).click()

		select = Select(driver.find_element(*locator["subject_handling_menu"]))
		select.select_by_visible_text(row[0])
		
		driver.find_element(*locator["email_field"]).send_keys(row[1])

		driver.find_element(*locator["order_reference_field"]).send_keys(row[2])

		driver.find_element(*locator["message_field"]).send_keys(row[3])

		driver.find_element(*locator["send_button"]).click()

		assert driver.find_element(*locator["alert_message"]).is_displayed()
		assert "Your message has been successfully sent to our team." == driver.find_element(*locator["alert_message"]).text

driver.quit()
