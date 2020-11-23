# -*- coding: UTF-8 -*-

# Import from standard library
import os
import moo
# Import from our lib
from moo.lib import moo
import pytest


def test_moo():
    assert type(moo()) == str
    assert moo("john") == "Mooooooo... Hello john!"
