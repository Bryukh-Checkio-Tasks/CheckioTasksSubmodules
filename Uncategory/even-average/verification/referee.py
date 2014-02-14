
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

cover_tuple = """

def cover(func, in_data):
    return func(tuple(in_data))

"""


from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover_tuple,
            'python-3': cover_tuple
        }).on_ready)
