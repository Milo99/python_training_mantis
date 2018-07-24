# -*- coding: utf-8 -*-
from model.project import Project
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Project(name=proj)
    for proj in [random_string("PROJ", 10)]
]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.soap.get_projects_list('administrator','root')
    app.project.create(project)
    new_projects = app.soap.get_projects_list('administrator','root')
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects) == sorted(new_projects)