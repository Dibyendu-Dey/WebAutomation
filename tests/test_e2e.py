import pytest


@pytest.mark.usefixtures("setup")
class TestE2E:
    """
    TestE2E is a Pytest clas to wrap all the Pytest test methods
    """

    def test_radio_button_example(self):
        """Pytest test method to handle radio button in page"""
        pass

    def test_suggestive_dropdown(self):
        """Pytest test method to handle suggestive dropdown in page"""
        pass
