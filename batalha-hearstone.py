
print("-----------------------------------------_")
print("|x| Seja Bem vindo a Arena HearthStone |x|")
print("__________________________________________")

#HÉROI 1
print("Está preparado para batalhar? \nInsira os dados da sua batalha!")

heroi_1 = str(input("Você poderá escolher entre Guldan e Anduim como heróis! \n Quem será o seu héroi?:"))
vida_h1 = int(input(f"OBS:A vida do héroi {heroi_1} pode variar entre 1 e 30! \nInsira a vida do héroi {heroi_1}:"))
while (vida_h1 < 1 or vida_h1 > 30):
    print(f"Você inseriu a vida do héroi {heroi_1} incorretamente, insira a vida correta do héroi {heroi_1}!")
    vida_h1 = int(input(f"Insira a vida do héroi {heroi_1}:"))

#LACAIO  1
lacaio_1 = str(input(f"Você poderá escolher entre Morloc, Anão, Vampiro e Duende para lacaios do seu héroi {heroi_1}! \nQuem será o primeiro lacaio do héroi {heroi_1}?:"))
vida_L1 = int(input(f"OBS: A vida do lacaio {lacaio_1} de {heroi_1} pode variar entre 1 e 10! \nInsira a vida do lacaio {lacaio_1} de {heroi_1}:"))
while (vida_L1 < 1 or vida_L1 > 10):
    print(f"Você inseriu a vida do lacaio {lacaio_1} de {heroi_1} incorretamente, insira a vida do lacaio {lacaio_1} de {heroi_1} corretamente!")
    vida_L1 = int(input(f"Insira a vida do lacaio {lacaio_1} de {heroi_1}:"))
dano_L1 = int(input(f"OBS: Os pontos de dano do lacaio {lacaio_1} de {heroi_1} podem variar entre 1 e 10! \nInsira os pontos de dano do {lacaio_1} de {heroi_1}:"))
while (dano_L1 < 1 or dano_L1 > 10):
    print(f"Você inseriu os pontos de dano do lacaio {lacaio_1} de {heroi_1} incorretamente, insira a vida do {lacaio_1} de {heroi_1} corretamente!")
    dano_L1 = int(input(f"Insira os pontos de dano do {lacaio_1} de {heroi_1}:"))

#CONDIÇÕES E LACAIO 2

if (lacaio_1 == 'Morloc'):
    lacaio_2 = str(input(f"Você poderá escolher entre Anão, Vampiro e Duende para segundo lacaio do héroi {heroi_1}! \nQuem será o segundo lacaio de {heroi_1}?: "))
elif(lacaio_1 == 'Anão'):
    lacaio_2 = str(input(f"Você poderá escolher entre Morloc, Vampiro e Duende para segundo lacaio do héroi {heroi_1}! \nQuem será o segundo lacaio de {heroi_1}?: "))
elif(lacaio_1 == 'Vampiro'):
    lacaio_2 = str(input(f"Você poderá escolher entre Morloc, Anão e Duende para segundo lacaio do héroi {heroi_1}! \nQuem será o segundo lacaio de {heroi_1}?: "))
elif(lacaio_1 == 'Duende'):
    lacaio_2 = str(input(f"Você poderá escolher entre Morloc, Anão e Vampiro para segundo lacaio do héroi {heroi_1}! \nQuem será o segundo lacaio de {heroi_1}?: "))
while lacaio_2 == lacaio_1:
    print(f"Você inseriu um lacaio repetido, escolha o segundo lacaio de {heroi_1} corretamente!")
    lacaio_2 = str(input(f"Quem será o segundo lacaio de {heroi_1}?:"))
vida_L2 = int(input(f"OBS: A vida do lacaio {lacaio_2} de {heroi_1} pode variar entre 1 e 10! \nInsira a vida do lacaio {lacaio_2} de {heroi_1}:"))
while (vida_L2 < 1 or vida_L2 > 10):
    print(f"Você inseriu a vida do lacaio {lacaio_2} de {heroi_1} incorretamente, insira a vida do lacaio {lacaio_2} de {heroi_1} corretamente!")
    vida_L2 = int(input(f"Insira a vida do lacaio {lacaio_2} de {heroi_1}:"))
dano_L2 = int(input(f"OBS: Os pontos de dano do lacaio {lacaio_2} de {heroi_1} podem variar entre 1 e 10! \nInsira os pontos de dano do {lacaio_2} de {heroi_1}:"))
while (dano_L2 < 1 or dano_L2 > 10):
    print(f"Você inseriu os pontos de dano do lacaio {lacaio_2} de {heroi_1} incorretamente, insira a vida do {lacaio_2} de {heroi_1} corretamente!")
    dano_L2 = int(input(f"Insira os pontos de dano do {lacaio_2} de {heroi_1}:"))

