from trytond.pool import Pool

def register():
    Pool.register(
        module='arzo', type_='model')
