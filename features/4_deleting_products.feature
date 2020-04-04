@delete
Feature: Ability to delete products from the admin section


  Background: We are logged into admin area
    Given Home page of the admin area is opened

  @test @one_prod
  Scenario: Deleting one product
    Given The Products category is opened
    And The product "Old product" exists
    When Product "Old product" is deleted
    Then Product "Old product" doesnt exist anymore


  Scenario: Deleting more products
    Given The Products category is opened
    And Products with quantity of "1000" exist
    When All products with the quantity of "1000" are deleted
    Then No products with the quantity of "1000" exist in the store

  @test @no_prod
  Scenario: Deleting no products
    Given The Products category is opened
    When No products are selected and deleted
    Then The product count remains the same
