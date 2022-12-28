from lib.unused_css import get_unused_css

def finds_correct_number_unused_classes():
    (_, count) = get_unused_css("./mock/angular")
    assert count == 2

def test_test():
    (unused_classes, _) = get_unused_css("./mock/angular")
    assert len(unused_classes) == 4

