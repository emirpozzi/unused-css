from lib.angular import Angular
from lib.react import React
from lib.unused_css import UnusedCss


def test_Angular_get_unused_css_finds_correct_number_unused_classes():
    sut = UnusedCss("./tests/mock/angular", Angular())

    _, unused_classes = sut.get_unused_css()

    assert unused_classes == 2


def test_Angular_get_unused_css_finds_correct_number_style_files():
    sut = UnusedCss("./tests/mock/angular", Angular())

    style_files, _ = sut.get_unused_css()

    assert len(style_files) == 4


def test_React_get_unused_css_finds_correct_number_unused_classes():
    sut = UnusedCss("./tests/mock/react", React())

    _, unused_classes = sut.get_unused_css()

    assert unused_classes == 5


def test_React_get_unused_css_finds_correct_number_style_files():
    sut = UnusedCss("./tests/mock/react", React())

    style_files, _ = sut.get_unused_css()

    assert len(style_files) == 6
