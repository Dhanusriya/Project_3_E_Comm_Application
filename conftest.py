import pytest
from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot

@pytest.fixture()
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            Screenshot.capture(driver,item.name)