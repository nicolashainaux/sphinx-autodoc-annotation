import inspect

from sphinx.ext.autodoc import FunctionDocumenter, MethodDocumenter

def get_class_link(obj):
    if obj == inspect.Signature.empty:
        return None
    if inspect.isclass(obj):
        if inspect.isbuiltin(obj):
            return obj.__qualname__
        else:
            fullname = '%s.%s' % (obj.__module__, obj.__qualname__)
            return ':class:`~%s`' % fullname
    return None

def add_annotation_content(documenter):
    obj = documenter.object
    try:
        sig = inspect.signature(obj)
    except ValueError:
        # Can't extract signature, do nothing
        return
    src = inspect.getsourcefile(obj)
    srcline = inspect.getsourcelines(obj)[1]
    existing_contents = ''.join(documenter.directive.result)
    for param in sig.parameters.values():
        type_directive = ":type %s:" % param.name
        if type_directive in existing_contents:
            # We already specidy the type of that argument in the docstring, don't specify it again.
            continue
        arg_link = get_class_link(param.annotation)
        if arg_link:
            line = "%s: %s\n" % (type_directive, arg_link)
            documenter.add_line(line, src, srcline)
    if ":rtype:" not in existing_contents:
        return_link = get_class_link(sig.return_annotation)
        if return_link:
            line = ":rtype: %s\n" % return_link
            documenter.add_line(line, src, srcline)

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
