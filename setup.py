from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements

    '''

    requirements = []

    with open(file_path) as file_obj:

        requirements = file_obj.readlines()
        # List comprehension to remove \n which is read from the requirements.txt file
        requirements = [req.replace("\n","")for req in requirements]

        # removing -e . as it is only used to connect the requirements file to the setup.py file
        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        


        

setup(

name = 'mlproject_basics',
version = '0.0.1',
author = 'Samrajya Basnyat',
author_email='samrajyabasnyat64@gmail.com',
packages=find_packages(),
# install_requires=['pandas', 'numpy', 'seaborn']

install_requires = get_requirements('requirements.txt')


)