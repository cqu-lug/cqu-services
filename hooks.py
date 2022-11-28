import os
import shutil

def add_cname(config, **kwargs):
    site_dir = config['site_dir']
    shutil.copy('CNAME', os.path.join(site_dir, 'CNAME'))
