from model.project import Project
from random import randrange

def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test"))

    old_projects = app.soap.get_projects_list('administrator','root')
    index = randrange(len(old_projects))
    project = old_projects[index]
    app.project.delete_project_by_index(index)
    new_projects = app.soap.get_projects_list('administrator','root')
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)