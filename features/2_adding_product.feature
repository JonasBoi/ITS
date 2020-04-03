@add
Feature: Adding products to the list

  Background: We are logged into admin area
    Given Home page of the admin area is opened

  @test
  Scenario: Create a new product
    Given The Products category is opened
    When A new product "New product" is created
    Then "New product" is shown in the Product List


  Scenario: Creating product by copying
    Given The product "New product" is in the Product List
    When "New product" is copied
    Then Two products called "New product" are shown
    But One of products called "New product" has "Disabled" status


  Scenario: Creating a product with no name
    Given Blank Add Product page is opened
    When The blank product is saved
    Then The operation is unsuccessful