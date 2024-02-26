from smt.surrogate_models.surrogate_model import SurrogateModel
import egobox as egx

class GPX(SurrogateModel):
    name = "GPX"

    def _initialize(self):
        super(self)._initialize()

        self.supports = supports = {}
        supports["variances"]= True
        self.gpx = None

    def _train(self):
        xt, yt = self.training_points[None][0]
        gpx = egx.GpMix().fit(xt, yt)
        return gpx

    def _predict_values(self, xt):
        y = self.gpx.predict_values(xt)

    def predict_variances(self, xt):
        s2 = self.gpx.predict_variances(xt)