from selenium.webdriver.common.by import By

locator = {
	"contact_us_button": (By.ID, "contact-link"),
	"subject_handling_menu": (By.ID, "id_contact"),
	"email_field": (By.ID, "email"),
	"order_reference_field": (By.ID, "id_order"),
	"message_field": (By.ID, "message"),
	"send_button": (By.ID, "submitMessage"),
	"alert_message": (By.XPATH, "/html/body/div/div[2]/div/div[3]/div/p")
}
