from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-05-08",
        },
        {
            "min_salary": "125410",
            "max_salary": "212901",
            "date_posted": "2020-04-28",
        },
        {
            "min_salary": "94715",
            "max_salary": "103279",
            "date_posted": "2020-05-05",
        },
    ]

    sort_by_min_salary = [
        {
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-05-08",
        },
        {
            "min_salary": "94715",
            "max_salary": "103279",
            "date_posted": "2020-05-05",
        },
        {
            "min_salary": "125410",
            "max_salary": "212901",
            "date_posted": "2020-04-28",
        },
    ]

    sort_by_max_salary = [
        {
            "min_salary": "125410",
            "max_salary": "212901",
            "date_posted": "2020-04-28",
        },
        {
            "min_salary": "94715",
            "max_salary": "103279",
            "date_posted": "2020-05-05",
        },
        {
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-05-08",
        },
    ]

    sort_by_date_posted = [
        {
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-05-08",
        },
        {
            "min_salary": "94715",
            "max_salary": "103279",
            "date_posted": "2020-05-05",
        },
        {
            "min_salary": "125410",
            "max_salary": "212901",
            "date_posted": "2020-04-28",
        },
    ]

    sort_by(jobs, "min_salary")
    assert jobs == sort_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sort_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == sort_by_date_posted
