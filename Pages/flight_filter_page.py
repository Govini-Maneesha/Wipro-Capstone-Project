from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class FlightFiltersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    flights_loaded = (By.XPATH, "//button[contains(.,'Book Now')]")

    outbound_direct = (By.XPATH, "(//span[normalize-space()='Direct'])[1]")
    outbound_one_stop = (By.XPATH, "(//span[normalize-space()='1 Stop'])[1]")

    return_direct = (By.XPATH, "(//span[normalize-space()='Direct'])[2]")
    return_one_stop = (By.XPATH, "(//span[normalize-space()='1 Stop'])[2]")

    outbound_morning = (By.XPATH, "(//div[@class='text-xs text-gray-500'][contains(text(),'06:00 – 12:00')])[1]")
    outbound_afternoon = (By.XPATH, "(//div[@class='text-xs text-gray-500'][contains(text(),'12:00 – 18:00')])[1]")
    outbound_evening = (By.XPATH, "(//div[@class='text-xs text-gray-500'][contains(text(),'18:00 – 24:00')])[1]")


    return_early_morning = (By.XPATH, "(//div[@class='text-xs text-gray-500'][contains(text(),'00:00 – 06:00')])[2]")
    return_morning = (By.XPATH, "(//div[@class='text-xs text-gray-500'][contains(text(),'06:00 – 12:00')])[2]")
    return_afternoon = (By.XPATH, "(//div[@class='text-xs font-semibold text-gray-900 dark:text-gray-100'][normalize-space()='Afternoon'])[2]")

    sort_dropdown = (By.XPATH, "//select[@x-model='sortBy']")

    def apply_stop_filters(self, trip_type):

        self.wait.until(
            EC.presence_of_all_elements_located(self.flights_loaded)
        )

        outbound_direct = self.driver.find_element(*self.outbound_direct)
        self.driver.execute_script("arguments[0].click();", outbound_direct)

        outbound_one = self.driver.find_element(*self.outbound_one_stop)
        self.driver.execute_script("arguments[0].click();", outbound_one)

        if trip_type == "roundtrip":

            return_direct = self.driver.find_element(*self.return_direct)
            self.driver.execute_script("arguments[0].click();", return_direct)

            return_one = self.driver.find_element(*self.return_one_stop)
            self.driver.execute_script("arguments[0].click();", return_one)

        self.driver.execute_script("window.scrollBy(0,600)")

    def apply_departure_time_filters(self, trip_type):

        outbound_morning = self.driver.find_element(*self.outbound_morning)
        self.driver.execute_script("arguments[0].click();", outbound_morning)

        outbound_afternoon = self.driver.find_element(*self.outbound_afternoon)
        self.driver.execute_script("arguments[0].click();", outbound_afternoon)

        outbound_evening = self.driver.find_element(*self.outbound_evening)
        self.driver.execute_script("arguments[0].click();", outbound_evening)

        if trip_type == "roundtrip":

            return_early = self.driver.find_element(*self.return_early_morning)
            self.driver.execute_script("arguments[0].click();", return_early)

            return_morning = self.driver.find_element(*self.return_morning)
            self.driver.execute_script("arguments[0].click();", return_morning)

            return_afternoon = self.driver.find_element(*self.return_afternoon)
            self.driver.execute_script("arguments[0].click();", return_afternoon)

    def sort_by_departure_time(self):

        self.driver.execute_script("window.scrollTo(0,0);")

        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.sort_dropdown)
        )

        select = Select(dropdown)
        select.select_by_value("departure")