from selenium import webdriver


def before_all(context):
    driver = webdriver.Chrome()
    driver.maximize_window()
    context.response = driver


def after_all(context):
    context.response.quit()
