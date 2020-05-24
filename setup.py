import setuptools


setuptools.setup(
    name="labtools", # Replace with your own username
    version="0.0.1",
    author="Wehr Lab",
    author_email="jlsaunders987@gmail.com",
    description="general use utility functions for the wehr lab",
    url="https://github.com/wehr-lab/labtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pandas',
        'numpy'

    ],
    python_requires='>=3.6',
)