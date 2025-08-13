from selenium.webdriver.common.by import By
import pytest
from src.pages.Base_Page import BasePage


class SanboxPage(BasePage):

    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)
