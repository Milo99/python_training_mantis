from model.project import Project
# import re

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        # open projects page
        self.display_projects_page()
        # init contact creation
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_contact_form(project)
        # submit contact creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def delete_project_by_index(self, index):
        wd = self.app.wd
        # open projects page
        self.display_projects_page()
        # select first contact
        wd.find_elements_by_css_selector("tr.row-1 td a, tr.row-2 td a")[index].click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    def fill_contact_form(self, project):
        self.change_field_value("name", project.name)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.display_projects_page()
        return len(wd.find_elements_by_css_selector("tr.row-1 td a, tr.row-2 td a"))


    def display_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.display_projects_page()
            self.project_cache = []
            project_list = wd.find_elements_by_css_selector("tr.row-1 td a, tr.row-2 td a")
            for element in project_list:
                name = element.text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)