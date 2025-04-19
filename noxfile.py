# /// script
# dependencies = ["nox", "uv", "py-markdown-table"]
# ///

import nox
from py_markdown_table.markdown_table import markdown_table
import tomllib
import pathlib

nox.options.sessions = ["lint"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def build(session: nox.Session) -> None:
    """Build the website."""
    session.notify("software_table")
    session.notify("mystify")


@nox.session
def software_table(session: nox.Session) -> None:

    software_projects_path = pathlib.Path("data/software_projects.toml")
    with software_projects_path.open("rb") as data_file:
        software_projects = tomllib.load(data_file)

    projects_table = markdown_table(software_projects["project"]).get_markdown()

    generated_file = pathlib.Path("content/_generated_software_table.md")

    with generated_file.open("w") as out_file:
        out_file.write(projects_table)

@nox.session
def mystify(session: nox.Session) -> None:
    """Run mystmd."""
    session.run("uvx", "--from=mystmd", "myst", "build", "--all", "--html")


@nox.session
def lint(session):
    session.install("uv")
    session.run("uvx", "pre-commit", "run","--all-files")


if __name__ == "__main__":
    nox.main()
