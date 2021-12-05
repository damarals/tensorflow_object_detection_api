from optparse import OptionParser
from os import makedirs
from os.path import dirname
import wget
from shutil import unpack_archive

p = OptionParser()
p.add_option('--models_dir')
options, arguments = p.parse_args()

makedirs(dirname(options.models_dir + '/'), exist_ok = True)

models_url = ['http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_512x512_coco17_tpu-8.tar.gz',
 'http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d0_coco17_tpu-32.tar.gz',
 'http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz']
models_name = [m.rsplit('/', 1)[1] for m in models_url]

configs_url = ['https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/centernet_hourglass104_512x512_coco17_tpu-8.config',
 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/ssd_efficientdet_d0_512x512_coco17_tpu-8.config',
 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/centernet_hourglass104_1024x1024_coco17_tpu-32.config']
configs_name = [c.rsplit('/', 1)[1] for c in configs_url]


for url, model in zip(models_url, models_name):
  wget.download(url, options.models_dir + '/' + model)
  unpack_archive(options.models_dir + '/' + model, options.models_dir + '/')

for url, config in zip(configs_url, configs_name):
  wget.download(url, options.models_dir + '/' + config)