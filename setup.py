from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='Calman',
    version='0.0.1',
    author='Drozdov Alexey',
    author_email='drozdofflekha1997@yandex.ru',
    description='Calman filtration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://phys.msu.ru',
    license='MIT',
    packages=find_packages(),
    # If all your code are in a module, use py_modules instead of packages:
    # py_modules=['ser'],
    scripts=['bin/serpens'],
    entry_points={
        'console_scripts': ['issnake = ser.snake:main'],
        'gui_scripts': ['plotsnake = ser.snake:plot'],
    },
    test_suite='test',
    install_requires=['numpy>=1.13', 'matplotlib>=2.0,<3.0'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',
        'Programming Language :: Python :: 3',
        # See full list on https://pypi.org/classifiers/
    ],
    keywords='sample science astrophysics',
)
