from selenium import webdriver
from selenium.webdriver.common.by import By
import meraki
import os
import dotenv
import logging
import csv

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
dotenv.load_dotenv()

dashboard = meraki.DashboardAPI()
driver = webdriver.Chrome()

# List to store organization IDs
orgs_list = []


def append_on_file(org, name, serial, retention_days):
    """
    Append the camera serial and retention days to a file.
    """
    with open("camera_retention.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([org, name, serial, retention_days])
    logging.info(
        f"Appended {serial} with retention days {retention_days} to CSV file.")


def login_meraki_webpage(username, password):
    # First page: Insert username info
    try:
        text_box = driver.find_element(by=By.NAME, value="email")
        submit_button = driver.find_element(
            By.XPATH, "//button[normalize-space(text())='Next']")
        text_box.send_keys(username)
        submit_button.click()
    except Exception as e:
        logging.error(f"Error finding elements on the login page: {e}")
        return
    # Wait for the next page to load
    # Cisco Meraki login page elements
    #! Comment this part of the (bellow try-except) code if you are not using a cisco e-mail (ex.: lucas@cisco.com)
    try:
        signin_personal_button = driver.find_element(
            By.XPATH, "//button[normalize-space(text())='Sign in to personal account']")
        signin_personal_button.click()

    except Exception as e:
        logging.error(
            f"Error finding elements on the Cisco Meraki login page: {e}")
        return

    # Second page: Insert password info
    try:
        input_password = driver.find_element(
            by=By.CSS_SELECTOR, value="input[type='password']")
        signin_account_button = driver.find_element(
            By.XPATH, "//button[normalize-space(text())='Sign in']")
        # Input the password and click the sign-in button
        input_password.send_keys(password)
        signin_account_button.click()
    except Exception as e:
        logging.error(f"Error finding elements on the password page: {e}")
        return
    # If you are using 2FA, you will need to handle that separately.
    input("Press Enter to continue after completing any 2FA steps...")
    # Wait for the dashboard to load
    logging.info("Login successful, waiting for dashboard to load...")
    return True


def main():
    orgs = dashboard.organizations.getOrganizations()

    for org in orgs:
        print(f"Organization: {org['name']} - ID: {org['id']}")
        orgs_list.append(org['id'])

    # Fetch all cameras from all organizations
    camera_serial_list = []
    info_cam = {}
    for org in orgs_list:
        try:
            logging.info(f"Fetching cameras for organization ID: {org}")
            cameras = dashboard.organizations.getOrganizationInventoryDevices(
                org)
            for camera in cameras:
                if camera['model'].startswith('MV'):
                    camera_serial_list.append(camera['serial'])
                    info_cam[camera['serial']] = {
                        'name': camera['name'],
                        'ORG': org,
                        'model': camera['model'], }
        except meraki.APIError as e:
            logging.error(
                f"Error fetching cameras for organization {org}: {e}")

    video_url_dic = {}
    for serial in camera_serial_list:
        try:
            # Fetch the video URL for each camera
            logging.info(f"Fetching video URL for camera serial: {serial}")
            video_url_dic[serial] = dashboard.camera.getDeviceCameraVideoLink(serial)[
                'url']
        except meraki.APIError as e:
            logging.error(f"Error fetching video URL for camera {serial}: {e}")

    # Open the Meraki login page
    driver.get("https://account.meraki.com/login/")
    driver.implicitly_wait(0.5)

    # Login to the Meraki dashboard
    # If you are using 2FA, you will need to handle that separately.
    login_successful = login_meraki_webpage(os.getenv("MERAKI_USERNAME"),
                                            os.getenv("MERAKI_PASSWORD"))
    if login_successful:
        logging.info("Login successful, proceeding to fetch camera data...")
        # Iterate through the video URLs and open each one
        for serial, url in video_url_dic.items():
            retention_days = None
            try:
                driver.get(f"{url}/settings/qualityRetention")
                logging.info(f"Opened video URL: {url}")
            except Exception as e:
                logging.error(f"Error opening video URL {url}: {e}")
            # Try to get the camera rentention Days
            try:
                retention_days = driver.find_element(
                    By.CLASS_NAME, "retentionDays").text
                logging.info(
                    f"Camera {serial} retention days: {retention_days}")
            except Exception as e:
                retention_days = None
                append_on_file(serial, retention_days)
                logging.error(
                    f"Error fetching retention days for camera {serial}: {e}")
            if retention_days is not None:
                append_on_file(
                    info_cam[serial]['ORG'], info_cam[serial]['name'], serial, retention_days)
    else:
        logging.error("Login failed, exiting script.")
        driver.quit()
        exit(1)

    driver.quit()
    logging.info("Script completed successfully.")


if __name__ == "__main__":
    logging.info("Running as main script.")
    main()
