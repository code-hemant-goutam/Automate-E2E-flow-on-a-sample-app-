import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright
        
        
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser=playwright_instance.chromium.launch(headless=True,slow_mo=2000)
    yield browser
    browser.close()
    
@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context(record_video_dir="videos/")
    page=context.new_page()
    yield page
    context.close()