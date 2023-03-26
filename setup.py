from setuptools import setup, find_packages

setup(
    name='Twitter_Scraper',
    version='0.1',
    description='A Python package to gather tweets from Twitter',
    packages=find_packages(),
    install_requires=[
        'tweepy',
    ],
    entry_points={
        'console_scripts': [
            'mytwitterpackage=mytwitterpackage.__main__:main',
        ],
    },
)
