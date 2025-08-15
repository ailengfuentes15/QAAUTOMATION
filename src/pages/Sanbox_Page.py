from selenium.webdriver.common.by import By
import pytest
from src.pages.Base_Page import BasePage


class SanboxPage(BasePage):

    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")


    DYNAMIC_BUTTON = (By.CLASS_NAME, "btn-primary")

    HIDDEN_TEXT_LABEL = (
        By.XPATH,
        "//p[@id='hidden-element']",
    )



    def navigate_sanbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)

    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_BUTTON)

    def select_checkbox_with_label(self, label_text):
        checkbox_locator = (
            By.XPATH,
            f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']",
        )
        self.select_element(checkbox_locator)
