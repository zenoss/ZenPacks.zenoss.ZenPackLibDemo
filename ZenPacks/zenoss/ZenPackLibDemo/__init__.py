from ZenPacks.zenoss.ZenPackLib import zenpacklib

CFG = zenpacklib.load_yaml(verbose=True, level=10)
schema = CFG.zenpack_module.schema
