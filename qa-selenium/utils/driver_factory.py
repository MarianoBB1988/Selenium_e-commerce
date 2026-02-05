from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_driver(headless=False):
    options = Options()

    # 🧠 Headless opcional
    if headless:
        options.add_argument("--headless=new")

    # 🖥️ Estabilidad visual
    options.add_argument("--start-maximized")
    
    # 🕵️ Modo incógnito - evita gestor de contraseñas
    options.add_argument("--incognito")

    # 🚫 Eliminar banners de automatización
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # 🔒 Desactivar gestor de contraseñas DEFINITIVO
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.notifications": 2,
        "autofill.enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    # 🚫 Quitar overlays y notificaciones
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-password-manager")
    options.add_argument("--disable-credential-manager")

    # 🛡️ Flags de estabilidad
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 🔐 Deshabilitar todos los servicios de sincronización
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-breakpad")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(5)
    
    # Ejecutar script para deshabilitar notificaciones del navegador
    try:
        driver.execute_script("""
            if (window.Notification) {
                window.Notification.permission = 'denied';
                window.Notification = function() {};
            }
        """)
    except:
        pass

    return driver
