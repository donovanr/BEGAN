import tensorflow as tf
import prettytensor as pt
from utils import custom_ops

if False:  # This to silence pyflake
    custom_ops


def began_discriminator(D_I, batch_size, hidden_size,
                        scope_name="discriminator", reuse_scope=False):
    '''
    Unlike most generative adversarial networks, the boundary
    equilibrium interestingly uses an *autoencoder* in place of the
    regular 'discriminator'.

    For simplicity, the decoder architecture is the same as the generator.

    Effectively, downsampling is just 3x3 convolutions with a stride of 2,
    while upsampling is 3x3 convolutions, with nearest neighbour resizing
    to the desired resolution.

    Args:
        D_I: a batch of images [batch_size, 128 x 128 x 3]
        batch_size: Batch size of encodings
        hidden_size: Dimensionality of encoding
        scope_name: Tensorflow scope name
        reuse_scope: Tensorflow scope handling
    Returns:
        Flattened tensor of re-created images, with dimensionality:
            batch_size * 128 * 128 * 3
    '''

    n = 128  # 'n' is number of filters
    with tf.variable_scope(scope_name) as scope:
        if reuse_scope:
            scope.reuse_variables()

        layer_1 = (pt.wrap(D_I)
                   .reshape([-1, 128, 128, 3]))  # '-1' is batch size

        conv_0 = (layer_1
                  .custom_conv2d(3, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        conv_1 = (conv_0
                  .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        conv_2 = (conv_1
                  .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        layer_2 = (conv_2
                   .conv2d(3, 2 * n, stride=2)
                   .apply(tf.nn.elu))

        conv_3 = (layer_2
                  .custom_conv2d(2 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        conv_4 = (conv_3
                  .custom_conv2d(2 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        layer_3 = (conv_4
                   .conv2d(3, 3 * n, stride=2)
                   .apply(tf.nn.elu))

        conv_5 = (layer_3
                  .custom_conv2d(3 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        conv_6 = (conv_5
                  .custom_conv2d(3 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        layer_4 = (conv_6
                   .conv2d(3, 4 * n, stride=2)
                   .apply(tf.nn.elu))

        conv_7 = (layer_4
                  .custom_conv2d(4 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        conv_8 = (conv_7
                  .custom_conv2d(4 * n, k_h=3, k_w=3, d_h=1, d_w=1)
                  .apply(tf.nn.elu))

        layer_5 = (conv_8
                   .flatten()
                   .fully_connected(hidden_size, activation_fn=tf.nn.elu))

        decode_layer_1 = (layer_5  # (hidden_size)
                          .flatten()
                          .fully_connected(16 * 16 * n, activation_fn=tf.nn.elu)
                          #.fc_batch_norm()
                          .reshape([-1, 16, 16, n]))  # '-1' is batch size

        decode_conv_1 = (decode_layer_1
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_conv_2 = (decode_conv_1
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_layer_2 = (decode_conv_2
                          .apply(tf.image.resize_nearest_neighbor, [32, 32]))

        decode_conv_3 = (decode_layer_2
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_conv_4 = (decode_conv_3
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_layer_3 = (decode_conv_4
                          .apply(tf.image.resize_nearest_neighbor, [64, 64]))

        decode_conv_5 = (decode_layer_3
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_conv_6 = (decode_conv_5
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_layer_4 = (decode_conv_6
                          .apply(tf.image.resize_nearest_neighbor, [128, 128]))

        decode_conv_7 = (decode_layer_4
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .apply(tf.nn.elu))

        decode_conv_8 = (decode_conv_7
                         .custom_conv2d(n, k_h=3, k_w=3, d_h=1, d_w=1)
                         .conv_batch_norm()
                         .apply(tf.nn.elu))

        decode_conv_9 = (decode_conv_8
                         .custom_conv2d(3, k_h=3, k_w=3, d_h=1, d_w=1)
                         .apply(tf.sigmoid))

        return decode_conv_9.flatten()
