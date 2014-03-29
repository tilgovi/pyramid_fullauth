import pytest

from pyramid_fullauth.tools import validate_passsword, password_generator
from pyramid_fullauth.exceptions import (
    EmptyError, ShortPasswordError, PasswordConfirmMismatchError
)


@pytest.mark.parametrize(('password', 'exception'),
                         [('', EmptyError),
                         ('1234', ShortPasswordError),
                         ('123456789', PasswordConfirmMismatchError)
                          ])
def test_raises_errors(web_request, password, exception):
    with pytest.raises(exception):
        validate_passsword(web_request, password)


@pytest.mark.parametrize('length', [5, 6])
def test_password_generator(length):
    assert len(password_generator(length)) == length