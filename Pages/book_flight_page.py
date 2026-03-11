from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class BookFlightPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    flights_loaded = (By.XPATH, "//button[contains(.,'Book Now')]")

    def book_second_flight(self):

        flights = self.wait.until(
            EC.presence_of_all_elements_located(self.flights_loaded)
        )

        # check if at least 2 flights exist
        if len(flights) < 2:
            raise AssertionError("Less than 2 flights found in results")

        second_flight = flights[2]

        # scroll to second flight
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            second_flight
        )

        # click Book Now for second flight
        self.driver.execute_script(
            "arguments[0].click();",
            second_flight
        )