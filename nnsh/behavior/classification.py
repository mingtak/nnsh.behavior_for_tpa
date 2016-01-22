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
from plone import api

from nnsh.behavior import MessageFactory as _


organizers = SimpleVocabulary(
    [SimpleTerm(value=u'department_01', title=_(u'department_01')),
     SimpleTerm(value=u'department_02', title=_(u'department_02')),
     SimpleTerm(value=u'department_03', title=_(u'department_03')),
     SimpleTerm(value=u'department_04', title=_(u'department_04')),
     SimpleTerm(value=u'department_05', title=_(u'department_05')),
     SimpleTerm(value=u'department_06', title=_(u'department_06')),
     SimpleTerm(value=u'department_07', title=_(u'department_07')),
     SimpleTerm(value=u'department_08', title=_(u'department_08')),
     SimpleTerm(value=u'department_09', title=_(u'department_09')),
     SimpleTerm(value=u'department_10', title=_(u'department_10')),
     SimpleTerm(value=u'department_11', title=_(u'department_11')),
     SimpleTerm(value=u'department_12', title=_(u'department_12')),]
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
    """
    department = schema.Choice(
            title=_(u"Department"),
            vocabulary=organizers,
            required=True,
            default='department_01',
        )"""


    publisher = schema.Choice(
        title=_(u"Publish Unit"),
        description=_(u"Please select a publish unit."),
        vocabulary=u"plone.principalsource.Groups",
        default=u"admin09",
        required=True,
    )

    """
    classify = schema.Choice(
            title=_(u"Classfication"),
            vocabulary=classfication,
            required=True,
            default='news',
        ) """


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
#    department = context_property("department")
    publisher = context_property("publisher")
#    classify = context_property("classify")


"""
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
"""
@indexer(Interface)
def publisher_indexer(obj):
    if hasattr(obj, 'publisher'):
        return api.group.get(groupname=obj.publisher).getProperty('title')
grok.global_adapter(publisher_indexer, name='publisher')

