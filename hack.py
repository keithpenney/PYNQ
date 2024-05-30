from distutils.command.build import build as dist_build

import subprocess

class _apply_pynqutils_patch(dist_build):
    """Custom distutils command to apply a dang patch."""

    description = "Apply a silly patch"

    def initialize_options(self):
        print("INFO: _apply_pynqutils_patch.initialize_options")
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("INFO: _apply_pynqutils_patch.run")
        subprocess.run(["sh", "pynqutils_patch.sh"])



