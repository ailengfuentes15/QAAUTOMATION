import pytest
from src.pages.Sanbox_Page import SanboxPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.regresion
def test_boton_id_dinamico(sanbox_page):
    sanbox_page.navigate_sanbox()
    sanbox_page.click_boton_id_dinamico()


    # Estamos usando el wait_for_element para esperar que el elemento sea visible
    elemento_texto_oculto = sanbox_page.wait_for_element(
        sanbox_page.HIDDEN_TEXT_LABEL
    )

    # Creamos la variable con el texto esperado y hacemos el assertion
    texto_esperado = (
        "OMG, aparezco después de 3 segundos de haber hecho click en el botón"
    )

    assert (
        texto_esperado in elemento_texto_oculto.text
    ), "El texto esperado no coincide con el texto encontrado"