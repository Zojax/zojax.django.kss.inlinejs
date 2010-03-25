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


class ImageWidgetBase(ClearableFileInput):
    
    value = None
    needs_multipart_form = True
    
    def get_thumbnail_tag(self, value):
        raise NotImplementedError()
    
    def render(self, name, value, attrs=None):
        """ Shows image thumbnail instead of link only"""
        output = []
        if value and hasattr(value, "url"):
            try:
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' % \
                    (_('Currently:'), value.url, self.get_thumbnail_tag(value), _('Change:')))
            except (IOError, ThumbnailException):
                pass
        output.append(super(ImageWidgetBase, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

    def value_from_datadict(self, data, files, name):
        res = super(ImageWidgetBase, self).value_from_datadict(data, files, name)
        if isinstance(res[0], list):
            return res[0]
        return res
    

class AdminImageWidget(ImageWidgetBase):
    
    def get_thumbnail_tag(self, value):
        return value.extra_thumbnails_tag['admin']


class ImageWidget(ImageWidgetBase):
    
    def get_thumbnail_tag(self, value):
        return value.thumbnail_tag
