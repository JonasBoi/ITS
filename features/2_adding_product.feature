@add @test
Feature: Adding products to the list

  Background: We are logged into admin area
    Given Home page of the admin area is opened

  @new_prod
  Scenario: Create a new product
    Given The Products category is opened
    When A new product "New product" is created
    Then "New product" is shown in the Product List

  @prod_copy
  Scenario: Creating product by copying
    Given The product "New product" is in the Product List
    When "New product" is copied
    Then Two products called "New product" are shown
    But One of the products called "New product" has "Disabled" status

  @fail_create
  Scenario: Creating a product with no name
    Given Blank Add Product page is opened
    When The blank product is saved
    Then The operation is unsuccessful