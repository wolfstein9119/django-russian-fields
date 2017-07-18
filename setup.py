import os
from setuptools import setup, find_packages
import russian_fields

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-russian-fields',
    version=russian_fields.__version__,
    packages=['russian_fields'],
    install_requires=['django'],
    include_package_data=True,
    license='BSD 2-Clause License',
    description='A simple Django app to use russian fields.',
    long_description=README,
    url='https://github.com/wolfstein9119/django-russian-fields',
    author='Alexey Tatarinov',
    author_email='wolfstein9119@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 2-Clause License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
