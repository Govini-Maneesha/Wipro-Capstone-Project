import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class BookingDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # ---------- BOOKING PAGE LOCATORS ----------

    guest_firstname = (By.XPATH, "//input[@placeholder='Enter First Name']")
    guest_lastname = (By.XPATH, "//input[@placeholder='Enter Last Name']")

    country_code = (By.XPATH, "(//select[@x-model='primary_guest.country_code'])[1]")

    guest_phone = (By.XPATH, "//input[@placeholder='Enter Phone Number']")

    # ---------- METHODS ----------

    def fill_guest_details(self, row):

        # wait until booking page loads
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Booking')]"))
        )

        # ---------- TITLE ----------
        title = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//select)[1]"))
        )
        Select(title).select_by_visible_text(row["Title"])

        # ---------- FIRST NAME ----------
        first = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter First Name']")
        first.clear()
        first.send_keys(row["FirstName"])

        # ---------- LAST NAME ----------
        last = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Last Name']")
        last.clear()
        last.send_keys(row["LastName"])

        # scroll to email section
        self.driver.execute_script("window.scrollBy(0,300)")

        # ---------- EMAIL ----------
        email = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@x-model='primary_guest.email']")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", email
        )

        email.click()
        email.clear()
        email.send_keys(str(row["Email"]))

        # ---------- COUNTRY CODE ----------
        country = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//select[@x-model='primary_guest.country_code'])[1]")
            )
        )

        Select(country).select_by_visible_text("IN +91")

        # ---------- PHONE ----------
        phone = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Phone Number']")
            )
        )

        self.driver.execute_script(
            "arguments[0].value = arguments[1];",
            phone,
            str(row["Phone"])
        )


    def fill_passenger_details(self, row):

        # scroll to passenger section
        self.driver.execute_script("window.scrollBy(0,500)")

        # ---------- LEAD TRAVELER NATIONALITY ----------
        nationality = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//select[contains(@x-model,'nationality')])[1]")
            )
        )
        Select(nationality).select_by_visible_text(row["Nationality"])

        # ---------- LEAD TRAVELER DOB ----------

        dob_day = self.driver.find_element(
            By.XPATH, "//label[contains(text(),'Date of Birth')]/following::select[1]"
        )
        Select(dob_day).select_by_visible_text(str(row["DOB_Day"]).zfill(2))

        dob_month = self.driver.find_element(
            By.XPATH, "//label[contains(text(),'Date of Birth')]/following::select[2]"
        )

        month1 = row["DOB_Month"].strftime("%d %b")
        Select(dob_month).select_by_visible_text(month1)

        dob_year = self.driver.find_element(
            By.XPATH, "//label[contains(text(),'Date of Birth')]/following::select[3]"
        )
        Select(dob_year).select_by_visible_text(str(row["DOB_Year"]))

        # ---------- LEAD TRAVELER PASSPORT ----------
        passport = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//input[@placeholder='6 - 15 Numbers'])[1]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            passport
        )

        passport.clear()
        passport.send_keys(str(row["Passport"]))

        if str(row["Passengers"]) == "1":
            print("Only 1 passenger selected → skipping Traveller 2 details")
            return

            # scroll to traveller 2
        self.driver.execute_script("window.scrollBy(0,400)")

        # ---------- TRAVELLER 2 TITLE ----------
        title2 = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//select[@class='select'])[8]"))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            title2
        )

        Select(title2).select_by_visible_text(str(row["Traveler2Title"]))

        # ---------- TRAVELLER 2 FIRST NAME ----------
        first2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//input[@placeholder='First Name'])[1]")
            )
        )

        first2.clear()
        first2.send_keys(row["Traveler2FirstName"])

        # ---------- TRAVELLER 2 LAST NAME ----------
        last2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//input[@placeholder='Last Name'])[1]")
            )
        )

        last2.clear()
        last2.send_keys(row["Traveler2LastName"])

        # ---------- TRAVELLER 2 NATIONALITY ----------
        nationality2 = self.driver.find_element(
            By.XPATH, "(//select[contains(@x-model,'nationality')])[2]"
        )
        Select(nationality2).select_by_visible_text(row["Traveler2Nationality"])

        # ---------- TRAVELLER 2 DOB ----------

        dob_day2 = self.driver.find_element(
            By.XPATH, "(//label[contains(text(),'Date of Birth')])[2]/following::select[1]"
        )
        Select(dob_day2).select_by_visible_text(
            str(row["Traveler2DOB_Day"]).zfill(2)
        )

        dob_month2 = self.driver.find_element(
            By.XPATH, "(//label[contains(text(),'Date of Birth')])[2]/following::select[2]"
        )

        month2 = row["Traveler2DOB_Month"].strftime("%d %b")
        Select(dob_month2).select_by_visible_text(month2)

        dob_year2 = self.driver.find_element(
            By.XPATH, "(//label[contains(text(),'Date of Birth')])[2]/following::select[3]"
        )
        Select(dob_year2).select_by_visible_text(
            str(row["Traveler2DOB_Year"])
        )

        # ---------- TRAVELER 2 PASSPORT ----------
        passport2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//input[@placeholder='6 - 15 Numbers'])[2]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            passport2
        )

        passport2.clear()
        passport2.send_keys(str(row["Traveler2_Passport"]))
