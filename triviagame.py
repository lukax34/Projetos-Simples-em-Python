print("Bem vindo(a) ao meu jogo de perguntas!")
playing = input("Vamos jogar? (s/n):  ")

if playing.lower() != "s":
    print("Até mais!!")
    quit()

print("Que comecem os jogos!!")
score = 0


print("Quem foi a primeira pessoa a viajar no Espaço? \n a) Yuri Gagarin \n b) A cadela Laika \n c) Neil Armstrong \n d) Marcos Pontes")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "a" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")
    

print("Qual a montanha mais alta do mundo? \n a) Mauna Kea\n b) Dhaulagiri\n c) Monte Chimborazo\n d) Monte Everest")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "d" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "a":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")


print("Onde se localiza Machu Picchu?\n a) Colômbia\n b) Peru\n c) China\n d) Bolívia")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "b" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "a" or lowanswer == "c" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")


print("Que país tem o formato de uma bota?\n a) Butão\n b) Brasil\n c) Portugal\n d) Itália")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "d" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "a":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")

print("Quem inventou a lâmpada?\n a) Graham Bell\n b) Steve Jobs\n c) Thomas Edison\n d) Henry Ford")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "c" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "a" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")


print("Quanto tempo a Terra demora para dar uma volta completa em torno dela mesma?\n a) Aproximadamente 24 horas\n b) 365 dias\n c) 7 dias\n d) 365 ou 366 dias")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "a" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")

print("A que temperatura a água ferve?\n a) 200 ºC\n b) -10 ºC \n c) 180 ºC\n d) 100 ºC")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "d" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "a":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")

print("Quais são as fases da Lua?\n a) Nova, cheia e superlua\n b) Penumbral, lunar parcial, lunar total e cheia\n c) Nova, cheia, minguante e lua de sangue\n d) Nova, crescente, cheia e minguante")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "d" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "c" or lowanswer == "a":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")

print("Quantos ossos temos no nosso corpo?\n a) 126\n b) 206\n c) 18\n d) 300")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "b" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "a" or lowanswer == "c" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")

print("Qual o planeta mais próximo do Sol?\n a) Netuno\n b) Júpiter\n c) Mercúrio\n d) Terra")
answer = input("Resposta: ")
lowanswer = answer.lower()

if lowanswer == "c" :
    print("Você acertou!!!")
    score += 10
elif lowanswer == "b" or lowanswer == "a" or lowanswer == "d":
    print("Você errou!!")
else:
    print("Digite a letra de uma alternativa para responder... ")
    print("Perdeu 10 pontos")


print(f"A sua pontuação foi de {score} pontos!!")