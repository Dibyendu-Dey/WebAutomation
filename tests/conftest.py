"""
Conftest.py is a centralized fixture available to all Pytest test file.
"""
import pytest

"""Let generalize the browser invocation and pass/select the browser at the run time using Pytest Command line 
Options """

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox or ie"
    )


@pytest.fixture(scope="class")
# the scope of this fixture is set to class that means this will get executed before the instantiation of the class
def setup(request):  # request is an object of the fixture
    """Setup method to invoke the browser"""
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/angularpractice/")