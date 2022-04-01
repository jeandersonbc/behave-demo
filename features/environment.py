from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from behave.model import Feature
from behave.runner import Context


def before_feature(_, feature: Feature):
    print("BEFORE FEATURE Run")
    print(f"- feature_name=\"{feature.name}\" status=\"{feature.status}\"")

    # I'm consciously setting auto-retry on every scenario since I don't trust on their stability
    for scenario in feature.scenarios:
        patch_scenario_with_autoretry(scenario, max_attempts=5)


def after_feature(context: Context, feature: Feature):
    print("AFTER FEATURE Run")
    print(f"- feature_name=\"{feature.name}\" status=\"{feature.status}\" failed=\"{context.failed}\"")
