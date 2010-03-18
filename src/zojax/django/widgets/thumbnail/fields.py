from django import forms

from form_utils.fields import ClearableImageField
from widgets import ImageWidget


class ImageWithThumbnailsField(ClearableImageField):
    widget = ImageWidget