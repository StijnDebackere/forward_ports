import setuptools

setuptools.setup(
    name="forward_ports",
    version="0.0.1",
    author="Stijn Debackere",
    author_email="debackere@strw.leidenuniv.nl",
    description="Python tool to setup remote port forwards.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/StijnDebackere/forward_ports",
    scripts=["forward_ports.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
