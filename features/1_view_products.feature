@view
Feature: Viewing products from admin area
  Try to take different looks on how to display products available


  Background: We are logged into admin area
    Given Home page of the admin area is opened


  Scenario: Viewing all products
    When The Products category is selected from the menu
    Then The products are shown in the Product List


  Scenario: Searching for non-existing product
    Given The Products category is opened
    When The product "babybox for twins" is searched
    Then No results are given


  Scenario: Searching for existing product
    Given The Products category is opened
    When The product "iPod" is searched
    Then Products with "iPod" in name are shown
