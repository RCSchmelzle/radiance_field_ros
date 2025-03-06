from setuptools import setup, find_packages

setup(
    name="ros-nerf",
    version="0.1",
    packages=find_packages(),  # Automatically discovers all submodules
    package_dir={"": "."},  # Ensure correct discovery
    install_requires=[],
)


