def test(required, optional='default'):
    print(str(required) + ' | ' + str(optional))


def run():
    test('req')


if __name__ == '__main__':
    run()
