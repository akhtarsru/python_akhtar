# test_factorial.py

from your_script_name import factorial  # Replace 'your_script_name' with the actual name of your script

def test_factorial_for_zero():
    assert factorial(0) == 1

def test_factorial_for_one():
    assert factorial(1) == 1

def test_factorial_for_positive_integer():
    assert factorial(5) == 120

def test_factorial_for_negative_number():
    # Assuming the function handles negative numbers gracefully by returning None or some sentinel value
    assert factorial(-5) is None

# Add more test cases as needed
