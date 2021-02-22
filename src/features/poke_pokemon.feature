Feature: Pokemon Query Base Exp
  As a player,
  I want to know the base exp of a pokemon,
  So that I can know what is the base exp of a pokemon


  Scenario Outline: Poke API will query a pokemon to return base exp
    When the Poke API is queried with "<pokemon>"
    Then the response status code is 200
    And the response is that "<base_exp>"

    Examples: Pokemon
      | pokemon           | base_exp  |
      | ditto             | 101       |
      | pikachu           | 112       |
      | charizard         | 240       |