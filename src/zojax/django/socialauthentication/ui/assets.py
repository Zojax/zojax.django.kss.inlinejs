from django_assets import Bundle
from django.conf import settings
from staticfiles import settings as staticfiles_settings
import os.path


PREFIX = os.path.join(staticfiles_settings.ROOT[len(settings.MEDIA_ROOT):], "socialauthentication")


socialauthentication_js = Bundle(
    os.path.join(PREFIX, 'javascripts/jquery.openid.js'),
    output="gen/socialauthentication.js"
)

socialauthentication_css = Bundle(
    os.path.join(PREFIX, 'styles/style.css'),
    output="gen/socialauthentication.css"
)
