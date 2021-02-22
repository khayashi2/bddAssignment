Feature: Anime Total Amount of Genre
  Find the amount of a genre for an anime


  Scenario Outline: Jikan API Query on genre
    When the Jikan is queried with "<id>" with a parameter of anime
    Then the response shows total shows of "<hasAmount>"

    Examples: id
      | id              | hasAmount |
      | 1               | True   |
      | 2               | True   |
      | 19              | True   |