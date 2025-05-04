from setuptools import setup

setup(
    name="github-activity",
    version="1.0.0",
    description="CLI para consultar actividad reciente de usuarios de GitHub",
    author="Andejecruher",
    packages=["github_activity"],
    entry_points={
        "console_scripts": [
            "github-activity = github_activity.__main__:main"
        ]
    },
    python_requires=">=3.6",
)
