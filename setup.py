##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


from setuptools import setup
from setuptools import find_packages

setup(
    name='Yaml-Editor',
    version='1.0',
    description='Minimal Flask server to edit yaml files.',
    url='http://github.com/att-comdev/tugboat/utils/',
    python_requires='>=3.5.0',
    license='MIT License',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-bootstrap',
    ],
    entry_points={
        'console_scripts': [
            'yaml-editor=yaml_editor.editor:main',
        ],
    },
    include_package_data=True,
)
