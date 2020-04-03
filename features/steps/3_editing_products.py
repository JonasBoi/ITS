from behave import *

@given('The product "New Product" exists')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given The product "New Product" exists')


@when('Its name is changed to "{name}"')
def step_impl(context, name):

    raise NotImplementedError(u'STEP: When Its name is changed to "Old Product"')


@step('The price is set to "1000"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And The price is set to "1000"')


@then('The product "Old Product" with the price of "1000" is displayed in the Product List')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then The product "Old Product" with the price of "1000" is displayed in the Product List')


@given('The status of "New Product" is "Disabled"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given The status of "New Product" is "Disabled"')


@when('the status is edited to "Enabled" and saved')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the status is edited to "Enabled" and saved')


@then('"New Product" is not listed in "Disabled" products')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then No "Disabled" products are in store')