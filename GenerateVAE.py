import os
import keras
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import backend as K
from keras.layers import Input, Dense, Conv2D, Conv2DTranspose, Flatten, Lambda, Reshape
from keras.models import Model
from keras.losses import binary_crossentropy
from keras.datasets import cifar100
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences


np.random.seed(25)
tf.compat.v1.disable_eager_execution()

# Kullanıcının girdiği prompt'ın okunması
with open("userprompt", 'r') as dosyaPrompt:
    userPrompt = dosyaPrompt.read()

# Kullanıcının belirlediği adım sayısının okunması
with open("useradimsayisi", "r") as dosyaAdimSayisi:
    adimSayisi = int(dosyaAdimSayisi.read())

# Seed değerinin okunması
with open("seed", "r") as dosyaSeed:
    mainSeed = int(dosyaSeed.read())

# CIFAR-10 veri setinin yüklenmesi
(X_train, y_train), (X_test, y_test) = keras.datasets.cifar100.load_data()

# Veri setinin normalize edilmesi
X_train = X_train / 255
X_test = X_test / 255

# Giriş görüntülerinin boyutları"
img_height = X_train.shape[1]  # 32
img_width = X_train.shape[2]   # 32
num_channels = X_train.shape[3]  # 3 (RGB)

# Giriş şekli
input_shape = (img_height, img_width, num_channels)

# Latent uzay boyutu
latent_dim = 2

# VAE Modeli
def build_vae_model(input_shape, latent_dim):
    # ENCODER
    encoder_input = Input(shape=input_shape)
    encoder_conv = Conv2D(filters=8, kernel_size=3, strides=2, padding='same', activation='relu')(encoder_input)
    encoder_conv = Conv2D(filters=16, kernel_size=3, strides=2, padding='same', activation='relu')(encoder_conv)
    encoder = Flatten()(encoder_conv)

    mu = Dense(latent_dim)(encoder)
    sigma = Dense(latent_dim)(encoder)

    def compute_latent(x):
        mu, sigma = x
        batch = K.shape(mu)[0]
        dim = K.int_shape(mu)[1]
        eps = K.random_normal(shape=(batch,dim), seed=mainSeed)
        return mu + K.exp(sigma/2) * eps

    latent_space = Lambda(compute_latent, output_shape=(latent_dim,))([mu, sigma])

    conv_shape = K.int_shape(encoder_conv)

    # DECODER
    decoder_input = Input(shape=(latent_dim,))
    decoder = Dense(conv_shape[1]*conv_shape[2]*conv_shape[3], activation='relu')(decoder_input)
    decoder = Reshape((conv_shape[1], conv_shape[2], conv_shape[3]))(decoder)
    decoder_conv = Conv2DTranspose(filters=16, kernel_size=3, strides=2, padding='same', activation='relu')(decoder)
    decoder_conv = Conv2DTranspose(filters=8, kernel_size=3, strides=2, padding='same', activation='relu')(decoder_conv)
    decoder_conv = Conv2DTranspose(filters=num_channels, kernel_size=3, padding='same', activation='sigmoid')(decoder_conv)

    encoder_model = Model(encoder_input, latent_space)
    decoder_model = Model(decoder_input, decoder_conv)

    vae_model = Model(encoder_input, decoder_model(encoder_model(encoder_input)))

    return vae_model, encoder_model, decoder_model

vae_model, encoder_model, decoder_model = build_vae_model(input_shape, latent_dim)

# LOSS FUNCTION
def kl_reconstruction_loss(true, pred):
    sigma= encoder_model.layers[-2].output
    mu = encoder_model.layers[-1].output
    reconstruction_loss = binary_crossentropy(K.flatten(true), K.flatten(pred)) * img_width * img_height
    kl_loss = 1 + sigma - K.square(mu) - K.exp(sigma)
    kl_loss = K.sum(kl_loss, axis=-1)
    kl_loss *= -0.5
    return K.mean(reconstruction_loss + kl_loss)

vae_model.compile(optimizer='adam', loss=kl_reconstruction_loss)

# Eğitim
history = vae_model.fit(x=X_train, y=X_train, epochs=20, batch_size=32, validation_data=(X_test, X_test))

# Loss grafiği
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

# Encoder çıkışları alınır
encoded = encoder_model.predict(X_train)

# Metin prompt'ının işlenmesi
tokenizer = Tokenizer()
tokenizer.fit_on_texts([userPrompt])
prompt_sequence = tokenizer.texts_to_sequences([userPrompt])
max_sequence_length = max(len(seq) for seq in prompt_sequence)
processed_prompt = pad_sequences(prompt_sequence, maxlen=max_sequence_length)

# Başlangıç ve bitiş noktaları belirlenir
start_point = np.array([0, 2])
end_point = np.array([2, 0])


def generate_and_save_image(x_start, y_start, x_end, y_end, num_images, output_folder="GeneratedImages"):
    x_axis = np.linspace(x_start, x_end, num_images)
    y_axis = np.linspace(y_start, y_end, num_images)

    x_axis = x_axis[:, np.newaxis]
    y_axis = y_axis[:, np.newaxis]

    new_points = np.hstack((x_axis, y_axis))
    new_images = decoder_model.predict(new_points)
    #new_images = new_images.reshape(new_images.shape[0], new_images.shape[1], new_images.shape[2])
    new_images = new_images.reshape(new_images.shape[0], img_height, img_width, num_channels)

    # En sonuncu görüntüyü kaydet
    final_image_path = os.path.join(output_folder, "imageVAE.png")
    plt.imsave(final_image_path, new_images[-1], cmap='gray')

    # Diğer adımlardaki görüntüleri kaydet
    """""for i in range(num_images):
        image_path = os.path.join(output_folder, f"image_{i}.png")
        plt.imsave(image_path, new_images[i], cmap='gray')"""""

generate_and_save_image(0, 2, 2, 0, adimSayisi)