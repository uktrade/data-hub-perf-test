from locust import HttpLocust, TaskSet, task
import os
import random

cookie = os.environ['COOKIE']
print(cookie)


searchables = ['apple', 'banana', 'carrot', 'date', 'eastern', 'forge', 'great', 'harris', 'incorporated', 'james']


class Interactions(TaskSet):
    def login(l):
        l.client.request('GET', '/', cookies = {'datahub.sid': cookie})

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
 
    @task()
    def interactions(l):
        l.client.get("/interactions?sortby=date%3Adesc")

    @task()
    def single_interaction(l):
        l.client.get("/interactions/aca7bb92-59b4-43d7-b0fa-019cdda36f1d")

    @task()
    def resort_interactions(l):
        l.client.get("/interactions?custom=true&sortby=dit_adviser.name%3Aasc")

class Companies(TaskSet):
    def login(l):
        l.client.request('GET', '/', cookies = {'datahub.sid': cookie})

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    @task()
    def companies(l):
        l.client.get("/companies?sortby=modified_on%3Adesc")

    @task()
    def single_company(l):
        l.client.get("/companies/6eb6db56-5ae4-41ac-99f1-65ab4b7a9ef6/details")

    @task()
    def filter_companies(l):
        l.client.get("/companies?custom=true&sector=9538cecc-5f95-e211-a939-e4115bead28a&sortby=modified_on%3Aasc")

    @task()
    def search_companies(l):
        term = random.choice(searchables)
        l.client.get("/search/companies?term=" + term)


class InteractionUser(HttpLocust):
    task_set = Interactions
    min_wait = 5000
    max_wait = 9000

class CompanyUser(HttpLocust):
    task_set = Companies
    min_wait = 5000
    max_wait = 9000
