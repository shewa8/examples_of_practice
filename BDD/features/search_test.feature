Feature: Google Search
As an internet surfer,
I want to find some information

  Scenario: Simple Google search
    Given the Google main page is opened
    When the user searches for "Python"
    Then results are shown for "Python"