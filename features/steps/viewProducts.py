from behave import *

import re

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_products_from_homepage(driver):
    btn = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//li[@id='catalog']/a")))
    btn.click()
    btn = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Products')]")))
    btn.click()


@given("Home page of the admin area is opened")
def step_impl(context):
    driver = context.response

    driver.get("http://mat.fit.vutbr.cz:8096/admin/")
    elem = driver.find_element_by_id("input-username")
    elem.send_keys("admin")
    elem = driver.find_element_by_id("input-password")
    elem.send_keys("admin")
    elem.submit()


@when('The Products category is selected from the menu')
def step_impl(context):
    driver = context.response

    open_products_from_homepage(driver)


@then("The products are shown in the Product List")
def step_impl(context):
    driver = context.response

    src = driver.page_source
    found = re.search("No results!", src)

    assert not found


@given("The Products category is opened")
def step_impl(context):
    driver = context.response

    open_products_from_homepage(driver)


@when('The product "{name}" is searched')
def step_search(context, name):
    driver = context.response

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, "input-name")))
    elem.send_keys(name)
    elem = driver.find_element_by_id("button-filter")
    elem.click()


@then("No results are given")
def step_impl(context):
    driver = context.response

    src = driver.page_source
    found = re.search("No results!", src)

    assert found


@then('Products with "{term}" in name are shown')
def step_find(context, term):
    driver = context.response

    src = driver.page_source
    found = re.search("No results!", src)

    if found:
        print("Produkt: '", term, "' není existující produkt")
        return

    elem = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//tbody/tr/td[3]")))

    i = 2
    while True:
        assert re.search(term, elem.text)
        elem = driver.find_elements_by_xpath("// tr["+str(i)+"] / td[3]")

        if not (len(elem) > 0):
            break

        i = int(i) + 1
        elem = elem[0]
