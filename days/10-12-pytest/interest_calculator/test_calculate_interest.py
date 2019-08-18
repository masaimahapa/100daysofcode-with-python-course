from program import calculate_interest

def test_interest_calculator():
    assert calculate_interest(1000, 5, 0.06)== 1338.23
