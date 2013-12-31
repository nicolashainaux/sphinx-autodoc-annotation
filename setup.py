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
    version = "1.0",
    url = "https://github.com/hsoft/sphinx-autodoc-annotation",
    py_modules = ['sphinx_autodoc_annotation'],
    install_requires = [
        'sphinx>=1.1',
    ],
    author="Virgil Dupras",
    author_email="hsoft@hardcoded.net",
    description="Use Python 3 annotations in sphinx-enabled docstrings",
    long_description=open('README.rst', 'rt').read(),
    license="BSD",
    classifiers=CLASSIFIERS,
)
