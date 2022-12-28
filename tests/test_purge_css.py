import pytest
from lib.unused_css import get_unused_css

@pytest.mark.parametrize('input', 
["src/components/test.component.html",
"src/components/test.component.css",
"src/app/test.component.css"])
def test_is_component_recognizes_components(input):
    assert get_unused_css(input)

