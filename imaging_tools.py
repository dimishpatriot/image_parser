def welcome(program_data):
    print('=' * 78)
    print('Welcome to __{0}__, version {1}'.format(program_data.name, program_data.version))
    print('Author: {}'.format(program_data.author))
    print('Repository: {}'.format(program_data.rep))
    print('=' * 78)


def bye_bye():
    print('Bye Bye! See you later ^)')
    print('=' * 78)


def split_line():
    print('-' * 78)
