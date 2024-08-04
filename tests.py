import pytest
from utils.traverse_by_idx import traverse_by_idx

def test_traverse_by_idx():
    """
    Test to ensure traverse by index works to get clusters
    """

    data = [0,1,0,1,2,3,3,0,5,5,5,9]
    expected = [0,1,0,1,0,1,1,0,1,1,1,1]

    output = traverse_by_idx(data)

    assert output == expected