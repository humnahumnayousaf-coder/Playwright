import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import Loginpage
from pages.orange_home_page import Homepage


def test_example(page: Page) -> None:
    
     login_page = Loginpage(page)
     home_page = Homepage(page)
     
     login_page.enter_username("admin")
     login_page.enter_password("admin123")
     login_page.click_login()
    
     expect(home_page.is_upgrade_button_visible()).to_be_true()
     home_page.click_dashboard()
     
