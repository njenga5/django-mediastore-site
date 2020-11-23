import os


_INFO = [('DATABASE_USER', 'njenga'), ('DATABASE_PASSWORD', '12monicahwanja'), ('EMAIL_HOST_PASSWORD', '12monicahwanja'), ('SECRET_KEY', 'f$o$pa1_zbbo&u!4z0i=^ynol*q@7_7bw*vq#_z%y7mpx3*ucq')]


def set_up_env():
    for key, val in _INFO:
        os.environ.setdefault(key, val)
    return os.environ
