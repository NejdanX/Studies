def who_are_you_and_hello():
    while True:
        name = input()
        changed_name = ''.join(e for e in name if e.isalpha())
        changed_name = changed_name.capitalize()
        if name == changed_name:
            print(f"Привет, {name}!")
            break

