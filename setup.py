"""OpenMM-ML: A high level API for using machine learning models in OpenMM simulations
"""

from setuptools import setup, find_packages

DOCLINES = __doc__.split("\n")

########################
__version__ = '1.3'
VERSION = __version__
ISRELEASED = False
########################
CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Scientific/Engineering :: Bio-Informatics
Topic :: Scientific/Engineering :: Chemistry
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""


setup(
    name='openmmml',
    author='Peter Eastman',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=__version__,
    license='MIT',
    url='https://github.com/openmm/openmm-ml',
    platforms=['Linux', 'Mac OS-X', 'Unix', 'Windows'],
    classifiers=CLASSIFIERS.splitlines(),
    packages=find_packages(),
    zip_safe=False,
    install_requires=['numpy', 'openmm >= 7.5'],
    entry_points={
        'openmmml.potentials': [
            'ani1ccx = openmmml.models.anipotential:ANIPotentialImplFactory',
            'ani2x = openmmml.models.anipotential:ANIPotentialImplFactory',
            'mace = openmmml.models.macepotential:MACEPotentialImplFactory',
            'mace-off23-small = openmmml.models.macepotential:MACEPotentialImplFactory',
            'mace-off23-medium = openmmml.models.macepotential:MACEPotentialImplFactory',
            'mace-off23-large = openmmml.models.macepotential:MACEPotentialImplFactory',
            'nequip = openmmml.models.nequippotential:NequIPPotentialImplFactory',
            'deepmd = openmmml.models.deepmdpotential:DeepmdPotentialImplFactory',
        ]
    }
)

