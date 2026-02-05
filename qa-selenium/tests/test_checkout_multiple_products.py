#Ejecutar caso de prueba

import pytest
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.driver_factory import get_driver

def close_alert_if_present(driver):
    """Cierra cualquier alerta presente"""
    try:
        alert = Alert(driver)
        alert.accept()
        return True
    except NoAlertPresentException:
        return False

@pytest.mark.e2e

def test_checkout_multiple_products():
    """
    Escenario end-to-end:
    - Login
    - Agregar varios productos
    - Ir al carrito
    - Checkout completo
    - Finalizar compra
    - Volver al home
    """

    # Obtener driver
    driver = get_driver(headless=False)
    
    try:
        # ---------- LOGIN ----------
        login_page = LoginPage(driver)
        login_page.open()
        close_alert_if_present(driver)
        login_page.login("standard_user", "secret_sauce")
        close_alert_if_present(driver)

        # ---------- INVENTORY ----------
        inventory_page = InventoryPage(driver)

        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt"
        ]

        for product in products:
            inventory_page.add_product_by_name(product)
            close_alert_if_present(driver)

        # Validar badge del carrito
        assert inventory_page.get_cart_badge_count() == len(products)

        inventory_page.go_to_cart()
        close_alert_if_present(driver)

        # ---------- CART ----------
        cart_page = CartPage(driver)
        cart_page.verify_products_in_cart(products)
        cart_page.click_checkout()
        close_alert_if_present(driver)

        # ---------- CHECKOUT ----------
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information(
            first_name="Mariano",
            last_name="QA",
            postal_code="12345"
        )

        checkout_page.continue_checkout()
        close_alert_if_present(driver)
        checkout_page.finish_checkout()
        close_alert_if_present(driver)

        # ---------- ASSERT FINAL ----------
        assert checkout_page.is_checkout_complete()

        checkout_page.back_to_home()
    finally:
        driver.quit()
