from features.steps import viewProducts

from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import re


@given('The product "{name}" exists')
def step_impl(context, name):
    driver = context.response

    viewProducts.open_products_from_homepage(driver)
    viewProducts.step_search(context, name)

    src = driver.page_source
    assert not re.search("No results!", src)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//tbody/tr/td[3]")))

    assert elem.text == name


@when('Its name is changed to "{name}"')
def step_impl(context, name):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "// form[ @ id = 'form-product'] / div / table / tbody / tr / td[8] / a")))
    elem.click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-name1")))
    elem.clear()
    elem.send_keys(name)


@step('The price is set to "{price}"')
def step_impl(context, price):
    driver = context.response

    elem = driver.find_element_by_xpath("//a[contains(text(),'Data')]")
    elem.click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-price")))
    elem.clear()
    elem.send_keys(price)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "// div[ @ id = 'content'] / div / div / div / button / i")))
    elem.click()


@then('The product "{name}" with the price of "{price}" is displayed in the Product List')
def step_impl(context, name, price):

    viewProducts.step_search(context, name)

    driver = context.response

    elem1 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//tbody/tr/td[3]")))
    elem2 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//tbody/tr/td[5]")))

    el_name = elem1.text
    el_price = elem2.text

    assert el_name == name
    assert el_price == price


@given('The status of "{name}" is "{status}"')
def step_impl(context, name, status):
    viewProducts.open_products_from_homepage(context.response)
    viewProducts.step_search(context, name)

    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//tbody/tr/td[7]")))

    assert elem.text == status


@when('the status is edited to "{status}" and saved')
def step_impl(context, status):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "// form[ @ id = 'form-product'] / div / table / tbody / tr / td[8] / a")))
    elem.click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Data')]")))
    elem.click()

    # dropdown
    driver.find_element_by_xpath("//select[@id='input-status']/option[text()='"+status+"']").click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, "// div[ @ id = 'content'] / div / div / div / button / i")))
    elem.click()


@then('"{name}" is not listed in "{status}" products')
def step_impl(context, name, status):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-name")))
    elem.clear()
    elem.send_keys(name)
    driver.find_element_by_xpath("//select[@id='input-status']/option[text()='"+status+"']").click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "button-filter")))
    elem.click()

    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "text-center")))

    src = driver.page_source
    assert re.search("No results!", src)
