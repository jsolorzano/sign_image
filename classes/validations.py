class Validations:

    def __init__(self):
        pass

    def validateName(self, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError(f'The name must have a minimum of 3 characters and a maximum of 50 characters, current size: {len(name)}')
        return True
