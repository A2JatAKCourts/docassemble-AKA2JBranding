# pre-load
import os
try:
    from docassemble.ALWeaver.custom_values import advertise_capabilities
    if not os.environ.get('ISUNITTEST'):
        advertise_capabilities(__name__, minimum_version="1.5")

except ImportError:
    from docassemble.base.util import log
    log("Not advertising capabilities because ALWeaver is not installed.")