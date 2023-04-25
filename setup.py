from pkg_resources import parse_requirements
from setuptools import setup, find_packages


setup(
    name=f'remo_memory',
    version='0.0.1',
    install_requires=[
        str(_requirement)
        for _requirement in parse_requirements(
            open("requirements.txt")
        )
    ],
    extras_require={
        "dev": [
            str(_requirement)
            for _requirement in parse_requirements(
                open("requirements-dev.txt")
            )
        ],
    },
    packages=find_packages(
        include=[
            f"remo_memory",
            f"remo_memory.*",
        ]
    ),
    description=f'REMO: Rolling Episodic Memory Organizer',
)
