from django import forms

from form_utils.fields import ClearableImageField
from widgets import AdminImageWidget, ImageWidget


class ImageWithThumbnailsField(ClearableImageField):
    widget = ImageWidget


class ImageWithThumbnailsAdminField(ClearableImageField):
    widget = AdminImageWidget