import pytest
from lib.file import is_source_file


@pytest.mark.parametrize('input',
                         ["src/components/test.jsx",
                          "src/styles/test.scss",
                          "src/app/test.module.css"])
def test_is_source_file_returns_true_for_source_file_path(input):
    sut = is_source_file(input)

    assert sut


@pytest.mark.parametrize('input',
                         ["project/node_modules/test.jsx",
                          "src/coverage/test.scss",
                          "src/app/dist/test.module.css"])
def test_is_source_file_returns_false_for_non_source_file_path(input):
    sut = is_source_file(input)

    assert not sut
