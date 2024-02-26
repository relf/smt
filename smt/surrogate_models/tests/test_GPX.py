import unittest
from smt.sampling_methods import LHS
from smt.problems import Sphere
from smt.surrogate_models import GPX

class TestGPX(unittest.TestCase):

    def test_gpx(self):
        ndim = 2
        num = 50
        problem = Sphere(ndim)
        xlimits = problem.xlimits
        sampling = LHS(xlimits=xlimits, criterion="ese")
        
        xt = sampling(num)
        yt = Sphere(ndim)

        sm = GPX()
        sm.set_training_values(xt, yt)
        sm.train()

        sm.predict_values(xt)
        sm.predict_variances(xt)

if __name__ == "__main__":
    unittest.main()
