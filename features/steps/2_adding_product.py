from behave import *


@when('A new product "New product" is created')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When A new product "New product" is created')


@then('"New product" is shown in the Product List')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then "New product" is shown in the Product List')


@given('The product "New product" is in the Product List')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given The product "New product" is in the Product List')


@when('"New product" is copied')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When "New product" is copied')


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