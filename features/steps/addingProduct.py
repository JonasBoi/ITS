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


@then('Two products called "New product" are shown')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Two products called "New product" are shown')


@step('One of products called "New product" has "Disabled" status')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: But One of them has "Disabled" status')


@given("Blank Add Product page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Blank Add Product page is opened')


@when("The blank product is saved")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When The blank product is saved')


@then("The operation is unsuccessful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The operation is unsuccessful')
