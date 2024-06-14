import pytest
from Utilities.BaseClass import BaseClass


# @pytest.mark.use-fixtures("setup")  # This statement is no longer needed as parent BaseClass has the idea of setup
class TestE2E(BaseClass):  # Now we are inheriting all the properties and method of the parent Base class
    """
    TestE2E is a Pytest clas to wrap all the Pytest test methods
    """

    def test_radio_button(self):
        """Pytest test method to handle radio button in page"""
        self.get_logger().info("TC: test_radio_button passed")
        print(self.data["TestData"]["RadioButton"])

    def test_suggestive_dropdown(self):
        """Pytest test method to handle suggestive dropdown in page"""
        self.get_logger().info("TC: test_suggestive dropdown passed")
