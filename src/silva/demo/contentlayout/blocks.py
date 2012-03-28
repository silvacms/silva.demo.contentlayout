
from five import grok

from silva.core.contentlayout.blocks import Block
from silva.core.contentlayout.interfaces import IBlock

from silva.app.page.interfaces import IPage
from silva.translations import translate as _


class CustomBlock(Block):
    grok.context(IPage)
    grok.name('news_info')
    grok.title(_('News info'))
    grok.implements(IBlock)
