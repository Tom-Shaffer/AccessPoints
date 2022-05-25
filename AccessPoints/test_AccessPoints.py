import AccessPoints as AP


def test_no_connections_necessary():
    matrix = \
    [ 
        [False, True, False, False, True],
        [True, False, True, False, False], 
        [False, True, False, True, False], 
        [False, False, True, False, False], 
        [True, False, False, False, False] 
    ]
    assert AP.get_minimum_connections(matrix) == 0, "Should require no connections"

def test_some_connections_necessary():
    matrix = \
    [ 
        [True, False, False, False, False],
        [False, False, True, False, False], 
        [False, True, False, False, False],
        [False, False, False, False, True], 
        [False, False, False, True, False] 
    ]
    assert AP.get_minimum_connections(matrix) == 2, "Should require 2 connections"

if __name__ == "__main__":
    test_no_connections_necessary()
    test_some_connections_necessary()
    print("Access Points Tests Passed!")