# test_coinledger.py
"""
Tests for CoinLedger module.
"""

import unittest
from coinledger import CoinLedger

class TestCoinLedger(unittest.TestCase):
    """Test cases for CoinLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinLedger()
        self.assertIsInstance(instance, CoinLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
