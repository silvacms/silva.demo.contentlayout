
from five import grok
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from silva.core import conf as silvaconf
from silva.core.contentlayout import Design, Slot
from silva.fanstatic import need
from silva.translations import translate as _


grok.templatedir('templates')


class OneColumn(Design):
    silvaconf.icon("one_column.png")
    grok.order(10)
    grok.name('demo.one_column')
    grok.title(_(u"One Column (standard)"))

    description = _(u"A simple one column layout")
    slots = {'main': Slot()}


class ITwoColumnsResources(IDefaultBrowserLayer):
    silvaconf.resource('two_columns.css')


class TwoColumns(Design):
    silvaconf.icon("two_columns.png")
    grok.order(20)
    grok.name('demo.two_column')
    grok.title(_(u"Two Columns (standard)"))

    description = _(u"A simple two columns layout")
    slots = {'one': Slot(),
             'two': Slot()}


    def update(self):
        need(ITwoColumnsResources)
