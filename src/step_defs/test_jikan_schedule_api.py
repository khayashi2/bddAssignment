import pytest
import requests
from jikanpy import Jikan
from pytest_bdd import scenarios, when, then

jikan = Jikan()

DAY_API = 'https://private-anon-147fc027b5-jikan.apiary-proxy.com/v3/schedule/'
scenarios('../features/jikan_schedule.feature', example_converters=dict(time=str, hasEpisode=bool))


@pytest.fixture
@when('the Jikan is queried with "<time>"')
def schedule_response(time):
    params = {'format': 'json'}
    response = requests.get(DAY_API + time, params=params)
    return response


@then('the response status code is 200')
def schedule_response_code(schedule_response):
    assert schedule_response.status_code == 200


@then('the response if it has an episode more than 1 "<has_episode>"')
def schedule_response_has_episodes(schedule_response, time, has_episode):
    response_body = schedule_response.json()[time]
    contains = 'False'
    for v in response_body:
        num_of_episodes = v['episodes']
        if isinstance(num_of_episodes, int):
            contains = 'True'
            break
    assert contains == has_episode
