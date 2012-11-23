from zope.interface import implements

from plone.dexterity.content import Item
from plone.dexterity.content import Container

from plone.app.contenttypes.interfaces import (
    IDocument,
    IEvent,
    IFile,
    IFolder,
    IImage,
    ILink,
    INewsItem
)


class Document(Item):
    implements(IDocument)


class Event(Item):
    implements(IEvent)


class File(Item):
    implements(IFile)


class Folder(Container):
    implements(IFolder)


class Image(Container):
    implements(IImage)


class Link(Container):
    implements(ILink)


class NewsItem(Container):
    implements(INewsItem)
