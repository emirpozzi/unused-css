import pytest
from lib.angular import Angular
from lib.react import React
from lib.unused_css import UnusedCss

def test_get_unused_css_finds_correct_number_unused_classes():
    sut = UnusedCss("./mock/angular", Angular())

    _, count = sut.get_unused_css()

    assert count == 2

def test_get_unused_css_finds_correct_number_css_classes():
    sut = UnusedCss("./mock/angular", Angular())

    unused_classes, _ = sut.get_unused_css()

    assert len(unused_classes) == 4

@pytest.mark.skip(reason="not implemented yet")
def test_get_unused_css_finds_correct_number_unused_classes():
    sut = UnusedCss("./mock/react", React())

    _, count = sut.get_unused_css()

    assert count == 2

@pytest.mark.skip(reason="not implemented yet")
def test_get_unused_css_finds_correct_number_css_classes():
    sut = UnusedCss("./mock/react", React())

    unused_classes, _ = sut.get_unused_css()

    assert len(unused_classes) == 4

