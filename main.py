import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = YOUR_INSTAGRAM_USERNAME
PASSWORD = YOUR_INSTAGRAM_PASSWORD
SIMILAR_ACCOUNT = INSTAGRAM_ACCOUNT_YOU_WANT_TO_FOLLOW_USERNAME
LOGIN_URL = INSTAGRAM_LOGIN_URL

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class InstaFollower:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def login(self):
        self.driver_path.get(LOGIN_URL)
        time.sleep(8)
        username = self.driver_path.find_element(By.NAME, "username")
        password = self.driver_path.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        save_info = self.driver_path.find_element(By.CSS_SELECTOR, 'button._acap')
        if save_info:
            save_info.click()

        time.sleep(12)
        not_now = self.driver_path.find_element(By.CSS_SELECTOR, 'button._a9_1')
        if not_now:
            not_now.click()

    def find_followers(self):
        time.sleep(5)
        self.driver_path.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver_path.find_element(By.XPATH, '//*[contains(text(), "followers")]')
        followers.click()

        time.sleep(3)
        modal = self.driver_path.find_element(By.XPATH, '//div[starts-with(@class, "_aano")]')

        # for i in range(10):
        #     self.driver_path.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(3)

    def follow(self):
        time.sleep(2)
        buttons = self.driver_path.find_elements(By.CSS_SELECTOR, 'button._acan')

        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver_path.find_element(By.CSS_SELECTOR, 'button._a9_1')
                cancel_button.click()


bot = InstaFollower(driver)
bot.login()
bot.find_followers()
bot.follow()


