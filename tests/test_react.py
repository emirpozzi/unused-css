import pytest
from lib.react import React

@pytest.mark.parametrize('input', 
["src/components/test.jsx",
"src/components/test.tsx",
"src/app/test.module.css"])
def test_is_component_recognizes_components(input):
    sut = React()

    assert sut.is_component(input)