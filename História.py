import random

personagens = ["um astronauta", "uma princesa", "um robô", "um pirata", "uma cientista"]
acoes = ["descobriu um tesouro", "construiu uma máquina do tempo", "salvou o mundo", "encontrou um alienígena", "se perdeu no espaço"]
locais = ["em uma ilha misteriosa", "no meio do deserto", "em uma galáxia distante", "no fundo do mar", "em uma floresta encantada"]

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

historia = f"Certa vez, {personagem} {acao} {local}."
print(historia)