import os

PROJECT_NAME = "qa-selenium"

structure = {
    "pages": ["__init__.py", "login_page.py"],
    "tests": ["__init__.py", "test_login.py"],
    "utils": ["__init__.py", "driver_factory.py"],
}

files = {
    "requirements.txt": "selenium\npytest\nwebdriver-manager\n",
    "pytest.ini": "[pytest]\naddopts = -v\n",
}

def create_project():
    os.makedirs(PROJECT_NAME, exist_ok=True)

    for folder, folder_files in structure.items():
        folder_path = os.path.join(PROJECT_NAME, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in folder_files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                open(file_path, "w").close()

    for file, content in files.items():
        file_path = os.path.join(PROJECT_NAME, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)

    print("✅ Proyecto QA Selenium creado con éxito")

if __name__ == "__main__":
    create_project()
