import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    yield driver
    driver.quit()


def test_click_y_assert(browser):
    wait = WebDriverWait(browser, 5)

    # Identificar botón usando class name con espera explícita
    boton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))


    boton.click()


    print(boton.text)

    # 3) Espera explícita de hasta 5 segundos para que aparezca el otro elemento

    otro_elemento = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#hidden-element")
        )
    )

    # 4) Assert sobre el texto del otro elemento
    texto_esperado = "OMG, aparezco después de 3 segundos de haber hecho click en el botón 👻."

    assert otro_elemento.text == texto_esperado

def test_basic_text(browser):

    # Identificar el elemento de texto básico usando su XPATH
    texto_elemento = browser.find_element(By.XPATH, "//input[@id='formBasicText']")
    texto_elemento.clear()
    # Escribir un texto en el elemento

    texto_elemento.send_keys("¡Hola, soy un texto básico!")
    time.sleep(3)

    # Assert sobre el texto del elemento
    assert texto_elemento.get_attribute("value") == "¡Hola, soy un texto básico!"

def test_checkbox(browser):
    # Identificar el checkbox usando su XPATH
    checkbox = browser.find_element(By.XPATH, "//input[@id='checkbox-0']")

    # Marcar el checkbox
    checkbox.click()

    assert checkbox.is_selected(), "El checkbox debería estar marcado después de hacer click"

    time.sleep(3)

def test_checkbox_both(browser):
    # Identificar ambos checkboxes usando su XPATH
    checkbox1 = browser.find_element(By.XPATH, "//input[@id='checkbox-2']")
    checkbox2 = browser.find_element(By.XPATH, "//input[@id='checkbox-3']")

    # Marcar ambos checkboxes
    checkbox1.click()
    checkbox2.click()

    assert checkbox1.is_selected(), "El primer checkbox debería estar marcado después de hacer click"
    assert checkbox2.is_selected(), "El segundo checkbox debería estar marcado después de hacer click"

    time.sleep(3)

def test_radio(browser):
    # Identificar el radio button usando su XPATH
    radio_button = browser.find_element(By.XPATH, "//input[@id='formRadio2']")

    # Marcar el radio button
    radio_button.click()

    assert radio_button.is_selected(), "El radio button debería estar seleccionado después de hacer click"

    time.sleep(3)


def test_dropdown(browser):
    # Esperar a que el dropdown sea clickeable
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='formBasicSelect']"))
    )
    dropdown.click()

    # Esperar a que las opciones sean visibles
    opciones = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "option"))
    )

    time.sleep(3)

    # Buscar la opción "Tennis" y hacer click
    for opcion in opciones:
        if opcion.text.strip() == "Tennis":
            opcion.click()
            break

    # Assert sobre la opción seleccionada
    assert dropdown.get_attribute("value") == "Tennis", \
        "La opción seleccionada debería ser 'Tennis'"


def test_popup(browser):
    wait = WebDriverWait(browser, 10)

    # Esperar el botón y movernos hacia él
    btn_mostrar_popup = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Mostrar popup']"))
    )
    ActionChains(browser).move_to_element(btn_mostrar_popup).perform()
    btn_mostrar_popup.click()

    # Esperar el mensaje y movernos hacia él
    mensaje_popup = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='¿Viste? ¡Apareció un Pop-up!']"))
    )
    ActionChains(browser).move_to_element(mensaje_popup).perform()

    assert mensaje_popup.is_displayed(), "El popup debería estar visible después de hacer click"
