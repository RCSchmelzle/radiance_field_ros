from setuptools import setup, find_packages
setup(
    name="ros_nerf",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ns-ros=ros_nerf.ros_nerf.scripts.ros_runner:entrypoint",
            "ns-ros-save=ros_nerf.ros_nerf.scripts.ros_saver:entrypoint",
        ],
    },
)
