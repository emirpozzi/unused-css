import pytest
from lib.angular import Angular


@pytest.mark.parametrize('input',
                         ["src/components/test.component.html",
                          "src/components/test.component.css",
                          "src/app/test.component.css"])
def test_is_component_recognizes_components(input):
    sut = Angular()

    assert sut.is_component(input)


@pytest.mark.parametrize('input',
                         ["src/styles/_buttons.scss",
                          "src/app/index.css",
                          "src/app/components/module.scss"])
def test_is_component_recognizes_not_components(input):
    sut = Angular()

    assert not sut.is_component(input)
