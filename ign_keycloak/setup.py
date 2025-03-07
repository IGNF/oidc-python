import os
import sys

from setuptools import setup

sys.path.append(os.path.dirname(__file__))

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="ign_keycloak",
    version="0.1" + "." + BUILD_ID,
)
