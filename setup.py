from io import open
from setuptools import find_packages, setup

setup(
    name="signature similarity",
    version="0.1.0",
    author="Xi Xiong",
    author_email="xx2188@columbia.edu",
    description="Handwritten Signature Similarity Check",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    keywords='Handwritten signature similarity verification',
    license='MIT License',
    url="https://github.com/pixix/Signature-Similarity",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    install_requires=['opencv>=0.4.1',
                      'numpy',
                      'scipy'],

    # python_requires='>=3.5.0',
    tests_require=['pytest'],
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)