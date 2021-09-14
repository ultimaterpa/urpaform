""" Functions, which help handle forms """

from ctypes import windll


def clear_clipboard() -> None:
    """Function will clear clipboard text, if there's anything stored"""

    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
