import pytest

from library import StateReporter


def test_init():
    # This test case ensures that the StateReporter class can be initialized with valid parameters.
    #
    # Expected result:
    #
    # The StateReporter class should be initialized with the specified module name, application name, state, and description.

    reporter = StateReporter(module_name="Test_Module", application_name="Test_app")
    assert reporter.module_name == "Test_Module"
    assert reporter.application_name == "Test_app"
    assert reporter.state == "0"
    assert reporter.desc == ""


def test_set_value():
    # This test case ensures that the StateReporter class can set a value for a given function name and description.
    #
    # Expected result:
    #
    # The StateReporter class should set the value for the specified function name and description.

    reporter = StateReporter(module_name="Test_Module", application_name="Test_app")
    reporter.set_value(3.0, function_name="Test_Function", description="3.0")
    assert reporter.state == "0"
    assert reporter.desc == "3.0"


def test_stop():
    # This test case ensures that the StateReporter class can stop the reporting process.
    #
    # Expected result:
    #
    # The StateReporter class should stop the reporting process.

    reporter = StateReporter(module_name="Test_Module", application_name="Test_app")
    reporter.stop()
    assert reporter.state == "3"


def test_bad_init():
    # This test case ensures that the StateReporter class raises a ValueError exception if it is initialized with invalid parameters.
    #
    # Expected result:
    #
    # The StateReporter class should raise a ValueError exception.

    with pytest.raises(ValueError):
        StateReporter(module_name="", application_name="Test_app")


def test_bad_set_value():
    # This test case ensures that the StateReporter class raises a ValueError exception if it is set a value for a function name with no description.
    #
    # Expected result:
    #
    # The StateReporter class should raise a ValueError exception.

    reporter = StateReporter(module_name="Test_Module", application_name="Test_app")
    with pytest.raises(ValueError):
        reporter.set_value(3.0, function_name="", description="3.0")
    with pytest.raises(ValueError):
        reporter.set_value(3.0, function_name="Test_Function", description="")
    with pytest.raises(ValueError):
        reporter.set_value(3.0, function_name="Test_Function", description="3.0")


def test_bad_stop():
    # This test case ensures that the StateReporter class raises a ValueError exception if it is stopped twice.
    #
    # Expected result:
    #
    # The StateReporter class should raise a ValueError exception.

    reporter = StateReporter(module_name="Test_Module", application_name="Test_app")
    reporter.stop()
    with pytest.raises(ValueError):
        reporter.stop()


if __name__ == "__main__":
    pytest.main()
