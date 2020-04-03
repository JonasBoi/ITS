Feature: Ability to delete products from the admin section

  Scenario: Deleting one product
    Given The Products category is opened
    When Product "Old product" is deleted
    Then Product "Old product" doesn't exist anymore


  Scenario: Deleting more products
    Given The Products category is opened
    And Products with quantity of "1000" exist
    When All products with the quantity of "1000" are deleted
    Then No products with the quantity of "1000" exist in the store


  Scenario: Deleting no products
    Given The Products category is opened
    When No products are selected and deleted
    Then The product count remains the same


  Scenario: Deleting all products
    Given  Given The Products category is opened
    When All products are selected and deleted
    Then No products are available in the store