"""Setup module for bellows"""

from setuptools import find_packages, setup

setup(
    name="bellows",
    version="0.3.5",
    description="Library implementing EZSP and ZigBee",
    url="http://github.com/rcloran/bellows",
    author="Russell Cloran",
    author_email="rcloran@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'console_scripts': ['bellows=bellows.cli.main:main'],
    },
    install_requires=[
        'Click',
        'click-log',
        'pure_pcapy3==1.0.1',
        'pyserial-asyncio',
    ],
    dependency_links=[
        'https://github.com/rcloran/pure-pcapy-3/archive/e289c7d7566306dc02d8f4eb30c0358b41f40f26.zip#egg=pure_pcapy3-1.0.1',
    ],
    tests_require=[
        'pytest',
    ],
)
