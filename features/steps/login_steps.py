import logging
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:8000/"

@given('the user "admin@upidev.com" exists with password "password123"')
def step_impl(context):
    # Assumes user exists in the FastAPI app statically; no action needed
    pass

@given("I am on the login page")
def step_impl(context):
    context.browser.get(BASE_URL)

@when('I enter email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.browser.find_element(By.NAME, "email").send_keys(email)
    context.browser.find_element(By.NAME, "password").send_keys(password)

@when("I click the login button")
def step_impl(context):
    context.browser.find_element(By.ID, "submit").click()
    time.sleep(5)


@then(u'I should be redirected to the dashboard')
def step_impl(context):

    assert "/dashboard" in context.browser.current_url, "Not redirected to dashboard"

@then(u'I should see a welcome message with my username')
def step_impl(context):
    page_text = context.browser.page_source
    assert "Welcome" in page_text and "admin" in page_text, "Welcome message not found"


@when(u'I enter username "admin@upidev.com" and password "wrongpass"')
def step_impl(context):
    context.browser.find_element(By.NAME, "email").clear()
    context.browser.find_element(By.NAME, "email").send_keys("admin@upidev.com")
    context.browser.find_element(By.NAME, "password").clear()
    context.browser.find_element(By.NAME, "password").send_keys("wrongpass")


@then(u'I should see an error message saying "Invalid username or password"')
def step_impl(context):
    time.sleep(3)
    error_message = context.browser.find_element(By.TAG_NAME, "body").text
    assert "Invalid username or password" in error_message, "Expected error message not shown"


@given(u'I am logged in as "admin@upidev.com"')
def step_impl(context):
    # Adjust this if the actual username is "admin" instead of an email
    context.browser.get(BASE_URL)
    context.browser.find_element(By.NAME, "email").send_keys("admin@upidev.com")
    context.browser.find_element(By.NAME, "password").send_keys("password123")
    context.browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)
    assert "/dashboard" in context.browser.current_url, "Login failed"


@when(u'I click the logout link')
def step_impl(context):
    logout_link = context.browser.find_element(By.LINK_TEXT, "Logout")
    logout_link.click()
    time.sleep(10)


@then(u'I should be redirected to the login page')
def step_impl(context):
    assert context.browser.current_url == BASE_URL, "Not redirected to login page"


@then(u'I should no longer have access to the dashboard')
def step_impl(context):
    context.browser.get(f"{BASE_URL}dashboard")
    time.sleep(1)
    assert context.browser.current_url == BASE_URL, "Still has access to dashboard after logout"


def after_all(context):
    context.browser.quit()