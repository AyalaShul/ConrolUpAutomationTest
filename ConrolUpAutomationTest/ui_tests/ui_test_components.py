from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITestComponents:

    driver = ''

    def setup(self):
        """
         Setup driver
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")


    def login(self, username, password):
        """
         Login using username and password, insert them and click login button.
        :param username:
        :param password:
        """
        username_element = self.driver.find_element(by=By.ID, value="user-name")
        password_element = self.driver.find_element(by=By.ID, value="password")

        username_element.send_keys(username)
        username_value = username_element.get_attribute("value")
        assert username_value == username

        password_element.send_keys(password)
        password_value = password_element.get_attribute("value")
        assert password_value == password

        signin_btn = self.driver.find_element(by=By.ID, value="login-button")
        signin_btn.click()

    def wait_for_new_page(self, wait_for_element_id):
        """
         Wait until success to get element from the new page
        :param wait_for_element_id: element's id from the new page
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, wait_for_element_id)))

    def get_element_by_class(self, class_name):
        """
         Find element by class name
        :param class_name: element's class name
        :return: element
        """
        return self.driver.find_element(by=By.CLASS_NAME, value=class_name)

    def get_elements_by_class(self, class_name):
        """
         Find elements by class name
        :param class_name: elements class name
        :return: list of elements
        """
        return self.driver.find_elements(by=By.CLASS_NAME, value=class_name)

    def quit_driver(self):
        """
         Quit the driver
        """
        self.driver.quit()
