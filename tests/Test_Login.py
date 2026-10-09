from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_exitoso():
    driver = webdriver.Chrome()

    # Abrir la página de inicio de sesión
    driver.get("https://saucedemo.com/")

    #Ingresar las credenciales de inicio de sesión y guardar variables
    usuario = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")

    #Completar los campos de usuario y contraseña
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    #Hacer clic en el botón de inicio de sesión
    boton_login.click()

    #Validar URL después del login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    #Esperar y cerrar navegador
    time.sleep(2)
    driver.quit()

def test_login_no_exitoso_wrong_username():
    driver = webdriver.Chrome()

    # Abrir la página de inicio de sesión
    driver.get("https://saucedemo.com/")

    #Ingresar las credenciales de inicio de sesión y guardar variables
    usuario = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")

    #Completar los campos de usuario y contraseña
    usuario.send_keys("wrong_user")
    password.send_keys("secret_sauce")

    #Hacer clic en el botón de inicio de sesión
    boton_login.click()

    #Validar mensaje de error
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

    #Esperar y cerrar navegador
    time.sleep(2)
    driver.quit()

def test_login_no_exitoso_wrong_password():
    driver = webdriver.Chrome()

    # Abrir la página de inicio de sesión
    driver.get("https://saucedemo.com/")

    #Ingresar las credenciales de inicio de sesión y guardar variables
    usuario = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")

    #Completar los campos de usuario y contraseña
    usuario.send_keys("standard_user")
    password.send_keys("wrong_password")

    #Hacer clic en el botón de inicio de sesión
    boton_login.click()

    #Validar mensaje de error
    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

    #Esperar y cerrar navegador
    time.sleep(2)
    driver.quit()
