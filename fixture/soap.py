from suds.client import Client
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects_list(self, username, password):
        client = Client("http://localhost:8080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        list = []
        for item in client.service.mc_projects_get_user_accessible(username, password):
            name = item[1]
            list.append(Project(name=name))
        return list