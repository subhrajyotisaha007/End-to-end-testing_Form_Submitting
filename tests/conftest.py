import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

def broswers(name):
    name.implicitly_wait(4)
    name.get("https://rahulshettyacademy.com/angularpractice/")
    name.maximize_window()


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        broswers(driver)

    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        broswers(driver)

    elif browser_name == 'edge':
        driver = webdriver.Edge()
        broswers(driver)

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# @pytest.fixture(params=[('Rahul',"mail@gmail.com",'Male'),("Subhra","mail@yahoo.com", "Male"),("Piu","mail@outlook.com","Female")])
# def getData(request):
#     return request.param