import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("banner").get_by_text("AQA POWE23 LastNameTest").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_text("Password", exact=True)).to_be_visible()
    page.get_by_text("Password", exact=True).click()
    page.get_by_text("Password", exact=True).click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_text("Password", exact=True).click()
    page.get_by_text("Password", exact=True).click()
    expect(page.locator("form")).to_contain_text("Password")
    expect(page.get_by_role("textbox", name="Username")).to_be_empty();
