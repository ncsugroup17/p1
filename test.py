import pytest

def test_passing_case():
    # Passing test case
    assert "Hello, Alice" == "Hello, Alice"

def test_failing_case():
    # Failing test case
    assert "Hello, Alice" == "Hi, Alice" 