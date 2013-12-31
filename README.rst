sphinx-autodoc-annotation
=========================

*Use Python 3 annotations in sphinx-enabled docstrings*

If you're on Python 3 and writing sphinx-enabled docstrings, you might feel like doing
needless work when typing ``:type arg:`` or ``:rtype:`` directives. After all, why not use
annotations for this?

Sure, ``:param str arg: description`` is not a lot of work, but when you want to document your
argument as a specific class for which you have a ``:class:`` link, then you need to use ``:type:``
and it's cumbersome. By using this sphinx extension, you can turn this::

    def f(a):
        """Do something.
        
        :param a: description for a
        :type a: :class:`ClassForA`
        :rtype: str
        """

into::

    def f(a: ClassForA) -> str:
        """Do something.
        
        :param a: description for a
        """

Installation
------------

First, you need Python 3.3+ and a Sphinx documentation (with ``autodoc`` enabled).

You can install ``sphinx-autodoc-annotation`` with::

    $ pip install sphinx-autodoc-annotation

Then, you need to enable it in your ``conf.py`` file::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx_autodoc_annotation',
    ]

You're done!

Usage
-----

All you need to do to use this extension is to properly annotate your functions and methods with
expected types for your arguments and return value. ``:type:`` and ``:rtype:`` directives will
automatically be added to your docstring.

These directives behave like if you added them manually, that is, your argument is not going to
show up only with ``:type arg:`` you *need* ``:param arg:`` to be there (with a description of what
it does) for your type to show up.

When there are no annotations, argument types are deduced from default values. If your default value
is a ``bool``, ``str``, ``int`` or ``float``, the argument is going to be considered of that type.
That feature is there mainly because ``f(flag: bool = False)`` feels a bit redundant.

In all cases, ``:type:`` and ``:rtype:`` directives in the docstring will always have precedence
over annotations and defaults.
