import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class SearchFlightsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # wait for page loader to disappear
        self.wait.until(
            EC.invisibility_of_element_located((By.ID, "page-loader"))
        )

    # LOCATORS

    departure_input = (By.XPATH, "//input[@placeholder='Departure City or Airport']")
    arrival_input = (By.XPATH, "//input[@id='arrival_airport_input']")

    trip_dropdown = (By.XPATH, "(//span[contains(text(),'expand_more')])[11]")

    one_way = (By.XPATH, "//span[normalize-space()='One Way']")
    round_trip = (By.XPATH, "//span[normalize-space()='Round Trip']")

    passenger_box = (By.XPATH, "(//span[contains(text(),'expand_more')])[13]")

    add_adult_btn = (By.XPATH, "(//span[contains(text(),'add')])[5]")

    return_input = (By.XPATH, "//input[@placeholder='Return Date']")

    search_btn = (By.XPATH, "//button[contains(.,'Search Flights')]")

    flight_results = (By.XPATH, "//button[contains(.,'Book Now')]")

    # ENTER DEPARTURE CITY

    def enter_departure_city(self, row):

        city = row["FromCity"]

        field = self.wait.until(
            EC.element_to_be_clickable(self.departure_input)
        )

        field.clear()
        field.send_keys(city[:3])

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(text(),'{city}')]")
            )
        )

        option.click()

    # ENTER ARRIVAL CITY

    def enter_arrival_city(self, row):

        city = row["ToCity"]

        field = self.wait.until(
            EC.element_to_be_clickable(self.arrival_input)
        )

        field.clear()
        field.send_keys(city[:3])

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(text(),'{city[:3].upper()}')]")
            )
        )

        option.click()

    # SELECT TRIP TYPE

    def select_trip_type(self, row):

        trip_type = row["TripType"]

        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.trip_dropdown)
        )

        dropdown.click()

        if trip_type.lower() == "roundtrip":

            option = self.wait.until(
                EC.element_to_be_clickable(self.round_trip)
            )

        else:

            option = self.wait.until(
                EC.element_to_be_clickable(self.one_way)
            )

        option.click()

    # SELECT DEPARTURE DATE

    def select_departure_date(self, row):

        dep_day = str(row["DepartureDate"])

        date = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//td/div[text()='{dep_day}']")
            )
        )

        self.driver.execute_script("arguments[0].click();", date)

        self.driver.find_element(By.TAG_NAME, "body").click()

    #SELECT RETURN DATE

    def select_return_date(self, row):

        # skip return date if one way
        if str(row["TripType"]).lower() == "oneway":
            print("One way trip → skipping return date")
            return

        ret_day = str(row["ReturnDate"])

        field = self.wait.until(
            EC.element_to_be_clickable(self.return_input)
        )

        field.click()

        date = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[text()='{ret_day}'])[2]")
            )
        )

        self.driver.execute_script("arguments[0].click();", date)

        self.driver.find_element(By.TAG_NAME, "body").click()

    #ADD PASSENGERS

    def add_passengers(self, row):

        passenger_count = int(row["Passengers"])

        add_clicks = passenger_count - 1

        passenger = self.wait.until(
            EC.element_to_be_clickable(self.passenger_box)
        )

        passenger.click()

        for i in range(add_clicks):

            add_btn = self.wait.until(
                EC.element_to_be_clickable(self.add_adult_btn)
            )

            add_btn.click()

        self.driver.find_element(By.TAG_NAME, "body").click()

    #CLICK SEARCH

    def click_search(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.search_btn)
        )

        button.click()

        # wait until flights appear
        self.wait.until(
            EC.presence_of_all_elements_located(self.flight_results)
        )