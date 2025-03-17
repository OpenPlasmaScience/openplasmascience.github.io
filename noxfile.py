# /// script
# dependencies = ["nox", "uv"]
# ///

import nox

nox.options.sessions = ["lint"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def build(session):
    session.install("uv")
    session.run("uvx", "--from=mystmd", "myst", "build", "--all", "--html")


@nox.session
def lint(session):
    session.install("uv")
    session.run("uvx", "pre-commit", "run","--all-files")


if __name__ == "__main__":
    nox.main()
