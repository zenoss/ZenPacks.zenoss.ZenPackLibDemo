from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap


class ZPLDemoMap(PythonPlugin):
    """"Return dummy output for modeler demo"""

    def collect(self, device, log):
        """"""
        log.info('Collecting ZPLDemoMap for {}'.format(device.id))
        return [
            RelationshipMap(
                modname="ZenPacks.zenoss.ZenPackLibDemo.SubComponent",
                relname="subComponents",
                objmaps=[ObjectMap({'id': 'subComponent-1',
                                    'basic_string': 'Sub Text',
                                    'basic_int': 1,
                                    'basic_boolean': True,
                                    })]),
            RelationshipMap(
                modname="ZenPacks.zenoss.ZenPackLibDemo.AuxComponent",
                relname="auxComponents",
                objmaps=[ObjectMap({'id': 'auxComponent-1',
                                    'basic_string': 'Aux Text',
                                    'basic_int': 2,
                                    'basic_boolean': False,
                                    'editable_float': 0.9,
                                    'set_subComponents': ['subComponent-1']
                                    })]),
        ]

    def process(self, device, results, log):
        """"""
        log.info('processing ZPLDemoMap for {}: {}'.format(device.id, results))
        return results