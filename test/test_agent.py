import unittest
from bunch import Bunch
import sys
import numpy as np
import operator

sys.path.append("..")
from neuropy.agent import Agent
import tensorflow as tf


class TestAgent(unittest.TestCase):
    def setUp(self):
        configuration = Bunch({
            "model": "./test/example_models/simple_model",
            "data_loader": "./test/mock_objects/simple_data_loader.py",
            "data": None
        })
        arguments = Bunch({})
        self.agent = Agent(configuration, arguments)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_training_loader(self):
        self.agent.train()
        infer = np.array([0.1,0.2,0.3,0.4])
        test_set = tf.data.Dataset.from_tensor_slices(infer).batch(2)
        outputs = np.array(self.agent.infer(test_set)[0]).transpose()[0]
        comparison = outputs-infer
        assert(all(values < 0.05 for values in comparison))

if __name__ == "__main__":
    unittest.main()
    # agent_test = TestAgent()
    # agent_test.test_training()