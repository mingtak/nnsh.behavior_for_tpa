from five import grok
from plone.indexer import indexer
from zope.interface import Interface
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.namedfile.field import NamedBlobImage

from nnsh.behavior import MessageFactory as _


class IBannerSlider(model.Schema):
    """
       Marker/Form interface for Classification
    """
    banner1 = NamedBlobImage(
        title=_(u"Banner image 1"),
        required=False,
    )

    banner2 = NamedBlobImage(
        title=_(u"Banner image 2"),
        required=False,
    )

    banner3 = NamedBlobImage(
        title=_(u"Banner image 3"),
        required=False,
    )

    banner4 = NamedBlobImage(
        title=_(u"Banner image 4"),
        required=False,
    )

    banner5 = NamedBlobImage(
        title=_(u"Banner image 5"),
        required=False,
    )


alsoProvides(IBannerSlider, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class BannerSlider(object):
    """
       Adapter for BannerSlider
    """
    implements(IBannerSlider)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    banner1 = context_property("banner1")
    banner2 = context_property("banner2")
    banner3 = context_property("banner3")
    banner4 = context_property("banner4")
    banner5 = context_property("banner5")
#    classify = context_property("classify")
