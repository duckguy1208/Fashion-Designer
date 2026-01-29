import unittest
from unittest.mock import patch
import main

class TestFashionBot(unittest.TestCase):
    """
    This class contains unit tests for our Fashion Bot.
    Unit testing involves testing small 'units' of code (like functions) 
    in isolation to make sure they work correctly.
    """

    def test_validate_name_valid(self):
        """Test that valid names return True."""
        # Simple valid case
        self.assertTrue(main.validate_name("Tieler"))
        # Another valid case with extra spaces
        self.assertTrue(main.validate_name("  Jonathan  "))

    def test_validate_name_invalid(self):
        """Test that invalid names return False."""
        # Too short
        self.assertFalse(main.validate_name("A"))
        # Empty string
        self.assertFalse(main.validate_name(""))
        # Numbers are not allowed
        self.assertFalse(main.validate_name("T1eler"))
        # Special characters are not allowed
        self.assertFalse(main.validate_name("Tieler!"))

    def test_get_age_group(self):
        """Test that ages are correctly categorized."""
        # Testing 'boundary' values (like 12, 13, 19, 20) is very important!
        self.assertEqual(main.get_age_group(5), "Child")
        self.assertEqual(main.get_age_group(12), "Child")
        self.assertEqual(main.get_age_group(13), "Teenager")
        self.assertEqual(main.get_age_group(19), "Teenager")
        self.assertEqual(main.get_age_group(20), "Adult")
        self.assertEqual(main.get_age_group(64), "Adult")
        self.assertEqual(main.get_age_group(65), "Senior")
        
        # Testing 'edge case' (negative age)
        self.assertEqual(main.get_age_group(-1), "Invalid")

    def test_get_hat_feedback(self):
        """Test hat feedback logic."""
        # Test positive response with specific types
        self.assertEqual(main.get_hat_feedback("yes", "beanie"), "Beanies Are Great For The Cold")
        self.assertEqual(main.get_hat_feedback("yes", "baseball hat"), "Baseball Hats Are My Favorite!")
        
        # Test unknown hat type
        self.assertEqual(main.get_hat_feedback("yes", "top hat"), "Not My First Choice But Its Still Good")
        
        # Test negative response
        self.assertEqual(main.get_hat_feedback("no"), "That's Okay")
        
        # Test mixed case input (proving we handle .lower() correctly)
        self.assertEqual(main.get_hat_feedback(" YES ", "BeAnIe"), "Beanies Are Great For The Cold")

    def test_get_bottom_feedback(self):
        """Test bottom feedback logic."""
        self.assertEqual(main.get_bottom_feedback("cargo pants"), "I Also Like Cargo Pants.")
        self.assertEqual(main.get_bottom_feedback("sweatpants"), "Sweatpants Are My Favorite!")
        self.assertEqual(main.get_bottom_feedback("swimsuit"), "Beach Day!!!")
        self.assertEqual(main.get_bottom_feedback(""), "Weird")
        self.assertEqual(main.get_bottom_feedback("jeans"), "You Can’t Go Wrong With jeans.")

    def test_get_top_feedback_fixed(self):
        """
        This test shows how to handle functions that use randomness.
        We use 'mocking' to force random.choice to return a specific value.
        """
        with patch('random.choice') as mocked_choice:
            mocked_choice.return_value = "That's a good choice."
            
            result = main.get_top_feedback("Hoodie")
            
            self.assertEqual(result, "That's a good choice.")
            # Check that the function actually called random.choice
            mocked_choice.assert_called_once()

    def test_get_top_feedback_empty(self):
        """Test empty top input."""
        self.assertEqual(main.get_top_feedback(""), "Beach Day?")

if __name__ == '__main__':
    unittest.main()
