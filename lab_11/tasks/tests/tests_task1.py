import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

@pytest.fixture()
def calculator():
    calc = Calculator()
    return calc

@pytest.mark.parametrize('operator, arg1, arg2, expected',
                         [['+', 1, 2, 3],
                          ['+', -1, 2, 1],
                          ['+', 1.5, 2, 3.5],
                          ['-', 1, 1, 0],
                          ['-', -0.5, 1, -1.5],
                          ['*', 2, 2, 4],
                          ['*', 3, -3, -9],
                          ['*', -4, -4, 16],
                          ['*', 2.0, 3.5, 7.0],
                          ['/', 4, 2, 2],
                          ['/', 5.0, 2.0, 2.5]])
def test_run_both_args_parametrize(operator, arg1, arg2, expected, calculator):
    print('test_run_both_args_parametrize <======================= tested code')

    assert calculator.run(operator, arg1, arg2) == expected





