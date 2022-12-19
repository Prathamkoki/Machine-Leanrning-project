from setuptools import setup
from typing import List

#Description variables for setup function
PROjECT_NAME="housing_prediction"
VERSION="0.0.1"
AUTHOR="Prathamesh Kokitkar"
DESCRIPTION="This is my first ML project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Desription:This function is going to return list of requirments mention in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()
setup(
name=PROjECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)