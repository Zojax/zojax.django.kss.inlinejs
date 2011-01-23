import os

import os

from kss.base.plugin import Plugin
from kss.base import core
from kss.base.selectors import css, htmlid, samenode, parentnode

import collective.kss.inlinejs
import inlinejs

kukit_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'javascript')

# Define the Javascripts by hand to ensure the order
js = ['inlinejs.js',
      'plugin.js',
     ]


class InlineJS(Plugin):
    '''The KSS core plugin has all the standard functionality'''

    priority = -1000

    javascripts = [os.path.join(kukit_dir, js) for js in js]

    commandsets = {
        'inlinejs': inlinejs,
        }

    selectors = {None: [css, htmlid, samenode, parentnode]}

