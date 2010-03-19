"""
widgets for django-form-utils

Time-stamp: <2010-03-05 15:03:36 carljm widgets.py>

parts of this code taken from http://www.djangosnippets.org/snippets/934/
 - thanks baumer1122

"""
from form_utils.widgets import ClearableFileInput
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from sorl.thumbnail.fields import ImageWithThumbnailsField, ImageWithThumbnailsFieldFile
from sorl.thumbnail.base import ThumbnailException

class AdminImageWidget(ClearableFileInput):
    
    def render(self, name, value, attrs=None):
        """ Shows image thumbnail instead of link only"""
        output = []
        if value and hasattr(value, "url"):
            try:
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' % \
                    (_('Currently:'), value.url, value.extra_thumbnails_tag['admin'], _('Change:')))
            except (IOError, ThumbnailException):
                pass
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
    

class ImageWidget(ClearableFileInput):
    
    def render(self, name, value, attrs=None):
        """ Shows image thumbnail instead of link only"""
        output = []
        if value and hasattr(value, "url"):
            try:
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' % \
                              (_('Currently:'), value.url, value.thumbnail_tag, _('Change:')))
            except  (IOError, ThumbnailException):
                pass
        output.append(super(ImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))