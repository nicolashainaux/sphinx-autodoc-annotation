from setuptools import setup

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.3',
    'Operating System :: OS Independent',
    'Topic :: Documentation',
]

setup(
    name = "sphinx-autodoc-annotation",
    version = "1.0-1",
    url = "https://github.com/hsoft/sphinx-autodoc-annotation",
    py_modules = ['sphinx_autodoc_annotation'],
    install_requires = [
        'sphinx>=1.1',
    ],
    author="Virgil Dupras; (Current maintainer: Nicolas Hainaux)",
    author_email="nh.techn@gmail.com",
    description="Use Python 3 annotations in sphinx-enabled docstrings",
    long_description=open('README.rst', 'rt').read(),
    license="BSD",
    classifiers=CLASSIFIERS,
)
