"""
    tests for Sectxt and txtsec
"""

from secondstotext import Sectxt, txtsec

testparm = [48646,37065900.007,36806700.000,5270700.007,0.007]

testparm2 = ["1y, 2M, 3d, 4h, 5m, 6s, 7ms",
            "1 Year, 2 Months, 3 Days, 4 Hours, 5 Minutes, 6 Seconds, 7 ms",
            "3 Days, 4 Hours, 5 Minutes, 6 Seconds, 7 ms",
            "4 Hours, 0 Minutes, 0 Seconds, 7 ms",
            "3 m, 3 Minutes, 0 m, 7 M"]

testanswers2 = [37065906.007,
                37065906.007,
                273906.007,
                14400.007,
                18396360.0]

def test_txtsec():
    """
        test for txtsec
    """
    for count, i in enumerate(testparm2):
        assert testanswers2[count] == txtsec(i)

def test_sectxtandtxtsec():
    """
        test for Sectxt and back to txtsec
    """
    for i in testparm:
        assert float(i) == txtsec(Sectxt(i).default())

def test_sectxttypes():
    """
        test for Sectxt output types
    """
    assert Sectxt(3750900.007).showall() == \
        "0 Years, 1 Month, 12 Days, 23 Hours, 55 Minutes, 0 Seconds, 7ms"
    assert Sectxt(3750900.007).showzeros() == \
        "1 Month, 12 Days, 23 Hours, 55 Minutes, 0 Seconds, 7ms"
    assert Sectxt(3750900.007).rawtuple() == \
        (0, 1, 12, 23, 55, 0, 7)
    assert Sectxt(3750900.007).default() == \
        "1 Month, 12 Days, 23 Hours, 55 Minutes, 7ms"
