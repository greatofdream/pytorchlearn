import numpy as np
import os
import random
from scipy import misc

def LoadDataMeta(num_metatrain_classes = 1000, num_samples_per_metatrain_class = 20, num_metatest_classes = 50, num_samples_per_metatest_class_training = 1, num_samples_per_metatest_class_testing = 10, seed = 1):
    """
    Load data, split the classes into meta-training and meta-testing; for meta-testing classes, split samples into training and testing
    Args:
        num_metatrain_classes: number of classes used for meta-training
        num_samples_per_metatrain_class: number of samples for meta-training classes
        num_metatest_classes: number of classes used for meta-testing
        num_samples_per_metatest_class_training: number of samples per meta-test class used for training
        num_samples_per_metatest_class_testing: number of samples per meta-test class used for testing
        seed: random seed to ensure consistent results
    Returns:
        a tuple of (1) images for meta-training (2) labels for meta-training (3) images for training in the meta-testing class (4) labels for training in the meta-testing class
                                                                             (5) images for testing in the meta-testing class (6) labels for testing in the meta-testing class
            (1) numpy array of shape [num_metatrain_classes * num_samples_per_metatrain_class, 784], binary pixels
            (2) numpy array of shape [num_metatrain_classes * num_samples_per_metatrain_class], integers of the class label
            (3) numpy array of shape [num_metatest_classes * num_samples_per_metatest_class_training, 784], binary pixels
            (4) numpy array of shape [num_metatest_classes * num_samples_per_metatest_class_training], integers of the class label
            (5) numpy array of shape [num_metatest_classes * num_samples_per_metatest_class_testing, 784], binary pixels
            (6) numpy array of shape [num_metatest_classes * num_samples_per_metatest_class_testing], integers of the class label
    """
    random.seed(seed)
    np.random.seed(seed)
    num_classes = num_metatrain_classes + num_metatest_classes
    assert num_classes <= 1623
    num_samples_per_metatest_class = num_samples_per_metatest_class_training + num_samples_per_metatest_class_testing
    num_samples_per_class = max(num_samples_per_metatrain_class, num_samples_per_metatest_class)
    assert num_samples_per_class <= 20
    dim_input = 28 * 28
    
    # construct folders
    data_folder = './omniglot_resized'
    character_folders = [os.path.join(data_folder, family, character)
                         for family in os.listdir(data_folder)
                         if os.path.isdir(os.path.join(data_folder, family))
                         for character in os.listdir(os.path.join(data_folder, family))
                         if os.path.isdir(os.path.join(data_folder, family, character))]
    random.shuffle(character_folders)
    character_folders_metatest = character_folders[: num_classes]
    
    # read images
    all_images = np.zeros(shape = (num_samples_per_class, num_classes, dim_input))
    all_labels = np.zeros(shape = (num_samples_per_class, num_classes))
    label_images = get_images(character_folders, list(range(num_classes)), nb_samples = num_samples_per_class, shuffle = True)
    temp_count = np.zeros(num_classes, dtype=int)
    for label,imagefile in label_images:
        temp_num = temp_count[label]
        all_images[temp_num, label, :] = image_file_to_array(imagefile, dim_input)
        all_labels[temp_num, label] = label
        temp_count[label] += 1
    
    # split and random permutate
    metatrain_image = all_images[:num_samples_per_metatrain_class,:num_metatrain_classes,:].reshape(-1,dim_input)
    metatrain_label = all_labels[:num_samples_per_metatrain_class,:num_metatrain_classes].reshape(-1)
    metatest_image_training  = all_images[:num_samples_per_metatest_class_training,num_metatrain_classes:num_classes,:].reshape(-1,dim_input)
    metatest_label_training  = all_labels[:num_samples_per_metatest_class_training,num_metatrain_classes:num_classes].reshape(-1)
    metatest_image_testing  = all_images[num_samples_per_metatest_class_training:num_samples_per_metatest_class,num_metatrain_classes:num_classes,:].reshape(-1,dim_input)
    metatest_label_testing  = all_labels[num_samples_per_metatest_class_training:num_samples_per_metatest_class,num_metatrain_classes:num_classes].reshape(-1)
    
    metatrain_image, metatrain_label = pair_shuffle(metatrain_image, metatrain_label)
    metatest_image_training, metatest_label_training = pair_shuffle(metatest_image_training, metatest_label_training)
    metatest_image_testing, metatest_label_testing = pair_shuffle(metatest_image_testing, metatest_label_testing)
    return metatrain_image, metatrain_label, metatest_image_training, metatest_label_training, metatest_image_testing, metatest_label_testing
 
 
def get_images(paths, labels, nb_samples=None, shuffle=True):
    """
    Takes a set of character folders and labels and returns paths to image files
    paired with labels.
    Args:
        paths: A list of character folders
        labels: List or numpy array of same length as paths
        nb_samples: Number of images to retrieve per character
    Returns:
        List of (label, image_path) tuples
    """
    if nb_samples is not None:
        sampler = lambda x: random.sample(x, nb_samples)
    else:
        sampler = lambda x: x
    images_labels = [(i, os.path.join(path, image))
                     for i, path in zip(labels, paths)
                     for image in sampler([pathstr for pathstr in os.listdir(path) if pathstr[-4:] == '.png' ])]
    if shuffle:
        random.shuffle(images_labels)
    return images_labels


def image_file_to_array(filename, dim_input):
    """
    Takes an image path and returns numpy array
    Args:
        filename: Image filename
        dim_input: Flattened shape of image
    Returns:
        1 channel image
    """
    image = misc.imread(filename)
    image = image.reshape([dim_input])
    image = image.astype(np.float32) / 255.0
    image = 1.0 - image
    return image

def pair_shuffle(array_a, array_b):
    """
    Takes an image array and a label array
    Returns:
        the shuffled image array and label array
    """
    temp_perm = np.random.permutation(array_a.shape[0])
    array_a = array_a[temp_perm]
    array_b = array_b[temp_perm]
    return array_a, array_b
    
    