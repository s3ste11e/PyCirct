from circt.ir import Context, Location

import atexit

DefaultContext = Context()
DefaultContext.__enter__()

DefaultLocation = Location.unknown()
DefaultLocation.__enter__()


@atexit.register
def __exit_context():
    DefaultLocation.__exit__(None, None, None)
    DefaultContext.__exit__(None, None, None)
