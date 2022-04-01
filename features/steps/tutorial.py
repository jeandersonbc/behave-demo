import behave

from behave import given, when, then


@given("we have behave installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert behave.__version__ == '1.2.6'


@when("we implement a test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True is not False


@then("behave will test it for us!")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.failed is False
