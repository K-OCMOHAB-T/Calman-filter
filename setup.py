from setuptools import setup

setup(
    name='Calman',
    version='beta 0.9',
    packages=['my_funct'],
    url='http://phys.msu.ru',
    license='SCR',
    author='Дроздов Алексей',
    author_email='drozdofflekha1997@yandex.ru',
    description='Это программа про фильтр Калмана',
    install_requires=['matplotlib', 'numpy'],
    scripts=['bin/serpens'],
    entry_points={
        'console_scripts': ['issnake = ser.snake:main'],
        'gui_scripts': ['plotsnake = ser.snake:plot'],
    },
    test_suite='test',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',
        'Programming Language :: Python :: 3',
    ],
    keywords='sample science astrophysics',
)
