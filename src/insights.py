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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
