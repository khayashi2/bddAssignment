import pytest
import requests
from pytest_bdd import scenarios, when, then

POKE_API = 'https://pokeapi.co/api/v2/pokemon/'
scenarios('../features/poke_pokemon.feature', example_converters=dict(pokemon=str, base_exp=int))


@pytest.fixture
@when('the Poke API is queried with "<pokemon>"')
def poke_response(pokemon):
    params = {'format': 'json'}
    response = requests.get(POKE_API + pokemon, params=params)
    return response


@then('the response status code is 200')
def poke_response_code(poke_response):
    assert poke_response.status_code == 200


@then('the response is that "<base_exp>"')
def schedule_response_has_episodes(poke_response, base_exp):
    assert base_exp == poke_response.json()['base_experience']
