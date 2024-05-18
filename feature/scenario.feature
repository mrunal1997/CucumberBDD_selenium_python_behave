Feature: Login functionality
  @regression
  Scenario Outline: Successful login with valid credentials
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should be logged in successfully

    Examples:
      | username    | password    |
      | student     | Password123 |
#      | student     | Password12  |
#      | student     | password123 |
  @smoke
  Scenario Outline: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see an error message

    Examples:
      | username       | password          |
      | invalid_user1  | invalid_password1 |
      | invalid_user2  | invalid_password2 |