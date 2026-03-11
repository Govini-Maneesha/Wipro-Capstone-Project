import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class InvoicePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    download_invoice_button = (
        By.XPATH,
        "//div[contains(@class,'btn light')]"
    )

    def wait_for_invoice_page(self):

        self.wait.until(
            EC.visibility_of_element_located(self.download_invoice_button)
        )

    def download_invoice(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.download_invoice_button)
        )

        self.driver.execute_script("arguments[0].click();", button)

        time.sleep(6)

    def verify_invoice_downloaded(self):

        downloads_folder = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        files = os.listdir(downloads_folder)

        invoice_files = [f for f in files if "invoice" in f.lower()]

        assert len(invoice_files) > 0