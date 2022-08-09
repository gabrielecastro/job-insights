from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    dict_jobs = read_brazilian_file(path)
    for job in dict_jobs:
        assert "title" and "salary" and "type" in job
