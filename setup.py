from setuptools import setup

package_name = "robotair_pub"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="pedro.m.melo",
    maintainer_email="pedro.m.melo@inesctec.pt",
    description="Minimal Demo Publisher for Robotair Galactic Example",
    license="Unlicense",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "robotair_pub_node = robotair_pub.robotair_pub_node:main"
        ],
    },
)
