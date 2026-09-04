from TestFramework.TestLoader import TestLoader
from Test.TestLoaderTest import TestLoaderTest
from TestFramework.TestRunner import TestRunner

if __name__ == "__main__":
    loader = TestLoader()
    suite = loader.make_suite(TestLoaderTest)

    runner = TestRunner()
    runner.run(suite)