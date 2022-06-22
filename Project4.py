from random import choice
jogadas = ['Ataque Aereo', 'Pedra', 'Papel']
sorteio = choice(jogadas)
jogador = ' '
while jogador not in 'Ataque Aereo' or 'Papel' or 'Pedra':
    jogador = str(input('Digite: ')).title()
    print('-=' * 25)
    print(f'Você escolheu {jogador} e eu {sorteio}')
    if jogador == 'Papel':
        if sorteio == 'Papel':
            print(
                'Ninguem ganhou, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder')
            print('-=' * 25)
            break
        if sorteio == 'Pedra':
            print(
                'Você perdeu!, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.')
            print('-=' * 25)
            break
        if sorteio == 'Ataque Aereo':
            print('Você Perdeu!, porque Ataque Aéreo sempre ganha e o Papel é patético')
            print('-=' * 25)
            break
    if jogador == 'Pedra':
        if sorteio == 'Papel':
            print(
                'Você ganhou!, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.')
            print('-=' * 25)
            break
        if sorteio == 'Pedra':
            print('Ninguem ganhou ,porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.')
            print('-=' * 25)
            break
        if sorteio == 'Ataque Aereo':
            print(
                'Você perdeu!, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.')
            print('-=' * 25)
            break
    if jogador == 'Ataque Aereo':
        if sorteio == 'Ataque Aereo':
            print(
                'Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua')
            print('-=' * 25)
            break
        if sorteio == 'Papel':
            print('Você ganhou!, porque Ataque Aéreo sempre ganha e o Papel é patético.')
            print('-=' * 25)
            break
        if sorteio == 'Pedra':
            print(
                'Você ganhou, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias')
            print('-=' * 25)
            break
