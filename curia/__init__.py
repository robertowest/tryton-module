from trytond.pool import Pool
from .sacerdote import *

def register():
    Pool.register(
        Sacerdote,
        module='arzo', type_='model')
