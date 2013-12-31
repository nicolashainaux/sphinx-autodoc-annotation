import inspect

from sphinx.ext.autodoc import FunctionDocumenter, MethodDocumenter

def get_class_link(obj):
    if (obj is None) or (obj == inspect.Signature.empty):
        return None
    if inspect.isclass(obj):
        if obj.__module__ == 'builtins':
            return "``%s``" % obj.__qualname__
        else:
            fullname = '%s.%s' % (obj.__module__, obj.__qualname__)
            return ':class:`~%s`' % fullname
    return None

def get_param_type(param):
    if param.annotation != inspect.Signature.empty:
        return param.annotation
    else:
        # We don't want to overreach ourselves. Too many possibilities of messing up. So, we
        # only support basic types here.
        if isinstance(param.default, (bool, int, float, str)):
            return type(param.default)
    return None

def add_annotation_content(obj, result):
    try:
        sig = inspect.signature(obj)
    except ValueError:
        # Can't extract signature, do nothing
        return
    existing_contents = ''.join(result)
    toadd = []
    for param in sig.parameters.values():
        type_directive = ":type %s:" % param.name
        if type_directive in existing_contents:
            # We already specidy the type of that argument in the docstring, don't specify it again.
            continue
        arg_link = get_class_link(get_param_type(param))
        if arg_link:
            toadd.append("%s %s" % (type_directive, arg_link))
            
    if ":rtype:" not in existing_contents:
        return_link = get_class_link(sig.return_annotation)
        if return_link:
            toadd.append(":rtype: %s" % return_link)
    if toadd:
        # Let's see where we're going to insert our directives. We can't append it at the end of
        # the docstring because there might be a section breaker between our params and the end
        # of the list that will also break our :type: stuff. We have to try to keep them grouped.
        for i, s in enumerate(result):
            if ":param" in s:
                insert_index = i
                break
        else:
            # We don't have a parameters directive, just add nothing.
            return
        for line in toadd:
            # Yeah, inefficient, but we need to keep the same list instance.
            result.insert(insert_index, line)

class MyFunctionDocumenter(FunctionDocumenter):
    def get_doc(self, *args, **kwargs):
        result = super().get_doc(*args, **kwargs)
        add_annotation_content(self.object, result[-1])
        return result

class MyMethodDocumenter(MethodDocumenter):
    def get_doc(self, *args, **kwargs):
        result = super().get_doc(*args, **kwargs)
        add_annotation_content(self.object, result[-1])
        return result

def setup(app):
    app.add_autodocumenter(MyFunctionDocumenter)
    app.add_autodocumenter(MyMethodDocumenter)
