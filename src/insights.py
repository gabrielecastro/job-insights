from src import jobs
# from jobs import read


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    job_type_list = set()
    for row in jobs_list:
        job_type_list.add(row["job_type"])
    return job_type_list


def filter_by_job_type(jobs, job_type):
    job_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    job_industry = set()
    for row in jobs_list:
        if len(row["industry"]) > 0:
            job_industry.add(row["industry"])

    return job_industry


def filter_by_industry(jobs, industry):
    job_industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_industry_list.append(job)
    return job_industry_list


def get_max_salary(path):
    jobs_list = jobs.read(path)
    job_salary = set()
    for row in jobs_list:
        if row["max_salary"].isdigit():
            job_salary.add(row["max_salary"])
    int_list = list(map(int, job_salary))
    max_salary = max(int_list)

    return max_salary


def get_min_salary(path):
    jobs_list = jobs.read(path)
    job_salary = set()
    for row in jobs_list:
        if row["min_salary"].isdigit():
            job_salary.add(row["min_salary"])
    int_list = list(map(int, job_salary))
    min_salary = min(int_list)

    return min_salary


def check_salary(min_salary, max_salary, salary):
    if not isinstance(salary, int):
        raise ValueError
    elif not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise ValueError
    elif min_salary > max_salary:
        raise ValueError


def matches_salary_range(job, salary):
    try:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        check_salary(min_salary, max_salary, salary)
        return min_salary <= salary <= max_salary
    except KeyError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            continue
    return list_jobs
