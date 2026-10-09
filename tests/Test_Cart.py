import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from pages.login_page import LoginPage


def iniciar_sesion(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))


def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()

    try:
        iniciar_sesion(driver)

        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/cart.html")
        )
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
    finally:
        driver.quit()


def test_remover_producto_desde_el_carrito():
    driver = webdriver.Chrome()

    try:
        iniciar_sesion(driver)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))

        remove_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        remove_button.click()

        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
        assert driver.find_element(By.ID, "continue-shopping").is_displayed()
    finally:
        driver.quit()
