import argparse

class CLIApp:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Mini CLI Framework')

    def add_command(self, name, func, help=None):
        self.parser.add_argument('-c', '--command', choices=[name], help=help)
        self.parser.set_defaults(command=name)
        self.commands[name] = func

    def run(self):
        args = self.parser.parse_args()
        if hasattr(args, 'command'):
            self.commands[args.command]()
        else:
            self.parser.print_help()

class Command:
    def __init__(self, app):
        self.app = app

    def run(self):
        pass

class HelloCommand(Command):
    def run(self):
        print('Hello, World!')

class AddCommand(Command):
    def run(self):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(f'Result: {num1 + num2}')

def main():
    app = CLIApp()
    app.add_command('hello', HelloCommand(app).run, 'Prints Hello, World!')
    app.add_command('add', AddCommand(app).run, 'Adds two numbers')
    app.run()

if __name__ == '__main__':
    main()
```

Kodni ishga tushirish uchun quyidagicha qilishingiz mumkin:

```bash
python cli_app.py -h
```

Bu sizga CLI dasturining yordam maqolasini ko'rsatadi. Keyin quyidagicha qilishingiz mumkin:

```bash
python cli_app.py -c hello
```

Bu sizga "Hello, World!" matnini ko'rsatadi. Keyin quyidagicha qilishingiz mumkin:

```bash
python cli_app.py -c add
```

Bu sizga ikki sonni kiritish uchun so'rov beradi va natijani ko'rsatadi.
