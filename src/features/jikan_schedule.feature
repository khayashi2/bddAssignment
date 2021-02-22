Feature: JiKan Schedules
  If the time of week contains more than a cour of episodes
  Find if an anime will have more than 12 episodes on a time of week


  Scenario Outline: Jikan API Query on schedule
    When the Jikan is queried with "<time>"
    Then the response status code is 200
    And the response if it has an episode more than 1 "<has_episode>"

    Examples: time
      | time              | has_episode  |
      | monday            | True        |
      | wednesday         | True        |
      | friday            | True        |