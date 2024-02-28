import pytest
from Views.View import View


@pytest.fixture
def view_instance():
    return View()


def test_is_valid_date_valid(view_instance):
    assert view_instance.is_valid_date("25/12/2023")


def test_is_valid_date_invalid(view_instance):
    assert not view_instance.is_valid_date("2023/12/25")


def test_is_valid_id_valid(view_instance):
    assert view_instance.is_valid_id("AB12345")


def test_is_valid_id_invalid(view_instance):
    assert not view_instance.is_valid_id("ABC12345")


def test_is_valid_alpha_valid(view_instance):
    assert view_instance.is_valid_alpha("abc XYZ")


def test_is_valid_alpha_invalid(view_instance):
    assert not view_instance.is_valid_alpha("abc123")


def test_is_valid_int_valid(view_instance):
    assert view_instance.is_valid_int("123")


def test_is_valid_int_invalid(view_instance):
    assert not view_instance.is_valid_int("abc")
