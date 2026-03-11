import os
import time
import pytest

from Pages.search_flights_page import SearchFlightsPage
from Pages.flight_filter_page import FlightFiltersPage
from Pages.book_flight_page import BookFlightPage
from Pages.booking_details_page import BookingDetailsPage
from Pages.payment_page import PaymentPage
from Pages.invoice_page import InvoicePage

from Utilities.excel_details import get_booking_data
from Utilities.logger import get_logger


logger = get_logger()

# read data from excel
test_data = get_booking_data("testdata/booking_data.xlsx")


@pytest.mark.parametrize("row", test_data)
def test_travel_booking(driver, row):

    logger.info("Travel Booking Test Started")

    try:

        #SEARCH FLIGHTS

        logger.info("Entering flight search details")

        search_page = SearchFlightsPage(driver)

        search_page.enter_departure_city(row)
        logger.info("Departure city selected")

        search_page.enter_arrival_city(row)
        logger.info("Arrival city selected")
        search_page.select_departure_date(row)
        logger.info("Departure date selected")
        search_page.select_trip_type(row)
        logger.info("Trip type selected")
        time.sleep(2)


        search_page.select_return_date(row)
        logger.info("Arrival city selected")
        search_page.add_passengers(row)
        logger.info("Added passengers")

        search_page.click_search()
        logger.info("Searching for flights")

        time.sleep(3)

        assert True

        #APPLY FILTERS

        logger.info("Applying flight filters")

        filters_page = FlightFiltersPage(driver)

        filters_page.apply_stop_filters("roundtrip")

        filters_page.apply_departure_time_filters("roundtrip")

        filters_page.sort_by_departure_time()
        logger.info("Sorted by Departure time")

        time.sleep(2)

        assert True


        #BOOK FLIGHT

        logger.info("Selecting flight")

        book_page = BookFlightPage(driver)

        book_page.book_second_flight()
        logger.info("SBooking flight")

        time.sleep(3)

        assert True


        #BOOKING DETAILS

        logger.info("Entering passenger details")

        booking_page = BookingDetailsPage(driver)

        booking_page.fill_guest_details(row)

        booking_page.fill_passenger_details(row)

        time.sleep(2)

        assert True


        #PAYMENT

        logger.info("Selecting payment method")

        payment_page = PaymentPage(driver)

        payment_page.select_payment_and_confirm()

        time.sleep(3)

        assert True


        #INVOICE

        logger.info("Downloading invoice")

        invoice_page = InvoicePage(driver)

        invoice_page.wait_for_invoice_page()

        invoice_page.download_invoice()

        invoice_page.verify_invoice_downloaded()

        logger.info("Invoice downloaded successfully")

        assert True


        logger.info("Test Completed Successfully")


    except Exception as e:

        logger.error(f"Test Failed : {str(e)}")

        # create screenshots folder if not exists
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot("screenshots/test_failure.png")

        pytest.fail("Test execution failed")