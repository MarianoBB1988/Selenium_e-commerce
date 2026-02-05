from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object del carrito de compras
    https://www.saucedemo.com/cart.html
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_products_in_cart(self, expected_products):
        """
        Verifica que los productos esperados estén en el carrito
        """
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        cart_product_names = [item.text for item in items]

        for product in expected_products:
            assert product in cart_product_names, f"{product} no está en el carrito"

    def click_checkout(self):
        """Hace click en el botón Checkout"""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
