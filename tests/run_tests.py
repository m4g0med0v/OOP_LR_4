import unittest

import tests.test_individual_task_1 as individual_task_1
import tests.test_individual_task_2 as individual_task_2
import tests.test_task_1 as task_1

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suites = unittest.TestSuite()

    suites.addTests(loader.loadTestsFromModule(individual_task_1))
    suites.addTests(loader.loadTestsFromModule(individual_task_2))
    suites.addTests(loader.loadTestsFromModule(task_1))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suites)
