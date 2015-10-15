#!/usr/bin/python

import unittest
import solve


class TestKeplerSolver(unittest.TestCase):
    def test_eccentric_anomaly_solver(self):
        self.assertEqual(0.0,solve.solve_for_eccentric_anomaly(0,0))
        self.assertEqual(1.0885977582695519,solve.solve_for_eccentric_anomaly(1,0.1))
        self.assertEqual(1.8620866869674508,solve.solve_for_eccentric_anomaly(1,0.9))

if __name__=='__main__':
    unittest.main()
