from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Page Object de la pantalla de productos (Inventory)
    """

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_by_name(self, product_name):
        """
        Agrega un producto al carrito buscando por el nombre visible.
        Esto evita usar IDs dinámicos.
        """
        add_button = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )

        self.wait.until(EC.element_to_be_clickable(add_button)).click()

    def go_to_cart(self):
        """Hace click en el icono del carrito"""
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()

    def get_cart_badge_count(self):
        """Devuelve la cantidad de productos en el badge del carrito"""
        return int(self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text)
