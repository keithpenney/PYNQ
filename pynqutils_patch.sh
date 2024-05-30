# Apply a damn patch to pynqutils

echo "INFO: patching pynqutils begin"
cd /usr/local/share/pynq-venv/lib/python3.10/site-packages/pynqutils
git apply /RFSoC-PYNQ/pynqutils.patch
echo "INFO: patching pynqutils done"
