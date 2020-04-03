from behave import *

use_step_matcher("re")


@when('Product "Old product" is deleted')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Product "Old product" is deleted')


@then('Product "Old product" doesn\'t exist anymore')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Product "Old product" doesn\'t exist anymore')


@step('Products with quantity of "1000" exist')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Products with quantity of "1000" exist')


@when('All products with the quantity of "1000" are deleted')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When All products with the quantity of "1000" are deleted')


@then('No products with the quantity of "1000" exist in the store')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then No products with the quantity of "1000" exist in the store')


@when("No products are selected and deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When No products are selected and deleted')


@then("The product count remains the same")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The product count remains the same')


@given("Given The Products category is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given  Given The Products category is opened')


@when("All products are selected and deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When All products are selected and deleted')


@then("No products are available in the store")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then No products are available in the store')