import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NumA",
    version="0.1",
    author="Maurice Künicke",
    author_email="m.kuenicke@campus.tu-berlin.de",
    description="Numerical Analysis Package containing various helpful methods.",
    packages=["numa", "numa/RootFinder", "numa/utils"],
    long_description=long_description,
    url="https://github.com/MauriceKuenicke/NumA",
    license="MIT",
    python_requires='>=3',
    install_requires=["numpy"]

)
