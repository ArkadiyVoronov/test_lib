import pytest

from library import StateReporter


def test_init():
    reporter = StateReporter("Test_Module", "Test_app")
    assert reporter.module == "Test_Module"
    assert reporter.app == "Test_app"
    assert reporter.state == "0"
    assert reporter.desc == ""


def test_set_value():
    reporter = StateReporter("Test_Module", "Test_app")
    reporter.set_value(3.0, "Test_Function", "3.0")
    assert reporter.state == "0"
    assert reporter.desc == "3.0"


def test_stop():
    reporter = StateReporter("Test_Module", "Test_app")
    reporter.stop()
    assert reporter.state == "3"


if __name__ == "__main__":
    pytest.main()
