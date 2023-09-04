import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def spheres():
    return open("test-data/spheres.i").read()


def test_line_endings(tmp_path, spheres):
    input = tmp_path / 'input.i'

    # test with unix line endings
    input.write_text(spheres, newline="\n")
    subprocess.check_call(
        "csg2csg -i input.i -f mcnp -o all",
        shell=True,
        cwd=tmp_path,
    )

    # test with windows line endings
    input.write_text(spheres, newline="\r\n")
    subprocess.check_call(
        "csg2csg -i input.i -f mcnp -o all",
        shell=True,
        cwd=tmp_path,
    )


# round trip the MCNP file produced from the line above - it should be
# identical
def test_round_trip(tmp_path, spheres):
    dira = tmp_path / 'a'
    dira.mkdir()
    (dira / 'input.i').write_text(spheres)
    subprocess.check_call(
        "csg2csg -i input.i -f mcnp -o mcnp",
        shell=True,
        cwd=dira,
    )

    # save the first MCNP output
    first = (dira / 'mcnp/file.mcnp').read_text()

    dirb = tmp_path / 'b'
    dirb.mkdir()
    (dirb / 'input.mcnp').write_text(first)
    subprocess.check_call(
        "csg2csg -i input.mcnp -f mcnp -o mcnp",
        shell=True,
        cwd=dirb,
    )

    second = (dirb / 'mcnp/file.mcnp').read_text()
    assert first == second
