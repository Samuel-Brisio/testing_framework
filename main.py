from TestFramework.TestLoader import TestLoader
from TestFramework.TestSuite import TestSuite
from TestFramework.TestRunner import TestRunner

from Test.TestLoaderTest import TestLoaderTest
from Test.TestSuiteTest import TestSuiteTest
from Test.TestCaseTest import TestCaseTest

if __name__ == "__main__":
    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)