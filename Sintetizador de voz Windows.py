# -*-coding: utf-8-*-

# pip install comtypes
# https://msdn.microsoft.com/en-us/library/ms723602(v=vs.85).aspx

try:
    import comtypes.client
except ImportError:
    from pip._internal import main

    main(['install', '--user', 'comtypes'])
    import comtypes.client

tts = comtypes.client.CreateObject("sapi.SPVoice")

# texto = open('1Pedro.txt', 'r')
# voz = texto.readlines()

texto = '1ª Carta de Pedro. Capitulo 1 1. Pedro, apóstolo de Jesus Cristo, aos eleitos que são estrangeiros e estão espalhados no Ponto, Galácia, Capadócia, Ásia e Bitínia 2. - eleitos segundo a presciência de Deus Pai, e santificados pelo Espírito, para obedecer a Jesus Cristo e receber a sua parte da aspersão do seu sangue. A graça e a paz vos sejam dadas em abundância. 3. Bendito seja Deus, o Pai de nosso Senhor Jesus Cristo! Na sua grande misericórdia ele nos fez renascer pela ressurreição de Jesus Cristo dentre os mortos, para uma viva esperança, 4. para uma herança incorruptível, incontaminável e imarcescível, reservada para vós nos céus; 5. para vós que sois guardados pelo poder de Deus, por causa da vossa fé, para a salvação que está pronta para se manifestar nos últimos tempos. 6. É isto o que constitui a vossa alegria, apesar das aflições passageiras a vos serem causadas ainda por diversas provações, 7. para que a prova a que é submetida a vossa fé (mais preciosa que o ouro perecível, o qual, entretanto, não deixamos de provar ao fogo) redunde para vosso louvor, para vossa honra e para vossa glória, quando Jesus Cristo se manifestar. 8. Este Jesus vós o amais, sem o terdes visto; credes nele, sem o verdes ainda, e isto é para vós a fonte de uma alegria inefável e gloriosa, 9. porque vós estais certos de obter, como preço de vossa fé, a salvação de vossas almas. 10. Esta salvação tem sido o objeto das investigações e das meditações dos profetas que proferiram oráculos sobre a graça que vos era destinada. 11. Eles investigaram a época e as circunstâncias indicadas pelo Espírito de Cristo, que neles estava e que profetizava os sofrimentos do mesmo Cristo e as glórias que os deviam seguir. 12. Foi-lhes revelado que propunham não para si mesmos, senão para vós, estas revelações que agora vos têm sido anunciadas por aqueles que vos pregaram o Evangelho da parte do Espírito Santo enviado do céu. Revelações estas, que os próprios anjos desejam contemplar. 13. Cingi, portanto, os rins do vosso espírito, sede sóbrios e colocai toda vossa esperança na graça que vos será dada no dia em que Jesus Cristo aparecer. 14. À maneira de filhos obedientes, já não vos amoldeis aos desejos que tínheis antes, no tempo da vossa ignorância. 15. A exemplo da santidade daquele que vos chamou, sede também vós santos em todas as vossas ações, pois está escrito: 16. Sede santos, porque eu sou santo (Lv 11,44). 17. Se invocais como Pai aquele que, sem distinção de pessoas, julga cada um segundo as suas obras, vivei com temor durante o tempo da vossa peregrinação. 18. Porque vós sabeis que não é por bens perecíveis, como a prata e o ouro, que tendes sido resgatados da vossa vã maneira de viver, recebida por tradição de vossos pais, mas pelo precioso sangue de Cristo, 19. o Cordeiro imaculado e sem defeito algum, aquele que foi predestinado antes da criação do mundo 20. e que nos últimos tempos foi manifestado por amor de vós. 21. Por ele tendes fé em Deus, que o ressuscitou dos mortos e glorificou, a fim de que vossa fé e vossa esperança se fixem em Deus. 22. Em obediência à verdade, tendes purificado as vossas almas para praticardes um amor fraterno sincero. Amai-vos, pois, uns aos outros, ardentemente e do fundo do coração. 23. Pois fostes regenerados não duma semente corruptível, mas pela palavra de Deus, semente incorruptível, viva e eterna. 24. Porque toda carne é como a erva, e toda a sua glória como a flor da erva. Seca-se a erva e cai a flor, mas a palavra do Senhor permanece eternamente (Is 40,6s). Ora, esta palavra é a que vos foi anunciada pelo Evangelho. '

voz = str(texto)

print('Sintetizando')

tts.Rate = 1  # Velocidade
tts.Volume = 100  # Volume
tts.Speak(voz)

# v = tts.GetVoices()
# totalDeVoz = len(v)

# frase2 = u"Este computador tem %d vozes instaladas, são elas:" % totalDeVoz
# print (frase2)
# tts.Speak(frase2)

# pega o nome da voz de numero 0
# nomeVoz = v[0].GetDescription()
# Lista o nome de todas as vozes instaladas
# for i in v:
#  print (i.GetDescription())

# Sintetiza o nome de todas as vozes instaladas
# for i in v:
# x = tts.Speak(i.GetDescription())
