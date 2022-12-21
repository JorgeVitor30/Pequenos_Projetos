def execute_command(command: str):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for dic in directories:
                print('$ listing all directories from', dic)
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from')
        case ['cd' | 'change', path]:
            print('$ change directory to', path)
        case _:  # NAO PASSOU NADA DENTRO DAS CONDIÇÕES
            print('$ command not implemented')
        
    print('... rest of the code')
    


execute_command('ls /home')
print()
execute_command('ls /home /users /homrhoe ')




