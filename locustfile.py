from locust import HttpLocust, TaskSet, task


class Interactions(TaskSet):
    def login(l):
        l.client.request('GET', '/', cookies = {'datahub.sid': 's%3A7cuTN6eEQ_Z0IE_mO7HTXUtTh1mgvA45.xoBBJSRRFfZ1Fu34PzBOveN7wBsM2O03rXzKZjosZ%2BM'})

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
 
    @task()
    def interactions(l):
        l.client.get("/interactions?sortby=date%3Adesc")

    @task()
    def single_interaction(l):
        l.client.get("/interactions/1c32d422-5d4b-42f8-81d7-8b2eed54c98e")

    @task()
    def resort_interactions(l):
        l.client.get("/interactions?custom=true&sortby=dit_adviser.name%3Aasc")

class CompanyUser(TaskSet):
    def on_

class InteractionUser(HttpLocust):
    task_set = Interactions
    min_wait = 5000
    max_wait = 9000

