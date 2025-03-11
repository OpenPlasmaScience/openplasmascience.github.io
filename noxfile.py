# /// script
# dependencies = ["nox", "uv"]
# ///

import nox

nox.options.sessions = ["lint"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def lint(session):
    session.run("uvx", "pre-commit", "run","--all-files")


if __name__ == "__main__":
    nox.main()
