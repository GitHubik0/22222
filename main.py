import warnings

class pomilka(Exception):
    def __str__(self):
        return f'So much code'

def check_text():

    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.simplefilter('always', ImportWarning)

    warnings.warn('Warning, no code here', SyntaxWarning)
    try:
        warnings.warn('Warning, module not import', ImportWarning)
    except:
        print('Warning processed')
check_text()