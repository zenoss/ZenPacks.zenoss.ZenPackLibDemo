##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

"""Python datasource plugins.

This module contains Python datasource plugins that aren't directly
associated with a specific DataSource. Those are located in their
corresponding datasource module in the datasources/ directory.

"""

# Logging
import random
import logging
log = logging.getLogger('zen.ZPLDemoDataSource')

# Twisted Imports
from twisted.internet.defer import inlineCallbacks, returnValue
from Products.ZenUtils.Utils import prepId
from Products.ZenEvents import ZenEventClasses

# PythonCollector Imports
from ZenPacks.zenoss.PythonCollector.datasources.PythonDataSource \
    import PythonDataSourcePlugin


class ZPLDemoDataSourcePlugin(PythonDataSourcePlugin):
    '''
    ZPLDemoDataSourcePlugin
    '''

    def get_ts_value(self):
        return (random.randint(1, 100), 'N')

    @inlineCallbacks
    def collect(self, config):
        log.info("Collect for ZPLDemoDataSourcePlugin (%s)" % config.id)
        data = self.new_data()
         # retrieve datasource results from output
        for ds in config.datasources:
            comp_id = None
            if ds.component:
                comp_id = prepId(ds.component)

            for dp in ds.points:
                log.info('{} {}'.format(comp_id, dp.id))
                ts_value = yield self.get_ts_value()
                if comp_id:
                    data['values'][comp_id][dp.id] = ts_value
                else:
                    data['values'][dp.id] = ts_value

        returnValue(data)



class ZPLDemoStatusDataSourcePlugin(ZPLDemoDataSourcePlugin):
    '''
    ZPLDemoStatusDataSourcePlugin
    '''

    def get_ts_value(self):
        return (random.randint(0, 2), 'N')

