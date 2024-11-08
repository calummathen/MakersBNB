from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository

"""
Testing Signup
Successful signup
As well as a few incorrect tries
Also the login navigation button
"""

def test_sign_up_page(db_connection, page, test_web_address):
    db_connection.seed('seeds/extensive_database.sql')
    page.goto(f"http://{test_web_address}/signup")

    title_element = page.locator('h1')
    expect(title_element).to_have_text('Sign Up')

    page.fill("input[name='name']", 'Cezary')
    page.fill("input[name='email']", 'Cezary@gmail.com')
    page.fill("input[name='phone_number']", '07710164198')
    page.fill("input[name='username']", 'Chequers')
    page.fill("input[name='password']", 'Chequers1')
    page.click("text='Submit'")

    repository = UserRepository(db_connection )

    user = repository.find_user(9)
    assert user.name == 'Cezary'
    assert user.username == 'Chequers'
    assert user.phone_number == '07710164198'
    assert user.email == 'Cezary@gmail.com'

    second_title = page.locator('h1')
    expect(second_title).to_have_text('Log In')

def test_sign_up_page_with_no_name_details(db_connection, page, test_web_address):
    db_connection.seed('seeds/extensive_database.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name='name']", ' ')
    page.fill("input[name='email']", 'Cezary@gmail.com')
    page.fill("input[name='phone_number']", '07710164198')
    page.fill("input[name='username']", 'Chequers')
    page.fill("input[name='password']", 'Chequers1')
    page.click("text='Submit'")
    error_message = page.locator('.error-message')
    expect(error_message).to_have_text('Name must be 1-30 characters and not empty.')

def test_sign_up_page_with_user_that_exists(db_connection, page, test_web_address):
    db_connection.seed('seeds/extensive_database.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name='name']", 'user_1')
    page.fill("input[name='email']", 'Cezary@gmail.com')
    page.fill("input[name='phone_number']", '07711111111')
    page.fill("input[name='username']", 'username_1')
    page.fill("input[name='password']", 'password_1')
    page.click("text='Submit'")

    error_messages = page.locator('.error-message')
    expected_errors = [
        'Name must not contain numbers.',
        'Username must be unique and 2-17 characters long with no spaces.'
    ]

    expect(error_messages).to_have_text(expected_errors)
    page.click("text='Login'")

    second_title = page.locator('h1')
    expect(second_title).to_have_text('Log In')    
    

"""
Testing the login Page
Successful Login
Failed Login
Navigation back to the Signup Page
"""

def test_login_page(db_connection, page, test_web_address):
    page.fill("input[name=username]", 'username_1')
    page.fill("input")







