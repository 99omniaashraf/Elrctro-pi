from setuptools import setup, find_packages

"""
The DataPrepKit capstone project is a comprehensive toolkit for preprocessing datasets,
focusing on efficient data reading, summary generation, handling missing values,
and categorical data encoding. The key features and requirements outlined provide
a clear roadmap for students to follow, ensuring a robust and versatile Python package.
Let's break down the key aspects:

Key Features:
1- Data Reading:
    Implement functions to read data from different file formats such as CSV, Excel, and JSON, using Pandas.

2- Data Summary:
    Develop functions that print key statistical summaries of the data, including the average and most
    frequent values, utilizing NumPy and Pandas.

3- Handling Missing Values:
    Create functions to handle missing values by either removing or imputing them based on predefined strategies.

4- Categorical Data Encoding:
    Implement encoding functions for categorical variables, enabling users to convert
    them into numerical representations.

5- Package Deployment:
    Publish the DataPrepKit package on PyPI to make it easily accessible to the broader Python community.

"""
setup(
    name='DataPrepKit',
    version='0.1',
    author="Omnia Ashraf(99omniaashraf)",
    author_email="<omniaashraf249@gmail.com>",
    url='https://github.com/99omniaashraf',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    keywords=[
        'Data Reading',
        'Data Summary',
        'Handling Missing Values',
        'Categorical Data Encoding',
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
