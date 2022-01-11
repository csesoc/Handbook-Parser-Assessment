"""
====================TESTS====================
You may add your own tests if you would like. We will run our much more extensive
hidden tests on your submission.
"""
from hard import is_unlocked

def test_empty():
    assert is_unlocked([], "COMP1511") == True
    assert is_unlocked([], "COMP9301") == False
    print("Tested empty and works")

def test_single():
    assert is_unlocked(["MATH1081"], "COMP3153") == True
    assert is_unlocked(["ELEC2141"], "COMP3211") == True
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531"], "COMP3153") == False
    print("Tested single and works")

def test_compound():
    assert is_unlocked(["MATH1081", "COMP1511"], "COMP2111") == True
    assert is_unlocked(["COMP1521", "COMP2521"], "COMP3151") == True
    assert is_unlocked(["COMP1917", "DPST1092"], "COMP3151") == False
    print("Tested compound and works")

def test_simple_uoc():
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521"], "COMP4161") == True
    assert is_unlocked(["COMP1511", "COMP1521"], "COMP4161") == False
    print("Tested simple uoc and works")

def test_annoying_uoc():
    assert is_unlocked(["COMP9417", "COMP9418", "COMP9447"], "COMP9491") == True
    assert is_unlocked(["COMP6441"], "COMP9302") == False
    assert is_unlocked(["COMP6441", "COMP64443", "COMP6843", "COMP6445"], "COMP9302") == True
    assert is_unlocked(["COMP1234", "COMP5634", "COMP4834"], "COMP9491") == False
    assert is_unlocked(["COMP3901"], "COMP3902") == False
    assert is_unlocked(["COMP3901", "COMP6441", "COMP6443"], "COMP3902") == False
    assert is_unlocked(["COMP3901", "COMP3441", "COMP3443"], "COMP3902") == True
    print("Tested annoying uoc and works")

def test_cross_discipline():
    assert is_unlocked(["COMP1911", "MTRN2500"], "COMP2121") == True
    assert is_unlocked(["COMP1521"], "COMP2121") == True
    print("Tested cross discipline and works")

test_empty()
test_single()
test_compound()
test_simple_uoc()
test_annoying_uoc()
test_cross_discipline()