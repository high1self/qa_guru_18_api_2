import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope='session')
def demoshop():
    return BaseSession(os.getenv("API_URL"))


@pytest.fixture(scope='session')
def reqres():
    return BaseSession(os.getenv("REQ_URL"))


@pytest.fixture(scope='session')
def browser_config(demoshop):
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demoshop.post(
        "login", json={"Email": os.getenv("LOGIN"), "Password": os.getenv("PASSWORD")}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    return browser
