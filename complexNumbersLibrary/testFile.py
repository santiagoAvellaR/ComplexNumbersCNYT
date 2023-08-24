import complexNumbersLibrary as lc
import unittest

class CmplxOperations(unittest.TestCase):

    def test_cmplxSum(self):
        # ejemplo 1. (-3.2, 6.4) y (5.8, -3.5)
        self.assertEqual(lc.sumCmplx((-3.2, 6.4),(5.8, -3.5)),(2.6, 2.9))
        self.assertEqual(lc.restCmplx((-3.2, 6.4),(5.8, -3.5)), (-9, 9.9))
        self.assertEqual(lc.multiCmplx((-3.2, 6.4),(5.8, -3.5)), (3.84, 48.32))
        self.assertEqual(lc.divCmplx((-3.2, 6.4),(5.8, -3.5)), (-0.77, 0.49))
        self.assertAlmostEqual(lc.modCmplx((-3.2, 6.4)), 7.16)
        self.assertEqual(lc.conjCmplx((-3.2, 6.4)), (-3.2, -6.4))
        self.assertAlmostEqual(lc.phaseCmplx((-3.2, 6.4)), 2.03)
        self.assertEqual(lc.polarCmplx((-3.2, 6.4)), (7.16, 2.03))
        # ejemplo 2. (3, 1.5) y (-2.5, -1.5)
        self.assertEqual(lc.sumCmplx((3, 1.5),(-2.5, -1.5)),(0.5, 0))
        self.assertEqual(lc.restCmplx((3, 1.5),(-2.5, -1.5)), (5.5, 3))
        self.assertEqual(lc.multiCmplx((3, 1.5),(-2.5, -1.5)), (-5.25, -8.25))
        self.assertEqual(lc.divCmplx((3, 1.5),(-2.5, -1.5)), (-2.17, 0.17))
        self.assertAlmostEqual(lc.modCmplx((3, 1.5)), 3.35)
        self.assertEqual(lc.conjCmplx((3, 1.5)), (3, -1.5))
        self.assertAlmostEqual(lc.phaseCmplx((3, 1.5)), 0.46)
        self.assertEqual(lc.polarCmplx((3, 1.5)), (3.35, 0.46))
if __name__ == '__main__':
    unittest.main()