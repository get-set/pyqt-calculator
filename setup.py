from setuptools import setup

requirements = [
    'PyQt5']

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='calculator',
    version='0.0.1',
    description="A PyQt5 calculator application.",
    author="get-set",
    author_email='535993116@qq.com',
    url='https://github.com/get-set/calculator',
    packages=['calculator', 'calculator.images',
              'calculator.tests'],
    package_data={'calculator.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Calculator=calculator.calculator:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='calculator',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
