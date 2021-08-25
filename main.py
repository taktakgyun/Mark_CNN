import tensorflow as tf
import numpy as np

lengh = [170, 180, 175, 160]
shose = [260, 270, 265, 255]

w = tf.Variable(0.1)
b = tf.Variable(0.2)



#xData = [1,2,3,4,5,6,7]
#yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]
#W = tf.Variable(tf.random.uniform([1], -100, 100))
#b = tf.Variable(tf.random.uniform([1], -100, 100))
#X = tf.constant(1.0)
#Y = tf.constant(1.0)
#H = W*X + b
#cost = tf.reduce_mean(tf.square(H-Y))
#a = tf.Variable(0.01)
#iptimizer = tf.train.