# import libraries
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import flags
from utils_meta import *

# define settings
FLAGS = flags.FLAGS
flags.DEFINE_integer('num_metatrain_classes', 1000, 'number of meta-train classes')
flags.DEFINE_integer('num_samples_metatrain', 20, 'number of samples per meta-train class used for meta-training')
flags.DEFINE_integer('num_metatest_classes',50, 'number of meta-test classes')
flags.DEFINE_integer('num_samples_metatest_train', 1, 'number of samples per meta-test class used for meta-test-training, i.e., adapation')
flags.DEFINE_integer('num_samples_metatest_test', 10, 'number of samples per meta-test class used for final testing')
flags.DEFINE_integer('seed', 1, 'random seed')
# in the meta-learning language, the above example is a 50-way-1-shot learning setting 

# define you model, loss functions, hyperparameters, and optimizers
### Your Code Here ###



# load data
metatrain_image, metatrain_label, metatest_image_training, metatest_label_training, metatest_image_testing, metatest_label_testing = LoadDataMeta(FLAGS.num_metatrain_classes, FLAGS.num_samples_metatrain, FLAGS.num_metatest_classes, FLAGS.num_samples_metatest_train, FLAGS.num_samples_metatest_test, FLAGS.seed)
# note: you should use metatrain_image, metatrain_label to meta-train, then use metatest_image_training, metatest_label_training to adapt, and finally evalute on metatest_image_testing, metatest_label_testing
# also note that, metatrain_label is [0,num_metatrain_classes), metatest_label_training/test is [num_metatrain_classes, num_metatrain_classes + num_metatest_classes) 

with tf.Session() as sess:
    # initialize 
    sess.run(tf.local_variables_initializer())
    sess.run(tf.global_variables_initializer())
    
    # metatrain model using metatrain_image and metatrain_label
    ### Your Code Here ###
    
    
    # use metatest_image_training and metatest_label_training to adapt
    ### Your Code Here ###
    
    
    # get predictions on metatest_image_testing
    ### Your Code Here ###
    pred = None
    
    
    # evaluation
    print("Final Test Accuracy:", np.mean(1.0 * (pred == metatest_label_testing)))
    # note that you should not use metatest_label_testing elsewhere






