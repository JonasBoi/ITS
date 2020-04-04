@edit @test
Feature: Various possibilities of editing products


  Background: We are logged into admin area
    Given Home page of the admin area is opened

  @edit_one
  Scenario: Changing the product name and price
    Given The product "New product" exists
    When Its name is changed to "Old product"
    And The price is set to "1000"
    Then The product "Old product" with the price of "1000.0000" is displayed in the Product List

  @blank_edit
  Scenario: Changing the name of product to blank
    Given The product "Old product" exists
    When Its name is changed to " "
    Then The operation is unsuccessful

  @status_edit
  Scenario: Changing the product status to Enabled
    Given The status of "New product" is "Disabled"
    When the status is edited to "Enabled" and saved
    Then "New product" is not listed in "Disabled" products

