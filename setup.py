from setuptools import setup

setup(
    name='Salty Cocktails',
    packages=['salty.cocktails'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)