import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="passtorage",
    version="0.0.1",
    requires = ['random', 'pyperclip'],
    author="Matías Pretz",
    url='https://github.com/matipretz/passtorage',
    platforms='Win10',
    license= 'MIT',
    entry_points={'console_scripts': ['passtorage-cli = src.__main__:main']},
    author_email="matipretz@gmail.com",
    description="CLI password generator and manager.",
    long_description="The main objective of passtorage is to generate random passwords and store them in text files without file extension. It futures recover, overwrite, delete and backup said passwords. Developed for Windows 10 and Python 3.7.2 (not tested in other versions). Currently uses the modules: random and pyperclip. Distributed under the MIT license. Any intentions to port this application to another platform are welcome. Contact: matipretz@gmail.com",
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=['src'],
    classifiers=[
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "Topic :: Utilities"]
    )
