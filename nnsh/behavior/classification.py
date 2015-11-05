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

from nnsh.behavior import MessageFactory as _


organizers = SimpleVocabulary(
    [SimpleTerm(value=u'adma', title=_(u'adma')),
     SimpleTerm(value=u'admb', title=_(u'admb')),
     SimpleTerm(value=u'admc', title=_(u'admc')),
     SimpleTerm(value=u'admd', title=_(u'admd')),
     SimpleTerm(value=u'adme', title=_(u'adme')),
     SimpleTerm(value=u'admf', title=_(u'admf')),
     SimpleTerm(value=u'admg', title=_(u'admg'))]
    )

classfication = SimpleVocabulary(
    [SimpleTerm(value=u'news', title=_(u'News')),
     SimpleTerm(value=u'student', title=_(u'Student')),
     SimpleTerm(value=u'coworker', title=_(u'Coworker')),
     SimpleTerm(value=u'honor', title=_(u'Honor'))]
    )


class IClassification(model.Schema):
    """
       Marker/Form interface for Classification
    """
    department = schema.Choice(
            title=_(u"Department"),
            vocabulary=organizers,
            required=True,
            default='adma',
        )

    classify = schema.Choice(
            title=_(u"Classfication"),
            vocabulary=classfication,
            required=True,
            default='news',
        )


alsoProvides(IClassification, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class Classification(object):
    """
       Adapter for Classification
    """
    implements(IClassification)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    department = context_property("department")
    classify = context_property("classify")



@indexer(Interface)
def department_indexer(obj):
    if hasattr(obj, 'department'):
        return obj.department
grok.global_adapter(department_indexer, name='department')

@indexer(Interface)
def classify_indexer(obj):
    if hasattr(obj, 'classify'):
        return obj.classify
grok.global_adapter(classify_indexer, name='classify')

