import pytest
from evaluation import evaluate

def test_evaluate_positive():
    assert evaluate(10) == "Positive"

def test_evaluate_negative():
    assert evaluate(-5) == "Negative"

def test_evaluate_zero():
    assert evaluate(0) == "Zero"

def test_evaluate_large_positive():
    assert evaluate(1000000) == "Positive"

def test_evaluate_large_negative():
    assert evaluate(-999999) == "Negative"
