from random import random

from behave import *

use_step_matcher("re")


@given("that I have a funky CUT")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I exercise the funky CUT")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("it might work as expected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    some_random_result = random()
    assert some_random_result > 0.5, f"Expected to be >0.5 but was {some_random_result:.2f}"
