import os

pipeline_config_path = '/home/ubuntu/dissertacao/models/pretrained/efficientdet_d0_coco17_tpu-32/pipeline_file.config'
model_dir = 'experimento/'
num_steps = 8000
num_eval_steps = 1000

os.system("python /home/ubuntu/tensorflow/models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path={} \
    --model_dir={} \
    --alsologtostderr \
    --num_train_steps={} \
    --sample_1_of_n_eval_examples=1 \
    --num_eval_steps={}".format(pipeline_config_path, model_dir, num_steps, num_eval_steps))
