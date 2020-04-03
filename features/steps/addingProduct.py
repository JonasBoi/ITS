from features.steps import viewProducts

from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import re


@when('A new product "{name}" is created')
def step_impl(context, name):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// div[ @ id = 'content'] / div / div / div / a")))
    elem.click()
    # page loads
    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-name1")))
    elem.send_keys(name)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-meta-title1")))
    elem.send_keys("test")

    elem = driver.find_element_by_xpath("//a[contains(text(),'Data')]")
    elem.click()
    # page loads

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-model")))
    elem.send_keys("test")

    elem = driver.find_element_by_xpath("// div[ @ id = 'content'] / div / div / div / button / i")
    elem.click()


@then('"{name}" is shown in the Product List')
def step_impl(context, name):
    viewProducts.step_search(context, name)

    driver = context.response

    src = driver.page_source
    nothing_found = re.search("No results!", src)

    assert not nothing_found

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//tbody/tr/td[3]")))

    assert re.search(name, elem.text)


@given('The product "{name}" is in the Product List')
def step_impl(context, name):

    driver = context.response
    viewProducts.open_products_from_homepage(driver)

    src = driver.page_source
    found = re.search(name, src)

    assert found


@when('"{name}" is copied')
def step_impl(context, name):
    viewProducts.step_search(context, name)

    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// input[ @ name = 'selected[]']")))
    elem.click()

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// div[ @ id = 'content'] / div / div / div / button / i")))
    elem.click()


@then('Two products called "{name}" are shown')
def step_impl(context, name):
    driver = context.response

    elem1 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// tbody / tr / td[3]")))
    elem2 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// tr[2] / td[3]")))

    assert elem1.text == elem2.text == name


@step('One of the products called "{name}" has "{status}" status')
def step_impl(context, name, status):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-name")))
    elem.clear()

    viewProducts.step_search(context, name)

    elem1 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// tbody / tr / td[7]")))
    elem2 = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//tr[2]/td[7]")))

    assert elem1.text != elem2.text
    assert elem1.text == status or elem2.text == status


@given("Blank Add Product page is opened")
def step_impl(context):
    driver = context.response

    viewProducts.open_products_from_homepage(driver)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "// div[ @ id = 'content'] / div / div / div / a")))
    elem.click()


@when("The blank product is saved")
def step_impl(context):
    driver = context.response

    elem = driver.find_element_by_xpath("// div[ @ id = 'content'] / div / div / div / button / i")
    elem.click()


@then("The operation is unsuccessful")
def step_impl(context):
    driver = context.response
    src = driver.page_source
    found = re.search("Warning: Please check the form carefully for errors!", src)

    if not found:
        assert not re.search("Success: You have modified products!", src)
    else:
        assert found
