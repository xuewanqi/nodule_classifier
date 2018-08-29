from nodule import inference_nodule

import argparse


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
    parser = argparse.ArgumentParser(description='model prediction')

    parser.add_argument('--image_path', type=str, default='',
                        help='path to the inference image. Currently only support inference on a single input image.')
    parser.add_argument('--params','-p', type=str, default='',
                        help='path to the file which stores network parameters.')
    args = parser.parse_args()

    classifier = NoduleClassifier(args.params)

    #test_image = "/wanqi/incubator-singa/I00001019003.jpg"

    prediction = classifier.predict(args.image_path)

    print(prediction)