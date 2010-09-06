from kss.base import htmldata

def execJs(commands, selector, code, debug='0'):
        command = commands.addCommand('inlinejs-effect', selector)
        command.addParam('code', code)
        command.addParam('debug', debug)
