from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' not in current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, browser):
        input_mail = browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        input_mail.send_keys(email)
        input_pass1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        input_pass1.send_keys(password)
        input_pass2 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        input_pass2.send_keys(password)
        register_button = browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        register_button.click()
