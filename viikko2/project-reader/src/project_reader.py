from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Hae ja dekoodaa sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        
        data = tomli.loads(content)
        

        
        name = data.get("tool", {}).get("poetry", {}).get("name", "Unnamed Project")
        description = data.get("tool", {}).get("poetry", {}).get("description", "No description provided")
        license_ = data.get("tool", {}).get("poetry", {}).get("license", "No license specified")

        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Luo Project-olio
        project = Project(name, description, license_, authors, dependencies, dev_dependencies)

        # Palauta Project-olio
        return project
