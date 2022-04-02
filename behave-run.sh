#!/usr/bin/env bash
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features
