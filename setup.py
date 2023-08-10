import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

requires = [
    "requests>=2.28.1",
    "pydantic>=2.1.1",
]

setuptools.setup(
    name="ipeakoin_sdk",
    version="0.0.1",
    keywords=["Global Account", "Crypto Asset", "Quantum Card"],
    author="iPeakoin team",
    author_email="",
    description="bass api",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(exclude=('tests', '.pypirc')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requires,
)