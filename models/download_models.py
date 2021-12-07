from optparse import OptionParser
from os import makedirs
from os.path import dirname
import wget
from shutil import unpack_archive

p = OptionParser()
p.add_option('--model_dir')
p.add_option('--download_model_url')
p.add_option('--download_config_url')
options, arguments = p.parse_args()

makedirs(dirname(options.model_dir + '/'), exist_ok = True)

model_name = options.download_model_url
print(model_name)
model_name = model_name.rsplit('/', 1)[1]
config_name = options.download_config_url
config_name = config_name.rsplit('/', 1)[1]

if options.download_config_url != 'default':
	wget.download(options.download_config_url, options.model_dir + '/' + config_name)

wget.download(options.download_model_url, options.model_dir + '/' + model_name)
unpack_archive(options.model_dir + '/' + model_name, options.model_dir + '/')