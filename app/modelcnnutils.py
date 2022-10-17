import librosa
import librosa.display
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

model = tf.keras.models.load_model('models/cnn')
datagen = ImageDataGenerator(rescale=1. / 255.)

def predict_cnn(aud):
    X, sample_rate = librosa.load(aud, sr=None, res_type='kaiser_fast')
    fig = plt.figure(figsize=[1, 1])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=X, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), x_axis='time', y_axis='mel', fmin=50, fmax=280)
    name = "random"
    file = './temp/test/' + str(name) + '.jpg'
    plt.savefig(file, dpi=500, bbox_inches='tight', pad_inches=0)
    plt.close()
    single_generator = datagen.flow_from_directory(directory=r"./temp/", target_size=(64, 64), batch_size=1, class_mode=None, shuffle=False)
    ans = model.predict(single_generator)
    return ans[0].argmax()
