import unittest
from neuropy.agent import Agent
from bunch import Bunch

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
