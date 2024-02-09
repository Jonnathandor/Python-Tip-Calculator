import pytest
from tip_calculator import calculate_tip

def test_calculate_tip():
    assert calculate_tip(100, 4) == 3.75
    assert calculate_tip(200, 2, 20) == 20.0
    assert calculate_tip(85.50, 3, 10) == 2.85
    with pytest.raises(ValueError):
        calculate_tip('abc', 2)
    with pytest.raises(ValueError):
        calculate_tip(100, 'xyz')
    with pytest.raises(ValueError):
        calculate_tip(100, 2, 'ten percent')