# -----------------------------------------------------------------------------

from time import time

# -----------------------------------------------------------------------------


def timeit(method):

    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        print("Time:{}".format("%.18f" % (te - ts)))
        return result

    return timed

# -----------------------------------------------------------------------------
