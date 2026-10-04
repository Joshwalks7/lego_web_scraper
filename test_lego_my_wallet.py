from lego_my_wallet import get_vendor_list, get_lego_set
from unittest.mock import patch
import pytest

def test_get_vendor_list():
    # assert the order of the prices from least to greatest
    d1 = {12345: ('Star Wars Set', 100),
          12346: ('Star Wars Set', 101),
          12347: ('Star Wars Set', 99.00)} #Balmart
    d2 = {12345: ('Star Wars Set', 99.99),
          12346: ('Star Wars Set', 99.99)} #Camazon
    d3 = {12345: ('Star Wars Set', 99.00)} #marget

    result1 = get_vendor_list(12345, d1, d2, d3)

    stores = list(result1.keys())
    assert len(stores) == 3
    assert stores[0] == 'Marget'
    assert stores[2] == 'Balmart'

    result1 = get_vendor_list(12346, d1, d2, d3)

    stores = list(result1.keys())
    assert len(stores) == 2
    assert stores[0] == 'Camazon'
    assert stores[1] == 'Balmart'

    result1 = get_vendor_list(12347, d1, d2, d3)

    stores = list(result1.keys())
    assert len(stores) == 1
    assert stores[0] == 'Balmart'

def test_get_lego_set():
    d1 = {12345: ('Star Wars Set', 100),
          12346: ('Star Wars Set', 101),
          12347: ('Star Wars Set', 99.00)} #Balmart
    d2 = {12345: ('Star Wars Set', 99.99),
          12346: ('Star Wars Set', 99.99)} #Camazon
    d3 = {12345: ('Star Wars Set', 99.00)} #marget

    with patch('builtins.input', side_effect=['0', '12345']) as mocked_input:
        result1 = get_lego_set(d1, d2, d3)
    
    assert result1 == 12345
    assert mocked_input.call_count == 2

    with patch('builtins.input', side_effect=['12346']) as mocked_input:
        result2 = get_lego_set(d1, d2, d3)
    
    assert result2 == 12346
    assert mocked_input.call_count == 1

pytest.main(["-v", "--tb=line", "-rN", __file__])