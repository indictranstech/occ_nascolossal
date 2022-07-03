from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in occ/__init__.py
from occ import __version__ as version

setup(
	name="occ",
	version=version,
	description="Operations Control Center",
	author="UnifiedSupportServices",
	author_email="info@unifiedsupport.co.za",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
