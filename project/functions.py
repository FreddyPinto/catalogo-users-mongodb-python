import os


def clear_system(function):

    def wrap(*args, **kwargs):
        os.system('cls')
        result = function(*args, **kwargs)
        input('')
        os.system('cls')

    wrap.__doc__ = function.__doc__
    return wrap


@clear_system
def create_user(collection):
    '''A) Crear un usuario'''

    username = input('Username: ')
    edad = int(input('Edad: '))
    email = input('Email: ')

    user = dict(username=username, edad=edad, email=email)

    collection.insert_one(user)

    print(user)

    return user


@clear_system
def get_user(collection):
    '''B) Consultar un usuario'''
    username = input('Username: ')
    user = collection.find_one(
        {'username': username},
        {'_id': False}
    )

    print(user)

    return user


def delete_user():
    '''C) Eliminar un usuario'''
    print('Eliminar usuario')


def update_user():
    '''D) Actualizar un usuario'''
    print('Actualizar usuario')


def default(*args, **kwargs):
    print('Opción no valida')
