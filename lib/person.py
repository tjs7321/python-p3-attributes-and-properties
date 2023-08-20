#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    species = "Homo sapiens"

    def __init__(self, name='Hubert', job='Admin'):
        self.name = name
        self.job = job

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age


    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if (type(name) == (str)) and (0 < len(name) < 24):
            self._name = name.title()

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if (type(job) == (str)) and (job in APPROVED_JOBS):
            self._job = job

        else:
            print("Job must be in list of approved jobs.")

    age = property(get_age, set_age)
    name = property(get_name, set_name)
    job = property(get_job, set_job)

    pass
