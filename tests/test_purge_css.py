from lib.unused_css import UnusedCss

def finds_correct_number_unused_classes():
    sut = UnusedCss("./mock/angular")

    (_, count) = sut.get_unused_css()

    assert count == 2

def test_test():
    sut = UnusedCss("./mock/angular")

    (unused_classes, _) = sut.get_unused_css()

    assert len(unused_classes) == 4

