import inspect

from sphinx.ext.autodoc import FunctionDocumenter, MethodDocumenter

def get_class_link(obj):
    if inspect.isclass(obj):
        if inspect.isbuiltin(obj):
            return obj.__qualname__
        else:
            fullname = '%s.%s' % (obj.__module__, obj.__qualname__)
            return ':class:`~%s`' % fullname
    return None

def add_annotation_content(documenter):
    sig = inspect.signature(documenter.object)
    for param in sig.parameters.values():
        arg_link = get_class_link(param.annotation)
        if arg_link:
            line = ":type %s: %s" % (param.name, arg_link)
            documenter.add_line(line, '', 0)
    return_link = get_class_link(sig.return_annotation)
    if return_link:
        line = ":rtype: %s" % return_link
        documenter.add_line(line, '', 0)

class MyFunctionDocumenter(FunctionDocumenter):
    def generate(self, *args, **kwargs):
        super().generate(*args, **kwargs)
        add_annotation_content(self)

class MyMethodDocumenter(MethodDocumenter):
    def generate(self, *args, **kwargs):
        super().generate(*args, **kwargs)
        add_annotation_content(self)

def setup(app):
    app.add_autodocumenter(MyFunctionDocumenter)
    app.add_autodocumenter(MyMethodDocumenter)
