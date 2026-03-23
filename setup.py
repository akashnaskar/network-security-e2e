from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns the list of reuqirements
    """
    requirement_lst: List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("reuirements.txt file not found")
    
    return requirement_lst

#Our main aim here is to print the metadata
setup(
    name = "networkSecurity",
    version = "0.0.1",
    author = "Akash Naskar",
    author_email="akashnaskar.hsbc@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements()
)