import os
import time
from distutils.sysconfig import get_python_lib
from pathlib import Path

from .encodings import _get_encodings_block
from .fonts import _get_fonts_block, get_fonts
from .utils import POPPLER_DATA_DIR

__version__ = "1.1.0"


def _xpdfrc_header():
    return [
        "# {0}".format(time.ctime()),
        "# Generated by pyxpdf_poppler_data python module",
        "# THIS FILE WILL NOT WORK ON OTHER SYSTEM, ",
        "# AS IT USES ABSOLUTE PATHs",
        "",
    ]


def generate_xpdfrc():
    xpdfrc = _xpdfrc_header()

    xpdfrc += _get_encodings_block()
    xpdfrc += _get_fonts_block()

    return os.linesep.join(xpdfrc)


def get_poppler_dir():
    return str(POPPLER_DATA_DIR)


def get_xpdfrc(force_rewrite=True):
    """
    Get the generated xpdfrc file path.

    Parameters
    ----------
    force_rewrite: bool
        generate xpdfrc again even if it exists already. Helpful if somehow xpdfrc file
        got corrupted.
    """
    xpdfrc_path = Path(get_python_lib(), "default.xpdf")
#     if (not xpdfrc_path.exists()) or force_rewrite:
#         xpdfrc = generate_xpdfrc()
#         with open(str(xpdfrc_path), "w") as fp:
#             fp.write(xpdfrc)
    return str(xpdfrc_path.absolute())


__all__ = [get_fonts, get_xpdfrc, get_poppler_dir, generate_xpdfrc]
