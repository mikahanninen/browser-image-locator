from ExtendedSelenium import ExtendedSelenium
from RPA.recognition import templates
from time import sleep
import os

WEB = ExtendedSelenium()

IMAGE_DIR = os.path.join(os.getenv("ROBOT_ROOT"), "images")
ARTIFACT_DIR = os.getenv("ROBOT_ARTIFACTS")
IMAGE_OF_PAGE = os.path.join(ARTIFACT_DIR, "webpage.png")
IMAGE_OF_MARK = os.path.join(IMAGE_DIR, "mark_monkey.png")
IMAGE_AFTER = os.path.join(ARTIFACT_DIR, "after_click.png")


def main():
    #
    WEB.open_available_browser(
        "https://robocorp.com/portal/robot/robocorp/template-python",
        headless=True,
        maximized=True,
    )
    # resolution on my Windows 11 & on Cloud Container seems both be 1440x900
    print(WEB.get_window_size())
    # taking base image of the web page for image comparison
    WEB.screenshot(filename=IMAGE_OF_PAGE)
    # finding template image in the base image of the webpage
    # lets find mark the monkey image on the top left to get back to the
    # main page of the Portal
    regions = templates.find(IMAGE_OF_PAGE, IMAGE_OF_MARK, confidence=40.0)
    if len(regions) == 1:
        # region contains left, top, right, bottom coordinates - clicking center
        # of those
        WEB.click_region(regions[0])
    # this is for leaving time for page load
    sleep(2.0)
    # capture proof of the page transition
    WEB.screenshot(filename=IMAGE_AFTER)


if __name__ == "__main__":
    main()
