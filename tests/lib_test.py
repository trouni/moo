# -*- coding: UTF-8 -*-

# Import from standard library
import os
import moo
import pandas as pd
# Import from our lib
from moo.lib import moo
import pytest


def test_moo():
    assert type(moo()) == str
    assert moo() == "Mooooooo..."
