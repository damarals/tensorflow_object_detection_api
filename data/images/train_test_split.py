from optparse import OptionParser
from shutil import copyfile
from os import listdir, makedirs
from os.path import isfile, join, dirname
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

p = OptionParser()
p.add_option('--image_dir')
p.add_option('--random_seed')
options, arguments = p.parse_args()

path = options.image_dir + '/'
file_list = [f for f in listdir(path) if isfile(join(path, f))]
file_names = np.unique([fl.rsplit('.', 1)[0] for fl in file_list])

da_files = pd.DataFrame({
    'path_image': [fl + '.jpg' for fl in file_names],
    'path_xml': [fl + '.xml' for fl in file_names],
    'group': [fl.rsplit('_', 1)[0] for fl in file_names]
})

train, test = train_test_split(da_files, test_size = 0.25, 
                               stratify = da_files.group, 
                               random_state = int(options.random_seed))

makedirs(dirname('train/'), exist_ok = True)
makedirs(dirname('test/'), exist_ok = True)

for rw in range(len(train)):
  copyfile(path + train.iloc[rw, 0], 'train/' + train.iloc[rw, 0])
  copyfile(path + train.iloc[rw, 1], 'train/' + train.iloc[rw, 1])

for rw in range(len(test)):
  copyfile(path + test.iloc[rw, 0], 'test/' + test.iloc[rw, 0])
  copyfile(path + test.iloc[rw, 1], 'test/' + test.iloc[rw, 1])