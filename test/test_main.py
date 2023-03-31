import unittest

loader = unittest.TestLoader()
suite = loader.discover('test', pattern='test_*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
