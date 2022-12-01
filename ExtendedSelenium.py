import logging
from RPA.Browser.Selenium import Selenium
from robot.api.deco import keyword
from selenium.webdriver.common.action_chains import ActionChains


class ExtendedSelenium(Selenium):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @keyword
    def click_coordinates(self, x: int, y: int):
        ActionChains(self.driver).move_by_offset(x, y).click().perform()

    @keyword
    def click_region(self, region):
        x_coord = region.left + int((region.right - region.left) / 2)
        y_coord = region.top + int((region.bottom - region.top) / 2)
        logging.info(f"Clicking region middle: {x_coord}, {y_coord}")
        self.click_coordinates(x_coord, y_coord)
