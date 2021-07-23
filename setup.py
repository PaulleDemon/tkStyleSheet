from setuptools import setup

with open("Readme.md", 'r') as f:
    long_description = f.read()

setup(
    name='tkstylesheet',
    version='0.0.1',
    description="This library helps you to set style to tkinter default widget using stylesheet with ease.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Paul',
    url="https://github.com/PaulleDemon/tkStyleSheet",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords=['tkinter', 'stylesheet', 'tkss', 'tkinter stylesheet'],
    packages=["tkstylesheet"],
    include_package_data=True,
    python_requires='>=3.6',
)
