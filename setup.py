import versioneer
from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="dask-ssh",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Deploy dask clusters with ssh",
    long_description=long_description,
    packages=["dask_ssh"],
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        dask-ssh=dask_ssh.cli:main
      """,
    zip_safe=False,
)
