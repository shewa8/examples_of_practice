# Created by shevchenko at 2/27/2020
Feature: Add item to the cart
  As an internet user
  Sometimes I buy goods through internet
  Therefore I want to add goods to cart.

 Scenario Outline: Looking for goods and add them to cart
    When I opened <link> using <browser>
    When I fill up <item_name> into search <field> and press on <item>
    When I open page with <item_name> and press <buy_button>
    Then I verify the availability of the <item_name> in the <cart>

    Examples:
     | link                        | browser |  item_name  | item                                    | field                            | buy_button                 | cart              |
     | https://rozetka.com.ua/     | chrome  | Python      | li.catalog-grid__cell:first-child       | .search-form__input.ng-untouched | button.buy-button          | .cart-modal__item |
     | https://www.foxtrot.com.ua/ | chrome  | Samsung s10 | .listing-item:nth-child(2)>.detail-link | .search__input                   | .new-purchase .add-to-cart | .cart-products    |
