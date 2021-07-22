from setuptools import setup

with open("Readme.md", 'r') as f:
    long_description = f.read()

setup(
    name='tkTimePicker',
    version='0.0.0',
    description="This library helps you to write set style to tkinter default widget using stylesheet without much "
                "work.",
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
    py_modules=["tkstylesheet.py"],
    include_package_data=True,
    python_requires='>=3.6',
)
