from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object del proceso de Checkout
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information(self, first_name, last_name, postal_code):
        """
        Completa el formulario del checkout
        """
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_checkout(self):
        """Continúa al resumen de compra"""
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def finish_checkout(self):
        """Finaliza la compra"""
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def is_checkout_complete(self):
        """Verifica que la compra se haya completado"""
        header = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return "Thank you for your order" in header.text

    def back_to_home(self):
        """Vuelve a la pantalla principal"""
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME_BUTTON)).click()
