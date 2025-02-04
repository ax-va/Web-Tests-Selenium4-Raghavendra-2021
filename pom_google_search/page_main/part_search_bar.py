from selenium.webdriver.common.by import By

from pom.elements.element_input import ElementInput
from pom.parts.part_base import PartBase


class PartSearchBar(PartBase):
    LOCATOR_FOR_ELEMENT_INPUT = (By.NAME, "q")

    @property
    def element_input(self):
        return ElementInput(self.driver, self.LOCATOR_FOR_ELEMENT_INPUT)

    def is_displayed(self):
        return self.element_input.is_displayed()

    def search_for(self, text):
        self.element_input.send_keys(text).submit()
        return self
