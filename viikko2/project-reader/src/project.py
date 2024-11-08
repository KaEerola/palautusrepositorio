class Project:
    def __init__(self, name, description, license_, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license_ = license_
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_str = "\n".join(f"- {author}" for author in self.authors)
        dependencies_str = "\n".join(f"- {dep}" for dep in self.dependencies)
        dev_dependencies_str = "\n".join(f"- {dev_dep}" for dev_dep in self.dev_dependencies)
        
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license_}\n\n"
            f"Authors:\n{authors_str}\n\n"
            f"Dependencies:\n{dependencies_str}\n\n"
            f"Development dependencies:\n{dev_dependencies_str}"
        )