#HÉROI 2

if (heroi_1 == 'Guldan'):
    heroi_2 = 'Anduim'
elif(heroi_1 == 'Anduim'):
    heroi_2 = 'Guldan'
vida_h2 = int(input(f"OBS:A vida do héroi {heroi_2} pode variar entre 1 e 30!\nJá que o seu héroi foi o {heroi_1}, insira a vida do héroi inimigo, o héroi {heroi_2}, que batalhará com {heroi_1}:"))
while (vida_h2 < 1 or vida_h2 > 30):
    print(f"Você inseriu a vida do héroi {heroi_2} incorretamente, insira a vida correta do héroi {heroi_2}!")
    vida_h2 = int(input(f"Insira a vida do héroi {heroi_2}:"))

#CONDIÇÕES LACAIO 3

#MORLOC
if lacaio_1 == 'Morloc' and lacaio_2 == 'Anão':
    print(f"Você poderá escolher entre Vampiro e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Morloc' and lacaio_2 == 'Vampiro':
    print(f"Você poderá escolher entre Anão e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Morloc' and lacaio_2 == 'Duende':
    print(f"Você poderá escolher entre Anão e Vampiro para primeiro lacaio do héroi {heroi_2}!")

#ANÃO
if lacaio_1 == 'Anão' and lacaio_2 == 'Morloc':
    print(f"Você poderá escolher entre Vampiro e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Anão' and lacaio_2 == 'Vampiro':
    print(f"Você poderá escolher entre Morloc e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Anão' and lacaio_2 == 'Duende':
    print(f"Você poderá escolher entre Morloc e Vampiro para primeiro lacaio do héroi {heroi_2}!")

#VAMPIRO
if lacaio_1 == 'Vampiro' and lacaio_2 == 'Morloc':
    print(f"Você poderá escolher entre Anão e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Vampiro' and lacaio_2 == 'Anão':
    print(f"Você poderá escolher entre Morloc e Duende para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Vampiro' and lacaio_2 == 'Duende':
    print(f"Você poderá escolher entre Morloc e Anão para primeiro lacaio do héroi {heroi_2}!")

#DUENDE
if lacaio_1 == 'Duende' and lacaio_2 == 'Morloc':
    print(f"Você poderá escolher entre Anão e Vampiro para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Duende' and lacaio_2 == 'Anão':
    print(f"Você poderá escolher entre Morloc e Vampiro para primeiro lacaio do héroi {heroi_2}!")
elif lacaio_1 == 'Duende' and lacaio_2 == 'Vampiro':
    print(f"Você poderá escolher entre Morloc e Anão para primeiro lacaio do héroi {heroi_2}!")
lacaio_3 = str(input(f"Muito bem, vamos escolher os lacaios do héroi {heroi_2}! \nQuem será o primeiro lacaio de {heroi_2}?:"))
while (lacaio_3 == lacaio_1 or lacaio_3 == lacaio_2):
    print(f"Você inseriu um lacaio repetido, escolha o primeiro lacaio do {heroi_2} corretamente!")
    lacaio_3 = str(input(f"Quem será o primeiro lacaio de {heroi_2}?:"))
vida_L3 = int(input(f"OBS: A vida do lacaio {lacaio_3} de {heroi_2} pode variar entre 1 e 10! \nInsira a vida do lacaio {lacaio_3} de {heroi_2}:"))
while (vida_L3 < 1 or vida_L3 > 10):
    print(f"Você inseriu a vida do lacaio {lacaio_3} de {heroi_2} incorretamente, insira a vida do lacaio {lacaio_3} de {heroi_2} corretamente!")
    vida_L3 = int(input(f"Insira a vida do lacaio {lacaio_3} de {heroi_2}:"))
dano_L3 = int(input(f"OBS: Os pontos de dano do lacaio {lacaio_3} de {heroi_2} podem variar entre 1 e 10! \nInsira os pontos de dano do {lacaio_3} de {heroi_2}:"))
while (dano_L3 < 1 or dano_L3 > 10):
    print(f"Você inseriu os pontos de dano do lacaio {lacaio_3} de {heroi_2} incorretamente, insira a vida do {lacaio_3} de {heroi_2} corretamente!")
    dano_L3 = int(input(f"Insira os pontos de dano do {lacaio_3} de {heroi_2}:"))

#CONDIÇÕES LACAIO 4

# MORLOC
if (lacaio_1 == 'Morloc' and lacaio_2 == 'Anão' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Morloc' and lacaio_2 == 'Anão' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Morloc' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Morloc' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Anão'
elif (lacaio_1 == 'Morloc' and lacaio_2 == 'Duende' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Morloc' and lacaio_2 == 'Duende' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Anão'

# ANÃO
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Morloc' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Morloc' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Morloc'
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Duende' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Anão' and lacaio_2 == 'Duende' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Morloc'

# VAMPIRO
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Morloc' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Morloc' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Anão'
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Anão' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Duende'
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Anão' and lacaio_3 == 'Duende'):
    lacaio_4 = 'Morloc'
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Duende' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Anão'
elif (lacaio_1 == 'Vampiro' and lacaio_2 == 'Duende' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Morloc'

# DUENDE
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Morloc' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Morloc' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Anão'
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Anão' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Vampiro'
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Anão' and lacaio_3 == 'Vampiro'):
    lacaio_4 = 'Morloc'
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Morloc'):
    lacaio_4 = 'Anão'
elif (lacaio_1 == 'Duende' and lacaio_2 == 'Vampiro' and lacaio_3 == 'Anão'):
    lacaio_4 = 'Morloc'

#LACAIO 4

print(f"O último lacaio que sobrou é o lacaio {lacaio_4}, ele será o segundo lacaio do héroi {heroi_2}!")
vida_L4 = int(input(f"OBS: A vida do lacaio {lacaio_4} de {heroi_2} pode variar entre 1 e 10! \nInsira a vida do lacaio {lacaio_4} de {heroi_2}:"))
while (vida_L4 < 1 or vida_L4 > 10):
    print(f"Você inseriu a vida do lacaio {lacaio_4} de {heroi_2} incorretamente, insira a vida do lacaio {lacaio_4} de {heroi_2} corretamente!")
    vida_L4 = int(input(f"Insira a vida do lacaio {lacaio_4} de {heroi_2}:"))
dano_L4 = int(input(f"OBS: Os pontos de dano do lacaio {lacaio_4} de {heroi_2} podem variar entre 1 e 10! \nInsira os pontos de dano do {lacaio_4} de {heroi_2}:"))
while (dano_L4 < 1 or dano_L3 > 10):
    print(f"Você inseriu os pontos de dano do lacaio {lacaio_4} de {heroi_2} incorretamente, insira os pontos de dano do {lacaio_4} de {heroi_2} corretamente!")
    dano_L4 = int(input(f"Insira os pontos de dano do {lacaio_4} de {heroi_2}:"))

#ATAQUE

print("____________________________________________________________________________________")
print("                                                                                    ")
print("                          Xx SUA BATALHA VAI COMEÇAR xX                             ")
print("____________________________________________________________________________________")
print("                                                                                    ")
print(f" {heroi_1}                          x                                {heroi_2}     ")
print("                                                                                    ")
print(f" {lacaio_1}                                                         {lacaio_3}     ")
print("                                                                                    ")
print(f" {lacaio_2}                                                         {lacaio_4}     ")
print("                                                                                    ")
print("____________________________________________________________________________________")

#ESCOLHAS DE ATAQUE

escolha_1 = str(input(f"Qual lacaio realizará o primeiro ataque, o lacaio {lacaio_1} ou lacaio {lacaio_2}?:"))
while escolha_1 == lacaio_3 or escolha_1 == lacaio_4 or escolha_1 == heroi_2 or escolha_1 == heroi_1:
    print(f"Você escolheu um personagem incorreto ou um dos lacaios ou héroi inimigos, insira um de seus lacaios!")
    escolha_1 = str(input(f"Qual lacaio realizará o primeiro ataque, o lacaio {lacaio_1} ou lacaio {lacaio_2}?:"))

print(f"Lembrando que o {escolha_1} poderá atacar o héroi {heroi_2}, o lacaio {lacaio_3} ou lacaio {lacaio_4}!")
escolha_2 = str(input(f"Quem o {escolha_1} atacará?:"))
while escolha_2 == lacaio_1 or escolha_2 == lacaio_2 or escolha_2 == heroi_1:
    print(f"Você escolheu um dos seus personagens para ser atacado, insira um adversário!")
    escolha_2 = str(input(f"Quem o {escolha_1} atacará?:"))

#DADOS DA PRIMEIRA ESCOLHA

if escolha_1 == lacaio_1:
    vida_E1 = vida_L1
    dano_E1 = dano_L1
    escolha_NE1 = lacaio_2
    vida_NE1 = vida_L2
    dano_NE1 = dano_L2
elif escolha_1 == lacaio_2:
    vida_E1 = vida_L2
    dano_E1 = dano_L2
    escolha_NE1 = lacaio_1
    vida_NE1 = vida_L1
    dano_NE1 = dano_L1

#DADOS DA SEGUNDA ESCOLHA

if escolha_2 == lacaio_3:
    vida_E2 = vida_L3
    dano_E2 = dano_L3
    escolha_NE2 = lacaio_4
    vida_NE2 = vida_L4
    dano_NE2 = dano_L4
elif escolha_2 == lacaio_4:
    vida_E2 = vida_L4
    dano_E2 = dano_L4
    escolha_NE2 = lacaio_3
    vida_NE2 = vida_L3
    dano_NE2 = dano_L3
elif escolha_2 == heroi_2:
    vida_E2 = vida_h2
    dano_E2 = 0
    escolha_NE2 = lacaio_3
    vida_NE2 = vida_L3
    dano_NE2 = dano_L3
    escolha_NE3 = lacaio_4
    vida_NE3 = vida_L4
    dano_NE3 = dano_L4

#CÁLCULO DO ATAQUE

vida_ataquePAE2 = (vida_E2 - dano_E1)
vida_ataquePAE1 = (vida_E1 - dano_E2)

print("____________________________________________________")
print("                  ATAQUE REALIZADO                  ")
print("____________________________________________________")

if vida_ataquePAE2 <= 0 and vida_ataquePAE1 <= 0:
    vida_E2 = vida_ataquePAE2
    vida_E1 = vida_ataquePAE1
    print(f"O {escolha_1} matou o {escolha_2}, mas acabou morrendo junto!")
elif vida_ataquePAE2 <= 0 and vida_ataquePAE1 > 0:
    vida_E2 = vida_ataquePAE2
    vida_E1 = vida_ataquePAE1
    print(f"O {escolha_1} matou o {escolha_2}, e o {escolha_2} deixou o {escolha_1} com {vida_ataquePAE1} de vida!")
elif vida_ataquePAE2 > 0 and vida_ataquePAE1 <= 0:
    vida_E2 = vida_ataquePAE2
    vida_E1 = vida_ataquePAE1
    print(f"O {escolha_1} não conseguiu matar o {escolha_2} e acabou morrendo, o {escolha_2} ficou com {vida_ataquePAE2} de vida!")
elif vida_ataquePAE2 > 0 and vida_ataquePAE1 > 0:
    vida_E2 = vida_ataquePAE2
    vida_E1 = vida_ataquePAE1
    print(f"Ambos sobreviveram, o {escolha_1} ficou com {vida_ataquePAE1} de vida e o {escolha_2} com {vida_ataquePAE2} de vida!")

#SATUS FINAL HÉROI 1

print("____________________________________________________")
print("                STATUS DO TABULEIRO                 ")
print("____________________________________________________")
print(f"O seu héroi, o {heroi_1}, ficou com {vida_h1} de vida!")

if vida_ataquePAE1 <= 0:
    print(f"O seu lacaio {escolha_1} morreu, seus pontos de dano são {dano_E1}!")
elif vida_ataquePAE1 > 0:
    print(f"O seu lacaio {escolha_1} ficou com {vida_E1} de vida e {dano_E1} pontos de dano!")

print(f"Seu lacaio {escolha_NE1} ficou com {vida_NE1} de vida e {dano_NE1} pontos de dano!")

#STATUS FINAL INIMIGO
#SE A ESCOLHA NÃO FOR O HÉROI INIMIGO

if escolha_2 != heroi_2 and vida_ataquePAE2 <= 0:
    print(f"O héroi inimigo {heroi_2} ficou com {vida_h2} de vida!")
    print(f"O lacaio inimigo {escolha_2} morreu, seus pontos de dano são {dano_E2}!")
    print(f"O lacaio inimigo {escolha_NE2} ficou com {vida_NE2} de vida e {dano_NE2} pontos de dano!")
elif escolha_2 != heroi_2 and vida_ataquePAE2 > 0:
    print(f"O héroi inimigo {heroi_2} ficou com {vida_h2} de vida!")
    print(f"O lacaio inimigo {escolha_2} ficou com {vida_E2} de vida e {dano_E2} pontos de dano!")
    print(f"O lacaio inimigo {escolha_NE2} ficou com {vida_NE2} de vida e {dano_NE2} pontos de dano!")

#SE A ESCOLHA FOR O HÉROI INIMIGO

if escolha_2 == heroi_2 and vida_E2 <= 0:
    print(f"O héroi inimigo {escolha_2} morreu!")
    print(f"O lacaio inimigo {escolha_NE2} ficou com {vida_NE2} de vida e {dano_NE2} pontos de dano!")
    print(f"O lacaio inimigo {escolha_NE3} ficou com {vida_NE3} de vida e {dano_NE3} pontos de dano!")
elif escolha_2 == heroi_2 and vida_E2 > 0:
    print(f"O héroi inimigo {heroi_2} ficou com {vida_E2} de vida!")
    print(f"O lacaio inimigo {escolha_NE2} ficou com {vida_NE2} de vida e {dano_NE2} pontos de dano!")
    print(f"O lacaio inimigo {escolha_NE3} ficou com {vida_NE3} de vida e {dano_NE3} pontos de dano!")

#FINALIZAÇÃO

print("____________________________________________________")
print("              OBRIGADO POR JOGAR!                   ")
print("____________________________________________________")
