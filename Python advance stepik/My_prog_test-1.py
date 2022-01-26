import pytest
from myprog import main

@pytest.mark.parametrize("n1,n2,exp", [
    (1, 2, 3),
    (3, 8, 11),
    ])
def test_main_sum(n1, n2, exp):
    assert main(n1, n2) == exp

