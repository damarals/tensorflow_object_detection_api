import re
from os import listdir
from optparse import OptionParser

p = OptionParser()
p.add_option('--models_dir')
options, arguments = p.parse_args()

path = options.models_dir + '/'

config_list = ['centernet_hourglass104_512x512_coco17_tpu-8.config',
               'ssd_efficientdet_d0_512x512_coco17_tpu-8.config',
               'ssd_efficientdet_d4_1024x1024_coco17_tpu-32.config']
models_folder = ['centernet_hg104_512x512_coco17_tpu-8',
                 'efficientdet_d0_coco17_tpu-32',
                 'efficientdet_d4_coco17_tpu-32']
models_folder = [c.rsplit('.tar', 1)[0] for c in models_folder]

labelmap_path = "/content/dissertacao/data/images/labelmap.pbtxt"
train_record_path = "/content/dissertacao/data/images/train.record"
test_record_path = "/content/dissertacao/data/images/test.record"
num_classes = 1 
batch_size = 4
num_steps = 8000

for config_file, config_folder in zip(config_list, models_folder):
  fine_tune_checkpoint = "/content/dissertacao/models/pretrained/" + config_folder + "/checkpoint/ckpt-0"

  with open(path + config_file) as f:
    config = f.read()

  with open(path + config_folder + '/pipeline_file.config', 'w') as f:
    
    # Set labelmap path
    config = re.sub('label_map_path: ".*?"', 
                    'label_map_path: "{}"'.format(labelmap_path), config)
    
    # Set fine_tune_checkpoint path
    config = re.sub('fine_tune_checkpoint: ".*?"',
                    'fine_tune_checkpoint: "{}"'.format(fine_tune_checkpoint), config)
    
    # Set train tf-record file path
    config = re.sub('(input_path: ".*?)(PATH_TO_BE_CONFIGURED/train)(.*?")', 
                    'input_path: "{}"'.format(train_record_path), config)
    
    # Set test tf-record file path
    config = re.sub('(input_path: ".*?)(PATH_TO_BE_CONFIGURED/val)(.*?")', 
                    'input_path: "{}"'.format(test_record_path), config)
    
    # Set number of classes.
    config = re.sub('num_classes: [0-9]+',
                    'num_classes: {}'.format(num_classes), config)
    
    # Set batch size
    config = re.sub('batch_size: [0-9]+',
                    'batch_size: {}'.format(batch_size), config)
    
    # Set training steps
    config = re.sub('num_steps: [0-9]+',
                    'num_steps: {}'.format(num_steps), config)
    
    # Set fine-tune checkpoint type to detection
    config = re.sub('fine_tune_checkpoint_type: "classification"', 
                    'fine_tune_checkpoint_type: "{}"'.format('detection'), config)
    
    f.write(config)