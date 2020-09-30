from setuptools import find_packages, setup  # type: ignore


with open("README.md") as fd:
    long_description = fd.read()


install_requires = ["grpcio>=1.32.0"]

setup(
    name="aioetcd",
    version="0.1.0",
    author="Sergey Tsaplin",
    author_email="me@sergeytsaplin.com",
    description="etcd v3 client for AsyncIO",
    long_description=long_description,
    license="MIT",
    url="https://github.com/SergeyTsaplin/aioetcd",
    packages=find_packages(exclude=["test", "examples"]),
    install_requires=install_requires,
    package_data={"aioetcd": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha Copy",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
