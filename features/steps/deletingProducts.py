from features.steps import viewProducts

from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import re


def del_item(driver, del_all):

    if not del_all:
        # check checkbox
        elem = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//tbody/tr/td/input")))
        elem.click()

    # delete
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-danger"))).click()
    # accept alert
    WebDriverWait(driver, 3).until(ec.alert_is_present(), "no alert")
    alert = driver.switch_to.alert
    alert.accept()


@when('Product "{name}" is deleted')
def step_impl(context, name):
    # //tbody/tr/td/input ---first
    # //td/input ---all
    # .btn-danger ---delete
    driver = context.response

    del_item(driver, False)

    # ------- test-cleanup -------
    viewProducts.step_search(context, "New product")
    del_item(driver, False)


@then('Product "{name}" doesnt exist anymore')
def step_impl(context, name):
    viewProducts.step_search(context, name)

    viewProducts.step_no_res(context)


# noinspection DuplicatedCode
@step('Products with quantity of "{count}" exist')
def step_impl(context, count):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-quantity")))
    elem.clear()
    elem.send_keys(count)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "button-filter")))
    elem.click()

    # assert we get some results
    src = driver.page_source
    found = re.search("No results!", src)

    assert not found


@when('All products with the quantity of "{count}" are deleted')
def step_impl(context, count):
    driver = context.response

    # check checkbox - all
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//td/input"))).click()

    del_item(driver, True)


# noinspection DuplicatedCode
@then('No products with the quantity of "{count}" exist in the store')
def step_impl(context, count):
    driver = context.response

    # search for quantity
    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-quantity")))
    elem.clear()
    elem.send_keys(count)

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "button-filter")))
    elem.click()

    # assert we get no results
    src = driver.page_source
    found = re.search("No results!", src)

    assert found


@when("No products are selected and deleted")
def step_impl(context):
    driver = context.response

    # save old count
    old_text = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//div[2]/div[2]/div[2]")))

    pom = old_text.text.split(" ")
    old_prod_count = pom[5]

    # no selection
    # delete
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-danger"))).click()
    # accept alert
    WebDriverWait(driver, 3).until(ec.alert_is_present(), "no alert")
    alert = driver.switch_to.alert
    alert.accept()

    # save driver and old_prod_count
    new_list = [driver, old_prod_count]
    context.response = new_list


@then("The product count remains the same")
def step_impl(context):
    driver = context.response[0]
    old_prod_count = context.response[1]

    new_text = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//div[2]/div[2]/div[2]")))

    new_prod_count = (new_text.text.split(" "))[5]

    context.response = driver

    assert old_prod_count == new_prod_count
