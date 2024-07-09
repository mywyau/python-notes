from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # Add any dependencies here
    ],
    tests_require=[
        'pytest',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    test_suite='test',
)
