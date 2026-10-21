import polars as pl
import qlabs

def test_imports():
    assert pl.DataFrame({"x": [1, 2]}).height == 2

    