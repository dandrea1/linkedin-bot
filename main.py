from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "YOUR PATH"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("YOUR JOB SEARCH CRITERIA URL")

sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(1)
username = driver.find_element_by_id("username")
username.click()
username.send_keys("YOUR USERNAME")
password = driver.find_element_by_id("password")
password.click()
password.send_keys("YOUR PASSWORD")
button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
button.click()
time.sleep(5)


# job = driver.find_element_by_class_name("jobs-search-results__list-item")
# job.click()
# save_button = driver.find_element_by_class_name("jobs-save-button")
# save_button.click()

all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")
for listing in all_listings:
    listing.click()
    time.sleep(5)
    print("sleep")

    try:
        save_button = driver.find_element_by_class_name("jobs-save-button")
        save_button.click()
        time.sleep(5)
        driver.back()
        time.sleep(5)
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
