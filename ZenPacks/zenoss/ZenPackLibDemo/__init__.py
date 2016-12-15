from ZenPacks.zenoss.ZenPackLib import zenpacklib

CFG = zenpacklib.load_yaml(verbose=False, level=30)
schema = CFG.zenpack_module.schema
