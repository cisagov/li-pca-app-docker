#!/usr/bin/env pytest -vs
"""Tests for example container."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest

ENV_VAR = "ECHO_MESSAGE"
ENV_VAR_VAL = "Hello from li-pca-app-docker!"
READY_MESSAGE = "This is a debug message"
SECRET_QUOTE = (
    "There are no secrets better kept than the secrets everybody guesses."  # nosec
)
RELEASE_TAG = os.getenv("RELEASE_TAG")
VERSION_FILE = "src/version.txt"


def test_container_count(dockerc):
    """Verify the test composition and container."""
    # stopped parameter allows non-running containers in results
    assert (
        len(dockerc.containers(stopped=True)) == 3
    ), "Wrong number of containers were started."


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_release_version():
    """Verify that release tag version agrees with the module version."""
    pkg_vars = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), pkg_vars)  # nosec
    project_version = pkg_vars["__version__"]
    assert (
        RELEASE_TAG == f"v{project_version}"
    ), "RELEASE_TAG does not match the project version"
