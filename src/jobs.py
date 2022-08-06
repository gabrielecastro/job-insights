from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs_list_dicts = []
        for row in jobs_reader:
            jobs_list_dicts.append(row)

    return jobs_list_dicts

