from nodule import inference_nodule


class Model(object):

    def __init__(self, args):
        pass

    def predict(self, img):
        pass


class NoduleClassifier(Model):

    def __init__(self, params_file):
        self.args = None
        self.model= inference_nodule.load_model(params_file)
        self.index2label={0:'normal', 1:'nodule'}
    def predict(self, img):
        return inference_nodule.predict(img, self.model, self.index2label, self.args)


if __name__ == "__main__":

    classifier = NoduleClassifier('xception_params.pkl')

    test_image = "/wanqi/incubator-singa/I00001019003.jpg"

    prediction = classifier.predict(test_image)

    print(prediction)