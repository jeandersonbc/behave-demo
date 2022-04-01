Feature: automatic handling failures

  Scenario: rerun a few times
    Given that I have a funky CUT
    When I exercise the funky CUT
    Then it might work as expected