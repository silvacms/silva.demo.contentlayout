
from five import grok
from zope.traversing.browser import absoluteURL
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from silva.core import conf as silvaconf
from silva.core.contentlayout import Template, Slot
from silva.core.interfaces import IPublication
from silva.core.layout.interfaces import ICustomizableTag
from silva.core.layout.porto import porto
from silva.translations import translate as _
from silvatheme.standardissue.standardissue import IStandardIssue
from silva.fanstatic import need


grok.templatedir('templates')



class IAdvancedTemplate(ICustomizableTag):
    """Advanced layout template for Page
    """


class IAdvancedResources(IDefaultBrowserLayer):
    silvaconf.resource('advanced.css')



class AdvancedTemplate(Template):
    grok.order(5)
    grok.context(IAdvancedTemplate)

    label = _(u"Advanced template (StandardIssue)")
    description = _(u'A template that use larger portion from a layout')

    slots = {'one': Slot(),
             'two': Slot(),
             'navigation': Slot(),
             'footer': Slot(css_class="horizontal-blocks")}

    def update(self):
        self.root = self.content.get_publication()
        need(IAdvancedResources)

    def top_menu_items(self):
        for content in self.root:
            if not IPublication.providedBy(content):
                continue
            yield {'title': content.get_title_or_id(),
                   'css': content in self.request.PARENTS and 'active' or '',
                   'url': absoluteURL(content, self.request)}


class AdvancedLayout(porto.Layout):
    grok.context(IAdvancedTemplate)
    grok.layer(IStandardIssue)
    grok.name('layout')