import unittest
from bunch import Bunch
import sys

sys.path.append("..")
from neuropy.agent import Agent
import tensorflow as tf


class TestAgent(unittest.TestCase):
    def setUp(self):
        configuration = Bunch({
            "model": "./example_models/simple_model",
            "data_loader": "./mock_objects/simple_data_loader.py",
            "data": None
        })
        arguments = Bunch({})
        self.agent = Agent(configuration, arguments)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_training(self):
        self.agent.train()
        outputs = self.agent.infer()
        print(outputs)

if __name__ == "__main__":
    unittest.main()
    # agent_test = TestAgent()
    # agent_test.test_training()