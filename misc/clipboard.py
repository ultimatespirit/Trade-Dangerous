"""
Wrapper for trade-dangerous clipboard functionality.
"""

import os

if 'NOTK' not in os.environ:
    try:
        from tkinter import Tk

        class SystemNameClip(object):
            """
            A cross-platform wrapper for copying system names into
            the clipboard such that they can be pasted into the E:D
            galaxy search - which means forcing them into lower case
            because E:D's search doesn't work with upper case
            characters.
            """

            def __init__(self):
                self.tkroot = Tk()
            self.tkroot.withdraw()

            def copy_text(self, text):
                """ Copies the specified text into the clipboard. """
                self.tkroot.clipboard_clear()
                self.tkroot.clipboard_append(text.lower())

    except ImportError:
        print(
                "WARNING: This feature expects you to have 'tkinter' package "
                "installed to work. It is either not installed or broken.\n"
                "Set the environment variable 'NOTK' to disable this warning."
        )

