from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    assert count_ocurrences(path, "products") == 1394
    assert count_ocurrences(path, "Products") == 1394
    assert count_ocurrences(path, "python") == 1639
    assert count_ocurrences(path, "Python") == 1639
