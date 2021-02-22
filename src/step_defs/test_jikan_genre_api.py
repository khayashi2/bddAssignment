import pytest
from jikanpy import Jikan

from pytest_bdd import scenarios, given, when, then, scenario
jikan = Jikan()

scenarios('../features/jikan_genre.feature', example_converters=dict(id=int, hasAmount=bool))


@pytest.fixture
@when('the Jikan is queried with "<id>" with a parameter of anime')
def genre_response(id):
    return jikan.genre("anime", id)

@then('the response shows total shows of "<hasAmount>"')
def genre_response_amount(genre_response):
    assert genre_response.get("item_count") > 0 if True else False
