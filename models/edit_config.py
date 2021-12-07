import re
from os import listdir
from optparse import OptionParser

p = OptionParser()
p.add_option('--models_dir')
p.add_option('--download_model_url')
p.add_option('--download_config_url')
options, arguments = p.parse_args()

path = options.models_dir + '/'

config_name = options.download_config_url.rsplit('/', 1)[1] 
model_folder = options.download_model_url.rsplit('/', 1)[1].rsplit('.tar', 1)[0] 

labelmap_path = "/content/dissertacao/data/images/labelmap.pbtxt"
train_record_path = "/content/dissertacao/data/images/train.record"
test_record_path = "/content/dissertacao/data/images/test.record"
num_classes = 1 
batch_size = 8
num_steps = 8000

fine_tune_checkpoint = "/content/dissertacao/models/pretrained/" + model_folder + "/checkpoint/ckpt-0"

if config_name == 'default':
    with open(path + model_folder + '/pipeline.config') as f:
        config = f.read()
else:
    with open(path + config_name) as f:
        config = f.read()

with open(path + model_folder + '/pipeline_file.config', 'w') as f:

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