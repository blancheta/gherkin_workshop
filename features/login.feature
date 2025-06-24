Feature: User Authentication

  As a registered user
  I want to be able to log in and log out
  So that I can access my personal dashboard securely

  Background:
    Given the user "admin@upidev.com" exists with password "password123"

  Scenario: Successful login
    Given I am on the login page
    When I enter email "admin@upidev.com" and password "password123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see a welcome message with my username

  Scenario: Failed login with incorrect credentials
    Given I am on the login page
    When I enter username "admin@upidev.com" and password "wrongpass"
    And I click the login button
    Then I should see an error message saying "Invalid username or password"

  Scenario: Logout
    Given I am logged in as "admin@upidev.com"
    When I click the logout link
    Then I should be redirected to the login page
    And I should no longer have access to the dashboard