import logging
import time

from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()  # Or Firefox
    context.browser.get("http://127.0.0.1:8000")
    logging.warning(context.__dict__)
    time.sleep(5)  # Or Firefox