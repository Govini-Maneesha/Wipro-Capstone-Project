from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    pay_later_option = (By.XPATH, "//div[contains(text(),'Pay Later')]")
    terms_checkbox = (By.XPATH, "//label[contains(text(),'I agree')]")
    confirm_button = (By.XPATH, "//span[normalize-space()='Confirm Booking']")

    def select_payment_and_confirm(self):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

        pay_later = self.wait.until(
            EC.element_to_be_clickable(self.pay_later_option)
        )

        self.driver.execute_script("arguments[0].click();", pay_later)

        terms = self.wait.until(
            EC.element_to_be_clickable(self.terms_checkbox)
        )

        self.driver.execute_script("arguments[0].click();", terms)

        confirm = self.wait.until(
            EC.element_to_be_clickable(self.confirm_button)
        )

        self.driver.execute_script("arguments[0].click();", confirm)