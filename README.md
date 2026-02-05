# Selenium E-commerce Testing Project

Un proyecto de automatización de pruebas end-to-end para aplicaciones de e-commerce usando Selenium WebDriver y pytest.

## 📋 Descripción

Este proyecto proporciona una suite de pruebas automatizadas para validar funcionalidades críticas de una plataforma de e-commerce, incluyendo:

- Autenticación de usuarios (Login)
- Navegación y búsqueda de productos (Inventario)
- Gestión del carrito de compras
- Proceso completo de checkout

## 📁 Estructura del Proyecto

```
Selenium_e-commerce/
├── init.py
├── qa-selenium/
│   ├── pages/                          # Page Object Model
│   │   ├── __init__.py
│   │   ├── login_page.py              # Elementos y acciones de login
│   │   ├── inventory_page.py          # Elementos y acciones del inventario
│   │   ├── cart_page.py               # Elementos y acciones del carrito
│   │   └── checkout_page.py           # Elementos y acciones del checkout
│   ├── tests/                          # Test suite
│   │   ├── __init__.py
│   │   └── test_checkout_multiple_products.py
│   ├── utils/                          # Utilidades
│   │   ├── __init__.py
│   │   └── driver_factory.py          # Gestor del WebDriver
│   ├── pytest.ini                      # Configuración de pytest
│   └── requirements.txt                # Dependencias
└── README.md
```

## 🛠️ Requisitos

- Python 3.x
- pip (gestor de paquetes)
- Navegador web (Chrome, Firefox, etc.)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/MarianoBB1988/Selenium_e-commerce.git
cd Selenium_e-commerce
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r qa-selenium/requirements.txt
```

## 🚀 Ejecución

### Ejecutar todos los tests

```bash
cd qa-selenium
pytest
```

### Ejecutar tests con salida detallada

```bash
cd qa-selenium
pytest -v
```

### Ejecutar un archivo de prueba específico

```bash
cd qa-selenium
pytest tests/test_checkout_multiple_products.py -v
```

### Ejecutar un test específico

```bash
cd qa-selenium
pytest tests/test_checkout_multiple_products.py::nombre_del_test -v
```

## 📖 Estructura del Código

### Page Object Model (POM)

El proyecto implementa el patrón **Page Object Model** para mantener el código limpio y reutilizable:

- **login_page.py**: Define elementos y métodos de la página de login
- **inventory_page.py**: Define elementos y métodos de la página de inventario
- **cart_page.py**: Define elementos y métodos del carrito
- **checkout_page.py**: Define elementos y métodos del checkout

### Driver Factory

El archivo `driver_factory.py` gestiona la creación y configuración del WebDriver, facilitando la compatibilidad con diferentes navegadores.

## 🧪 Tests Disponibles

### test_checkout_multiple_products.py
Pruebas para validar el flujo completo de compra de múltiples productos:
- Login en la aplicación
- Selección de productos del inventario
- Agregación de productos al carrito
- Proceso de checkout y validación

## 🔧 Configuración

El archivo `pytest.ini` contiene la configuración específica de pytest para el proyecto. Puedes modificarlo según tus necesidades.

## 📝 Notas Importantes

- Asegúrate de que los selectores CSS/XPath en los archivos de páginas coincidan con la estructura actual de la aplicación web
- Los navegadores se descargan automáticamente gracias a `webdriver-manager`
- Se recomienda usar un entorno virtual para evitar conflictos de dependencias

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

**Autor**: Mariano BB  
**GitHub**: [MarianoBB1988](https://github.com/MarianoBB1988)  
**Repositorio**: [Selenium_e-commerce](https://github.com/MarianoBB1988/Selenium_e-commerce)

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.

---

**Última actualización**: Febrero 2026
