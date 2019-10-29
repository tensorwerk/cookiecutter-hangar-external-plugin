import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()


setuptools.setup(
    name="{{cookiecutter.plugin_name}}",
    version="{{cookiecutter.version}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={'hangar.external.plugins': '{{cookiecutter.plugin_name}} = hangar_{{cookiecutter.plugin_name}}:Hangar{{cookiecutter.plugin_name}}'}
)
