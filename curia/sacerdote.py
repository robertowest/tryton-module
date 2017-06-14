from trytond.model import ModelView, ModelSQL, fields, Unique
from trytond.pyson import Eval

class Sacerdote(ModelSQL, ModelView):
    "Sacerdote"
    __name__ = 'arzo.sacerdote'
