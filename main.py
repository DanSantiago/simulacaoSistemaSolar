# Simulação do Sistema Solar
# Autor: Daniel Santiago da Silva (Estudante ICEX - UFF)

# Importando os módulos a serem usados
from membros.classes import classe
from membros.funcoes import func
from turtle import *
import pygame

# Importando as imagens para a forma dos astros, botões e informações
imagens = ['coisas/sol.gif', 'coisas/mercurio.gif', 'coisas/venus.gif',
           'coisas/terra.gif', 'coisas/marte.gif',
           'coisas/jupiter.gif', 'coisas/saturno.gif',
           'coisas/urano.gif', 'coisas/netuno.gif', 'coisas/plutao.gif',
           'coisas/start.gif', 'coisas/sair.gif', 'coisas/foguete.gif',
           'coisas/infomercurio.gif', 'coisas/infovenus.gif',
           'coisas/infoterra.gif', 'coisas/infomarte.gif',
           'coisas/infojupiter.gif', 'coisas/infosaturno.gif',
           'coisas/infourano.gif', 'coisas/infonetuno.gif',
           'coisas/infoplutao.gif', 'coisas/infosol.gif', 'coisas/instru.gif']

# Registrando as imagens na forma dos planetas
for i in imagens:
    register_shape(i)


def main():
    # iniciando a primeira música (tela inicial)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('coisas/menu.mp3')
    pygame.mixer_music.play()

    # configurando a tela inicial
    tela = Screen()
    tela.bgpic('coisas/telainicial.gif')
    tela.setup(1920, 1080, 0, 0)
    tela.title('Simulação do Sistema Solar')

    # configurando o foguete (botão)
    func.foguete.up()
    func.foguete.setpos(-160, -50)
    func.foguete.down()
    func.foguete.shape('coisas/foguete.gif')
    func.foguete.showturtle()

    # looping da tela inicial
    while True:
        # testa se alguma opção foi escolhida
        if func.start:
            break
        if func.sair:
            break

        # configurando o botão sair na tela inicial
        func.sair_button.up()
        func.sair_button.setpos(-20, -150)
        func.sair_button.down()
        func.sair_button.shape('coisas/sair.gif')
        func.sair_button.showturtle()

        # configurando o botão iniciar na tela inicial
        func.iniciar.up()
        func.iniciar.setpos(-20, -50)
        func.iniciar.down()
        func.iniciar.shape('coisas/start.gif')
        func.iniciar.showturtle()

        # checa se as teclas especiais foram apertadas e
        # chama as funções caso tenham sido
        tela.listen()
        tela.onkeypress(func.down, 'Down')
        tela.onkeypress(func.up, 'Up')
        tela.onkeypress(func.comecar, 'Return')

        # configurando a posição da tela de informações
        # sobre as teclas especiais da simulação
        func.info.up()
        func.info.setpos(-835, 308)
        func.info.down()
        func.info.hideturtle()

        # configurando a posição da tela com informações
        # sobre os astros da simulação
        func.instru.up()
        func.instru.setpos(-835, -308)
        func.instru.down()
        func.instru.hideturtle()

    # inicia a simulação caso a opção iniciar tenha sido escolhida
    tela.clear()
    if func.start:

        # configurando a tela de informações sobre as teclas especiais
        func.instru.shape('coisas/instru.gif')
        func.instru.showturtle()

        # para a primeira música e inicia a segunda
        pygame.mixer_music.stop()
        pygame.mixer.music.load('coisas/ambiente.mp3')
        pygame.mixer_music.play()

        # troca o plano de fundo
        tela.bgpic('coisas/universe.gif')  # plano de fundo

        # criando os objetos e definindo seus valores
        sol = classe.Estrela('Sol', 'coisas/sol.gif')
        mercurio = classe.Planeta('Mercúrio', 1, 'coisas/mercurio.gif', 'gray')
        venus = classe.Planeta('Vênus', 2, 'coisas/venus.gif', 'darkorange')
        terra = classe.Planeta('Terra', 3, 'coisas/terra.gif', 'blue')
        marte = classe.Planeta('Marte', 4, 'coisas/marte.gif', 'red')
        jupiter = classe.Planeta('Júpiter', 5, 'coisas/jupiter.gif', 'sandybrown')
        saturno = classe.Planeta('Saturno', 6, 'coisas/saturno.gif', 'goldenrod')
        urano = classe.Planeta('Urano', 7, 'coisas/urano.gif', 'mediumseagreen')
        netuno = classe.Planeta('Netuno', 8, 'coisas/netuno.gif', 'steelblue')
        plutao = classe.PlanetaAnao('Plutão', 9, 'coisas/plutao.gif', 'peachpuff')

        # looping da simulação
        while True:
            # controla o update time da tela
            tela.tracer(func.frames)

            # checa se alguma tecla especial foi pressionada,
            # ou se houve click do mouse
            tela.listen()
            tela.onkeypress(func.acelerar, 'Up')
            tela.onkeypress(func.desacelerar, 'Down')
            tela.onkeypress(func.resetar, 'R')
            tela.onkeypress(func.resetar, 'r')
            tela.onkeypress(func.pausar, 'P')
            tela.onkeypress(func.pausar, 'p')
            tela.onkeypress(func.fechar, 'Escape')
            tela.onclick(func.info_planets)

            # realiza o movimento de translação dos astros
            mercurio.translacao(func.timer)
            venus.translacao(func.timer * 0.8)
            terra.translacao(func.timer * 0.6)
            marte.translacao(func.timer * 0.4)
            jupiter.translacao(func.timer * 0.2)
            saturno.translacao(func.timer * 0.1)
            urano.translacao(func.timer * 0.05)
            netuno.translacao(func.timer * 0.1)
            plutao.translacao(func.timer * 0.1)

            # checa se a simulação foi pausada
            if not func.pausa:
                func.timer += 1

            # checa se a simulação deve ser fechada
            if func.terminar:
                break

            # reseta o tempo quando os astros estão alinhados
            if func.timer == 7200:
                func.timer = 0

    # limpa a tela, fecha e para a música
    tela.clear()
    pygame.mixer_music.stop()


if __name__ == '__main__':
    main()
