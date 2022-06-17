def check_password(password):
    def decorator(func):
        def do_it(*args, **kwargs):
            if password == input('Input password: '):
                return func(*args, **kwargs)
            else:
                print('В доступе отказано')
                return None
        return do_it
    return decorator


@check_password('password')
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print('Булочка')
    if with_onion:
        print('Луковые колечки')
    if with_tomato:
        print('Ломтик помидора')
    print('Котлета из', type_of_meat)
    print('Булочка')


make_burger(6)