import PasswordGenerator

if __name__ == '__main__':
    word_or_phrase = input('Generate password or passphrase? ')
    if word_or_phrase == 'password':
        args = input(' strong/weak | length (max 250) (0 for random)| Includes capital letters (True/False, default true): ')
        args = args.lower()
        args = args.split()
        generate = PasswordGenerator.password(args[0], args[1], args[2])
        print(generate.get_pass())
    elif word_or_phrase == 'passphrase':
        args = input(' word amount (max 50) (0 for random) | Capitalize first letter? (True/False, default false): ')
        args = args.lower()
        args = args.split()
        generate = PasswordGenerator.passphrase(args[0], args[1])
        print(generate.get_phrase())
    else:
        print(f'Invalid choice {word_or_phrase}')