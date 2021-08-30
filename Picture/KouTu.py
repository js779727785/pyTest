import os
import paddlehub as hub
"""
原人像图放在img下，抠图结果存在：代码同级目录的 humanseg_output目录下，默认安的1.2.0不兼容，指定1.0.0
"""
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg',version='1.0.0')
base_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(base_dir, 'img/')
files = [path + i for i in os.listdir(path)]
results = humanseg.segmentation(data={'image': files})