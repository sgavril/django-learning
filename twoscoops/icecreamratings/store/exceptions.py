class OutOfStock(Exception):
    """ Raised when an item is out of stock. """
    pass

class CorruptedDatabase(Exceiption):
    """ Raised when there is database corruption. """
    pass