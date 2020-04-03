Feature: Various possibilities of editing products

  Scenario: Changing the product name and price
    Given The product "New Product" exists
    When Its name is changed to "Old Product"
    And The price is set to "1000"
    Then The product "Old Product" with the price of "1000" is displayed in the Product List


  Scenario: Changing the name of product to blank
    Given The product "New Product" exists
    When Its name is changed to " "
    Then The operation is unsuccessful


  Scenario: Changing the product status to Enabled
    Given The status of "New Product" is "Disabled"
    When the status is edited to "Enabled" and saved
    Then "New Product" is not listed in "Disabled" products

