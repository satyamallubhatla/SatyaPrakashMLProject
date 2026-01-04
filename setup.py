from setuptools import find_packages,setup
from typing import list

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    HYPEN_E_DOT='-e .'

    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

      

setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Satya Prakash Mallubhatla',
    author_email='satya.mallubhatla@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')

)