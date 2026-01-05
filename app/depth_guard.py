class DepthGuardError(Exception):
    pass

def guarded(fn):
    def wrapper(*args, **kwargs):
        depth = kwargs.get("depth", 0)
        if depth > 5:
            raise DepthGuardError()
        kwargs["depth"] = depth + 1
        return fn(*args, **kwargs)
    return wrapper
