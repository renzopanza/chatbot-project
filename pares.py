pares_lista = [

    # Ficção cientifica, Fantasia, Romance, Terror, Suspense, Drama, Narrativa literária, Ação, Humor/Comedia



     [
        r"oi(.*)|(.*)oiii?(.*)|(.*)ol[aá](.*)|(.*)e ai(.*)|(.*)e ai(.*)|(.*)bom dia(.*)|(.*)boa tarde(.*)|(.*)boa noite(.*)|salve|opa|co[eé]|eae|yo|hey|oiiiii?|oiie|oie",
        [
            "Oi! Tudo bem? Me conta: qual gênero de livro você mais gosta?",
            "Olá! Querendo um livro? Qual gênero mais te agrada?",
            "E ai? Quer ler algo legal, ne? Qual gênero você vai querer hoje?"
        ]
    ],
    [
        r"(.*)recomend[ae]*g[eê]nero(.*)",
        [
            "Adoro ajudar a encontrar o gênero perfeito! Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Que legal que você quer uma sugestão! Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?"
        ]

    ],

    [
        r"(.*)mais op[cç][oõ]es(.*)|(.*)outras op[cç][oõ]es(.*)|(.*)s[óo]*essas op[cç][oõ]es(.*)|(.*)somente*essas op[cç][oõ]es(.*)",
        [
            "Você quer mais opções? E qual de gênero você quer mais opções?"
        ]
    ],

    [
        r"(.*)n[ãa]o sei*g[eê]nero(.*)|(.*)qualquer g[êe]nero(.*)|(.*)qualquer um(.*)|(.*)não me decidi(.*)|(.*)me recomende um(.*)",
        [
            "Adoro ajudar a encontrar o gênero perfeito! Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Que legal que você quer uma sugestão! Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?"
        ]

    ],
    [
        r"n[ãa]o sei|n[aã]o gostei de nenhum|(.*)nenhum(.*)",
        [
            "Está confuso? Tudo bem, vamos tentar encontrar algo que você goste. Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Está confuso? Tudo bem, vamos tentar encontrar algo que você goste. Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?",
            "Poxa, que pena. Mas vamos tentar encontrar algo legal. Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Tenho certeza que podemos encontrar algo que te agrade. Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?",
            "Tenho certeza que podemos encontrar algo que te agrade. Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Poxa, que pena. Mas vamos tentar encontrar algo legal. Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?",
        ]
    ],
    [
        r"(.*)n[ãa]o gosto(.*)|(.*)odeio(.*)|(.*)ruim(.*)|(.*)p[eé]ssimo|(.*)horr[íi]vel|(.*)merda(.*)",
        [
            "Não gosta? Tudo bem, vamos tentar encontrar algo que você goste. Você prefere histórias que te transportam para mundos fantásticos ou que exploram mistérios da vida real?",
            "Tudo bem, vamos tentar encontrar algo que você goste. Você gosta mais de livros que te fazem sentir adrenalina ou que trazem reflexões profundas?"
        ]
    ],

    # Nível 2: Aprofundando as preferências
    [
        r"(.*)mundos fant[aá]sticos(.*)|(.*)fant[aá]sticos(.*)",
        [
            "Mundos fantásticos são incríveis! Você prefere histórias com criaturas mágicas ou com viagens por terras desconhecidas?"
        ]
    ],
    [
        r"(.*)mist[eé]rios da vida real(.*)|(.*)vida real(.*)",
        [
            "Mistérios da vida real são bem envolventes! Você gosta mais de tramas com segredos escondidos ou com investigações detalhadas?"
        ]
    ],
    [
        r"(.*)adrenalina(.*)",
        [
            "Adrenalina é pura emoção! Você prefere ação que não para ou suspense que te deixa tenso?"
        ]
    ],
    [
        r"(.*)reflex[õo]es profundas(.*)|(.*)profundas(.*)",
        [
            "Reflexões profundas tocam a alma! Você gosta mais de histórias sobre relações humanas ou sobre dilemas pessoais?"
        ]
    ],

    # Nível 3: Recomendação de dois gêneros e pergunta sobre preferência
    [
        r"(.*)criaturas m[aá]gicas(.*)|(.*)m[aá]gicas(.*)",
        [
            "Com base nisso, acho que você ia curtir Fantasia ou Ficção Científica! Fantasia te leva a mundos com dragões e feitiços, enquanto Ficção Científica explora galáxias e tecnologias. Qual dos dois você escolhe?"
        ]
    ],
    [
        r"(.*)terras desconhecidas(.*)|(.*)desconhecidas(.*)",
        [
            "Parece que você gosta de explorar! Eu recomendaria Fantasia ou Aventura. Fantasia tem reinos mágicos, e Aventura te leva a jornadas épicas. Qual dos dois você prefere?"
        ]
    ],
    [
        r"(.*)segredos? escondidos?(.*)|(.*)escondidos?(.*)",
        [
            "Segredos são o seu forte, hein? Acho que Suspense ou Romance seriam ótimos! Suspense te mantém na dúvida, e Romance revela segredos do coração. Qual você prefere?"
        ]
    ],
    [
        r"(.*)investiga[çc][õo]es detalhadas?(.*)|(.*)detalhadas?(.*)|(.*)investiga[çc][ãa]o detalhadas?(.*)",
        [
            "Investigações são perfeitas para mentes curiosas! Eu diria Suspense ou Policial. Suspense te prende com reviravoltas, e Policial foca em desvendar crimes. Qual você escolhe?"
        ]
    ],
    [
        r"(.*)a[çc][aã]o que n[aã]o para(.*)|(.*)a[çc][aã]o(.*)",
        [
            "Você curte um ritmo acelerado! Aventura ou Thriller podem ser ideais. Aventura tem exploração e coragem, enquanto Thriller é pura tensão. Qual você prefere?"
        ]
    ],
    [
        r"(.*)suspense que te deixa tenso(.*)|(.*)tenso(.*)",
        [
            "Tensão é o seu lance! Acho que Suspense ou Terror seriam perfeitos. Suspense te mantém alerta, e Terror mexe com seus medos. Qual dos dois você escolhe?"
        ]
    ],
    [
        r"(.*)rela[çc][õo]es humanas(.*)|(.*)humanas(.*)",
        [
            "Relações humanas são tão ricas! Recomendo Romance ou Drama. Romance foca no amor, e Drama explora emoções complexas. Qual você prefere?"
        ]
    ],
    [
        r"(.*)dilemas pessoais(.*)|(.*)pessoais(.*)",
        [
            "Dilemas pessoais são profundos! Acho que Drama ou Narrativa Literária seriam incríveis. Drama mergulha em conflitos internos, e Narrativa Literária reflete sobre a vida. Qual você escolhe?"
        ]
    ],
    [
        r"Qual seu nome",
        ["Pode me chamar de ChatBooK. Sou uma Inteligência Artificial que te ajuda a escolher livros incríveis. Qual seu gênero favorito?",]
    ],












    [
        r"(.*)tudo bem(.*)|(.*)como vai(.*)|(.*)beleza(.*)|(.*)blz(.*)",
        [
            "Tudo ótimo por aqui! E com você? Qual gênero de livro você mais curte?"
        ]
    ],
    [
        r"(.*)quero ler(.*)|(.*)quero um livro(.*)|(.*)tô a fim de ler(.*)",
        [
            "Boa! Qual gênero você quer ler hoje?"
        ]
    ],
    [
        r"(.*)adoro livros(.*)|(.*)gosto de ler(.*)|(.*)curto leitura(.*)",
        [
            "Muito bom! Qual gênero é o seu favorito?"
        ]
    ],
    [
        r"(.*)me ajuda(.*)|(.*)me diga algo(.*)|(.*)tô entediado(.*)|(.*)dica aí(.*)",
        [
            "Tô aqui pra isso! Só me diga: qual gênero de livro você gosta mais?"
        ]
    ],
    [
        r"(.*)obrigado(.*)|(.*)valeu(.*)|(.*)agradeço(.*)",
        [
            "De nada! Se quiser mais recomendações, é só dizer um gênero de livro que você gosta."
        ]
    ],
    [
        r"(.*)legal(.*)|(.*)massa(.*)|(.*)curti(.*)|gostei(.*)",
        [
            "Que bom! Agora me diz: qual gênero de livro você quer pra sua próxima leitura?"
        ]
    ],
    [
        r"(.*)não sei(.*)|(.*)tanto faz(.*)|(.*)qualquer um(.*)",
        [
            "Sem problemas! Mas me ajuda aí, escolhe um gênero que você costuma gostar mais?"
        ]
    ],




    [
        r"(.*)me recomenda um livro(.*)|(.*)recomenda um livro(.*)|(.*)recomende*livros?(.*)",
        [
            "Claro! Mas antes preciso saber qual gênero literário você mais gosta. Qual é? "
        ]
    ],
    [
        r"(.*)dica de livros?(.*)|(.*)indica.*livro(.*)|(.*)me indica.*livro(.*)|(.*)quero*livros?(.*)",
        [
            "Com certeza! Qual gênero você costuma gostar mais?",
            "Claro! Você prefere Romance, Suspense ou Ação? Se não gostar desses qual outro você gosta?"
        ]
    ],
    [
        r"(.*)o que voc[eê] sugere(.*)|(.*)qual livro*voc[eê] sugere(.*)|(.*)me sugere um livro(.*)",
        [
            "Posso sugerir algo legal! Qual gênero você prefere?",
        ]
    ],
    [
        r"(.*)n[aã]o sei o que ler(.*)|(.*)sem ideia do que ler(.*)|(.*)preciso de um livro(.*)",
        [
            "Vamos achar um livro pra você! Me diz qual gênero você gosta mais."
        ]
    ],
    [
        r"(.*)algo leve(.*)|(.*)quero um livro leve(.*)",
        [
            "Legal! Qual gênero você costuma curtir em leituras mais leves?"
        ]
    ],
    [
        r"(.*)algo profundo(.*)|(.*)quero refletir(.*)|(.*)me fazer pensar(.*)",
        [
            "Boa! Qual gênero você acha mais interessante quando quer refletir?"
        ]
    ],
    [
        r"(.*)quero aprender(.*)|(.*)quero estudar(.*)|(.*)quero melhorar(.*)",
        [
            "Ótimo! Qual gênero você acha mais útil ou interessante pra isso?"
        ]
    ],
    [
        r"(.*)quero relaxar(.*)|(.*)quero distrair(.*)|(.*)livro divertido(.*)",
        [
            "Show! Qual gênero você gosta mais quando quer relaxar com uma boa leitura?"
        ]
    ],
    [
        r"(.*)já li (.*) quero algo parecido(.*)|(.*)parecido com (.*)",
        [
            "Beleza! Qual era o gênero do livro que você leu?"
        ]
    ],
    [
        r"(.*)livro curto(.*)|(.*)rápido de ler(.*)|(.*)história curta(.*)",
        [
            "Entendi! Qual gênero você gosta mais pra leituras rápidas?"
        ]
    ],
    [
        r"(.*)livro longo(.*)|(.*)livro grande(.*)|(.*)história longa(.*)",
        [
            "Boa! Qual gênero você prefere para leituras mais longas e imersivas?"
        ]
    ],
    [
        r"(.*)qual livro devo ler(.*)|(.*)o que devo ler(.*)",
        [
            "Me conta: qual gênero literário você gosta mais?"
        ]
    ],
    [
        r"(.*)indica alguma coisa(.*)|(.*)alguma sugestão(.*)",
        [
            "Claro! Pra eu te indicar algo legal, qual gênero você curte mais?"
        ]
    ],








    # PARES FICÇÃO CIENTIFICA
    [
    r"(.*)fic[cç][ãa]o cient[íi]fica(.*)|(.*)sifi.?|ficção|sci fy.?|(.*)scify.?",
    [
    "Claro! Ficção cientifica é realmente um dos gêneros mais interessantes e instigantes que existe, pois nos faz pensar sobre os limites da ciência e o que seria possìvel na realidade. Mas me diga, na ficção científica você prefere viagens no tempo, contato com extraterrestres ou futuros distópicos?"
    ]
    ],
        [
        r"(.*)viagens no tempo(.*)|(.*viagem no tempo(.*))",
        ["Viagens no tempo sempre rendem histórias instigantes! Você prefere histórias com paradoxos temporais ou mudanças na linha do tempo?",
        "Ah, histórias de viagens no tempo são fascinantes! Você gosta mais de histórias com paradoxos temporais ou mudanças na linha do tempo?"]
        ],
            [
            r"(.*)paradoxos temporais(.*)|(.*)paradoxos(.*)",
            ["Paradoxos temporais sempre desafiam a lógica! Você prefere histórias onde o personagem se encontra com ele mesmo ou onde muda eventos e cria realidades alternativas?",
            "Esses dilemas temporais são geniais! Você curte mais histórias onde o personagem se encontra com ele mesmo ou onde muda eventos e cria realidades alternativas?"]
            ],
                [
                r"(.*)encontra com ele mesmo(.*)|(.*)encontra com ele(.*)",
                ["Encontros consigo mesmo são sempre carregados de tensão e reflexão. Você prefere quando isso gera autoconhecimento ou quando provoca colapsos temporais perigosos?",
                "Esses encontros levantam dilemas pessoais profundos. Você curte mais quando isso gera autoconhecimento ou quando provoca colapsos temporais perigosos?"]
                ],
                    [
                    r"(.*)gera autoconhecimento(.*)",
                    ["Histórias que despertam autoconhecimento são sempre poderosas e emocionantes. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)colapsos temporais(.*)|(.*)colapsos(.*)",
                    ["Colapsos temporais deixam tudo à beira do caos! Uma escolha intensa. Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)realidades alternativas(.*)",
                ["Realidades alternativas abrem infinitas possibilidades! Você prefere histórias em que o personagem tenta voltar à linha original ou quando aceita viver nessa nova realidade?",
                "Essas bifurcações de tempo são fascinantes. Você curte mais histórias em que o personagem tenta voltar à linha original ou quando aceita viver nessa nova realidade?"]
                ],
                    [
                    r"(.*)tenta voltar à linha original(.*)|(.*)voltar(.*)|(.*)linha original(.*)",
                    ["Personagens que tentam consertar o tempo mostram determinação e sacrifício. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)aceita viver nessa nova realidade(.*)|(.*)na nova(.*)|(.*)nova realidade(.*)",
                    ["Aceitar uma nova realidade exige coragem e adaptação. Um caminho cheio de possibilidades. Qual outro gênero você gosta?"]
                    ],
            [
            r"(.*)mudan[çc]as na linha do tempo(.*)",
            ["Mudar a linha do tempo sempre traz consequências imprevisíveis! Você gosta mais de tramas em que o protagonista tenta salvar alguém ou mudar o rumo da história?",
            "Essas histórias mexem com o destino das coisas. Você prefere quando o protagonista tenta salvar alguém ou mudar o rumo da história?"]
            ],
            [
                r"(.*)salvar algu[eé]m(.*)",
                ["Tentar salvar alguém é sempre emocionante e perigoso! Você prefere quando tudo dá errado e vira tragédia ou quando há um final surpreendentemente positivo?",
                "Essas histórias mexem com emoções fortes. Você curte mais quando tudo dá errado e vira tragédia ou quando há um final surpreendentemente positivo?"]
                ],
                    [
                    r"(.*)tudo dá errado.*trag[eé]dia(.*)d[aá] errado(.*)",
                    ["Final trágico? Isso sempre deixa uma marca profunda. Que escolha intensa! Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)surpreendentemente positivo(.*)|(.*)final positivo(.*)",
                    ["Reviravoltas positivas dão aquele alívio e esperança no final! Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)mudar o rumo da hist[oó]ria(.*)|(.*)mudar*hist[oó]ria",
                ["Alterar o curso da história pode mudar o mundo! Você prefere histórias que tratam de grandes eventos históricos ou mudanças pequenas que geram grandes impactos?",
                "Essas mudanças são sempre um risco. Você curte mais histórias que tratam de grandes eventos históricos ou mudanças pequenas que geram grandes impactos?"]
                ],
                    [
                    r"(.*)grandes eventos hist[oó]ricos(.*)|(.*)grandes eventos(.*)",
                    ["Recriar grandes eventos históricos com ficção é uma forma incrível de refletir sobre o passado. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)mudan[çc]as pequenas.*grandes impactos(.*)",
                    ["Adoro essas mudanças sutis que transformam tudo! Pequenas ações, grandes consequências. Qual outro gênero você gosta?"]
                ],

        [
        r"(.*)contato com extraterrestres?(.*)|(.*)extraterrestres?(.*)|(.*)aliens|(.*)alienigenas(.*)|(.*)ets?",
        ["Contatos com extraterrestres são cheios de mistério e possibilidades! Você prefere quando os aliens são hostis ou quando são seres enigmáticos que vêm em paz?",
        "Esse tema sempre dá margem pra teorias incríveis! Você curte mais histórias quando os aliens são hostis ou quando são seres enigmáticos que vêm em paz?"]
        ],
            [
            r"(.*)aliens? hostis(.*)|hostis",
            ["Invasões alienígenas sempre rendem ação e tensão! Você prefere quando a humanidade luta de forma heroica ou quando está completamente indefesa?",
            "Histórias com aliens hostis são cheias de adrenalina. Você curte mais quando a humanidade luta de forma heroica ou quando está completamente indefesa?"]
            ],
                [
                r"(.*)luta de forma heroica(.*)|luta heroica",
                ["A resistência humana é sempre inspiradora! Você prefere histórias com alianças improváveis ou com heróis solitários que mudam tudo?",
                "Lutas épicas sempre empolgam. Você curte mais histórias com alianças improváveis ou com heróis solitários que mudam tudo?"]
                ],
                    [
                    r"(.*)alian[çc]as improv[aá]veis(.*)|(.*)alian[cç]a improv[aá]vel(.*)",
                    ["Alianças improváveis sempre trazem boas surpresas e grandes reviravoltas! Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)her[oó]is solit[aá]rios(.*)",
                    ["Heróis solitários mostram força e vulnerabilidade de forma única. Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)humanidade indefesa(.*)",
                ["Quando a humanidade está indefesa, tudo vira um suspense angustiante. Você prefere histórias com fuga e sobrevivência ou com busca desesperada por ajuda externa?",
                "Esse tipo de narrativa deixa a tensão no ar. Você curte mais histórias com fuga e sobrevivência ou com busca desesperada por ajuda externa?"]
                ],
                    [
                    r"(.*)fuga*sobreviv[eê]ncia(.*)",
                    ["Narrativas de fuga e sobrevivência sempre prendem a atenção! Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)busca desesperada por ajuda externa(.*)|(.*)ajuda externa(.*)",
                    ["Essa busca por ajuda externa dá um tom desesperador e emocionante à história. Qual outro gênero você gosta?"]
                    ],
            [
            r"(.*)aliens? enigm[aá]ticos?|aliens? pac[ií]ficos(.*)|pac[ií]ficos?|(.*)enigm[áa]ticos?|(.*)paz(.*)",
            ["Aliens misteriosos levantam mil questões! Você prefere quando eles compartilham conhecimento ou quando deixam pistas para serem decifradas?",
            "Esse tipo de história sempre tem uma vibe filosófica. Você curte mais quando eles compartilham conhecimento ou quando deixam pistas para serem decifradas?"]
            ],
                [
                r"(.*)compartilham? conhecimentos(.*)",
                ["Aliens que compartilham conhecimento sempre mudam a visão da humanidade. Você prefere quando isso desperta união global ou quando gera caos por medo do desconhecido?",
                "O impacto desse contato é profundo. Você curte mais quando isso desperta união global ou quando gera caos por medo do desconhecido?"]
                ],
                    [
                    r"(.*)uni[aã]o global(.*)",
                    ["A união global diante do desconhecido é um símbolo forte de esperança. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)caos por medo do desconhecido(.*)|(.*)medo*desconhecido(.*)",
                    ["O medo do desconhecido gerando caos é um espelho da própria humanidade. Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)pistas para serem decifradas(.*)|(.*)pistas*decifradas(.*)",
                ["Pistas alienígenas são puro mistério! Você prefere tramas em que um grupo investiga aos poucos ou histórias com simbolismos que só fazem sentido no final?",
                "Essas histórias são cheias de enigmas. Você curte mais tramas em que um grupo investiga aos poucos ou histórias com simbolismos que só fazem sentido no final?"]
                ],
                    [
                    r"(.*)investiga aos poucos(.*)",
                    ["Investigações coletivas criam aquele suspense gostoso que vai crescendo aos poucos. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)simbolismos*no final(.*)",
                    ["Simbolismos que só se revelam no final deixam a gente pensando por dias! Qual outro gênero você gosta?"]
                    ],  
        [
        r"(.*)futuro dist[oó]pico(.*)|(.*)distopia",
        ["Futuros distópicos mostram o lado sombrio da humanidade. Você prefere tramas com governos totalitários ou com sociedades colapsadas tentando sobreviver?",
        "Distopias nos fazem refletir sobre o presente. Você gosta mais de histórias com governos totalitários ou com sociedades colapsadas tentando sobreviver?"]
        ],
            [
            r"(.*)governos? totalit[aá]rios(.*)",
            ["Governos opressores criam cenários tensos e cheios de vigilância. Você prefere rebeliões contra o sistema ou personagens tentando sobreviver sem chamar atenção?",
            "Distopias com regimes autoritários são bem intensas. Você curte mais rebeliões contra o sistema ou personagens tentando sobreviver sem chamar atenção?"]
            ],
                [
                r"(.*)rebeli[oõ]es contra o sistema(.*)|rebeli[õo]es",
                ["Rebeliões distópicas são sempre cheias de adrenalina. Você prefere revoluções em grande escala ou pequenos grupos agindo nas sombras?",
                "Essa luta contra o sistema é simbólica. Você gosta mais de revoluções em grande escala ou pequenos grupos agindo nas sombras?"]
                ],
                    [
                    r"(.*)revolu[cç][oõ]es em grande escala(.*)",
                    ["Revoluções em grande escala sempre carregam ação, emoção e ideais fortes. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)pequenos grupos agindo nas sombras(.*)|pequenos? grupos?",
                    ["Pequenos grupos agindo nas sombras trazem aquele suspense estratégico! Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)sobreviver sem chamar aten[cç][aã]o(.*)",
                ["Sobreviver em silêncio num regime opressor é tenso e angustiante. Você prefere histórias de opressão ditatorial ou ações furtivas e planejadas?",
                "Essas tramas mostram o lado humano diante da opressão. Você curte mais histórias de opressão ditatorial ou ações furtivas e planejadas?"]
                ],
                    [
                    r"(.*)opress[aã]o ditatorial(.*)",
                    ["Narrativas com opressão ditatorial são intensas e fazem a gente refletir muito. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)a[cç][oõ]es furtivas e planejadas(.*)",
                    ["Ações furtivas e planejadas criam uma tensão constante no ar. Qual outro gênero você gosta?"]
                    ],
            [
            r"(.*)sociedades? colapsadas(.*)",
            ["Cenários de colapso social mostram o instinto de sobrevivência humano! Você prefere grupos tentando reconstruir uma nova ordem ou disputas violentas por recursos?",
            "Essas histórias mostram o caos e a esperança. Você curte mais grupos tentando reconstruir uma nova ordem ou disputas violentas por recursos?"]
            ],
                [
                r"(.*)reconstruir uma nova ordem(.*)",
                ["Reconstruir após o caos é um tema cheio de esperança. Você prefere histórias com líderes carismáticos tentando unir as pessoas ou com comunidades divididas aprendendo a cooperar?",
                "Esse recomeço é sempre complexo. Você curte mais histórias com líderes carismáticos tentando unir as pessoas ou com comunidades divididas aprendendo a cooperar?"]
                ],
                    [
                    r"(.*)l[ií]deres carism[aá]ticos(.*)",
                    ["Líderes carismáticos tentando unir as pessoas sempre inspiram! Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)comunidades divididas(.*)|(.*)aprendendo a cooperar(.*)",
                    ["Ver comunidades se unindo aos poucos é sempre uma jornada tocante. Qual outro gênero você gosta?"]
                    ],
                [
                r"(.*)disputas por recursos(.*)",
                ["Lutas por recursos escassos mostram o lado mais cru da humanidade. Você prefere conflitos brutais por sobrevivência ou alianças estratégicas que não duram muito?",
                "Essas histórias são intensas e realistas. Você curte mais conflitos brutais por sobrevivência ou alianças estratégicas que não duram muito?"]
                ],
                    [
                    r"(.*)conflitos brutais por sobreviv[eê]ncia(.*)|conflitos brutais",
                    ["Conflitos brutais por recursos mostram o lado mais intenso da luta pela vida. Qual outro gênero você gosta?"]
                    ],
                    [
                    r"(.*)alian[çc]as estrat[eé]gicas.*n[aã]o duram(.*)",
                    ["Alianças que parecem boas, mas logo desmoronam, deixam a trama cheia de reviravoltas. Qual outro gênero você gosta?"]
                    ],





# PARES FANTASIA

    # Nível 1: Tema principal - Fantasia
    [
        r"(.*)fantasia(.*)",
        [
            "Histórias de fantasia nos transportam para mundos mágicos e incríveis! Você prefere histórias com magia e feitiçaria ou com criaturas míticas?"
        ]
    ],

    # Nível 2: Subtemas de Fantasia
    [
        r"(.*)magia e feiti[cç]aria(.*)|(.*)magia(.*)|(.*)feiti[cç]aria(.*)",
        [
            "Magia e feitiçaria dão um toque especial às histórias de fantasia! Você gosta mais quando a magia é um dom natural ou quando é algo que exige estudo e prática?"
        ]
    ],
    [
        r"(.*)criaturas m[ií]ticas(.*)",
        [
            "Criaturas míticas tornam os mundos de fantasia tão vivos! Você prefere histórias com dragões majestosos ou com elfos e anões em conflitos épicos?"
        ]
    ],

    # Nível 3: Detalhando Magia e Feitiçaria
    [
        r"(.*)dom natural(.*)|(.*)magia natural(.*)",
        [
            "Magia como dom natural traz um ar de mistério! Você prefere quando os personagens nascem com poderes únicos ou quando os descobrem em momentos inesperados?"
        ]
    ],
    [
        r"(.*)estudo e pr[aá]tica(.*)|(.*)aprendida(.*)",
        [
            "Magia que exige estudo é cheia de detalhes fascinantes! Você gosta mais de sistemas de magia complexos com regras ou de uma magia fluida e intuitiva?"
        ]
    ],
    # Detalhando Criaturas Míticas
    [
        r"(.*)drag[õo]es majestosos(.*)|(.*)drag[õo]es(.*)",
        [
            "Dragões majestosos são impressionantes! Você prefere quando eles são aliados poderosos ou inimigos temidos?"
        ]
    ],
    [
        r"(.*)elfos e an[õo]es(.*)|(.*)conflitos [ée]picos(.*)",
        [
            "Elfos e anões em conflitos épicos criam tramas ricas! Você gosta mais de guerras entre raças ou alianças improváveis entre elas?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)nascem com poderes(.*)|(.*)poderes [uú]nicos(.*)",
        [
            "Nascer com poderes únicos é um peso e um presente! Você prefere quando os personagens aceitam seu destino ou quando lutam contra ele?"
        ]
    ],
    [
        r"(.*)descobrem em momentos(.*)|(.*)momentos inesperados(.*)",
        [
            "Descobrir poderes em momentos inesperados é emocionante! Você gosta mais quando isso leva a uma jornada de aprendizado ou a um confronto imediato?"
        ]
    ],
    [
        r"(.*)sistemas de magia(.*)|(.*)regras(.*)",
        [
            "Sistemas de magia complexos são intrigantes! Você prefere quando a magia tem um custo alto ou quando é usada para resolver mistérios?"
        ]
    ],
    [
        r"(.*)magia fluida e intuitiva(.*)|(.*)intuitiva(.*)",
        [
            "Magia fluida e intuitiva abre espaço para criatividade! Você gosta mais quando é usada de forma artística ou quando é perigosa e imprevisível?"
        ]
    ],
    [
        r"(.*)aliados poderosos(.*)",
        [
            "Dragões como aliados poderosos mudam o jogo! Você prefere quando eles lutam ao lado dos heróis ou quando protegem tesouros antigos?"
        ]
    ],
    [
        r"(.*)inimigos temidos(.*)",
        [
            "Dragões como inimigos temidos são de tirar o fôlego! Você gosta mais de batalhas épicas contra eles ou de tentativas de domá-los?"
        ]
    ],
    [
        r"(.*)guerras? entre ra[cç]as(.*)",
        [
            "Guerras entre raças criam tensão épica! Você prefere quando são batalhas em grande escala ou duelos entre líderes?"
        ]
    ],
    [
        r"(.*)alian[cç]as improv[aá]veis(.*)",
        [
            "Alianças improváveis trazem surpresas! Você gosta mais quando são forjadas por necessidade ou por um objetivo maior?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)aceitam seu destino(.*)|(.*)aceitar destino(.*)",
        [
            "Personagens que aceitam seu destino muitas vezes se tornam lendas! É incrível ver essa jornada de coragem. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)lutam contra ele(.*)|(.*)lutar contra destino(.*)",
        [
            "Lutar contra o destino adiciona um drama intenso à história! Uma escolha cheia de emoção. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)jornada de aprendizado(.*)",
        [
            "Uma jornada de aprendizado com poderes recém-descobertos é sempre inspiradora! Adoro esse crescimento pessoal. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)confronto imediato(.*)",
        [
            "Um confronto imediato com novos poderes traz ação instantânea! É pura adrenalina. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)custo alto(.*)",
        [
            "Magia com um custo alto dá profundidade à trama! Sacrícios assim deixam tudo mais intenso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)resolver mist[eé]rios(.*)",
        [
            "Usar magia para resolver mistérios é genial! Adoro quando a inteligência prevalece. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)forma art[ií]stica(.*)",
        [
            "Magia usada de forma artística é puro encantamento! Uma mistura linda de poder e beleza. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)perigosa e imprevis[ií]vel(.*)",
        [
            "Magia perigosa e imprevisível mantém a tensão no ar! É emocionante e arriscado. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)lutam ao lado dos her[oó]is(.*)",
        [
            "Dragões lutando ao lado dos heróis são aliados inesquecíveis! Que parceria épica. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)protegem tesouros(.*)",
        [
            "Dragões protegendo tesouros criam aventuras clássicas! Um desafio cheio de recompensas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)batalhas [ée]picas contra eles(.*)",
        [
            "Batalhas épicas contra dragões são o ápice da fantasia! Que confronto grandioso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tentativas de dom[aá]-los(.*)",
        [
            "Tentar domar dragões é uma prova de coragem e astúcia! Uma ideia ousada. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)batalhas em grande escala(.*)",
        [
            "Batalhas em grande escala entre raças são de tirar o fôlego! Um espetáculo de estratégia e força. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)duelos entre l[ií]deres(.*)",
        [
            "Duelos entre líderes trazem rivalidades pessoais à tona! É intenso e emocionante. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)necessidade(.*)",
        [
            "Alianças forjadas por necessidade mostram o poder da união em tempos difíceis! Uma lição forte. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)objetivo maior(.*)",
        [
            "Alianças por um objetivo maior elevam a história a outro nível! É inspirador ver essa determinação. E qual outro gênero você gosta?"
        ]
    ],

    # Nível 1: Tema principal - Romance
    [
        r"(.*)romance(.*)",
        [
            "Romances nos fazem sonhar e sentir intensamente! Você prefere romances contemporâneos ou romances históricos?"
        ]
    ],

    # Nível 2: Subtemas de Romance
    [
        r"(.*)contempor[aâ]neos?(.*)",
        [
            "Romances contemporâneos trazem amores modernos e relacionáveis! Você gosta mais de tropes como 'friends to lovers' ou 'enemies to lovers'?"
        ]
    ],
    [
        r"(.*)hist[oó]ricos?(.*)",
        [
            "Romances históricos nos levam a outras épocas! Você prefere histórias ambientadas na Regência ou na era Vitoriana?"
        ]
    ],

    # Nível 3: Detalhando Romances Contemporâneos e Históricos
    [
        r"(.*)friends to lovers(.*)|(.*)amigos? para amantes?(.*)",
        [
            "Friends to lovers é um trope doce e cativante! Você prefere quando os personagens são amigos de infância ou quando se conhecem mais tarde na vida?"
        ]
    ],
    [
        r"(.*)enemies to lovers(.*)|(.*)inimigos? para amantes?(.*)",
        [
            "Enemies to lovers traz tensão e química explosiva! Você gosta mais de rivalidades profissionais ou pessoais?"
        ]
    ],
    [
        r"(.*)reg[eê]ncia(.*)",
        [
            "Romances de Regência são cheios de elegância e regras sociais! Você prefere histórias com bailes e cortejos ou com escândalos e segredos?"
        ]
    ],
    [
        r"(.*)vitoriana(.*)|(.*)era vitoriana(.*)",
        [
            "A era Vitoriana é fascinante com suas convenções e inovações! Você gosta mais de histórias com nobreza ou com personagens comuns enfrentando a sociedade?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)amigos? de inf[aâ]ncia(.*)",
        [
            "Amigos de infância que se apaixonam têm uma conexão profunda! Você prefere quando há um reencontro após anos ou quando a amizade evolui naturalmente?"
        ]
    ],
    [
        r"(.*)conhecem mais tarde(.*)|(.*)mais tarde na vida(.*)",
        [
            "Conhecer o amor mais tarde traz frescor e surpresa! Você gosta mais quando há um encontro casual ou quando são forçados a trabalhar juntos?"
        ]
    ],
    [
        r"(.*)rivalidades profissionais(.*)|(.*)profissionais?(.*)",
        [
            "Rivalidades profissionais criam faíscas! Você prefere quando competem pelo mesmo objetivo ou quando têm estilos opostos?"
        ]
    ],
    [
        r"(.*)rivalidades pessoais(.*)|(.*)pessoais?(.*)",
        [
            "Rivalidades pessoais são intensas e emocionais! Você gosta mais quando há um mal-entendido do passado ou quando têm personalidades conflitantes?"
        ]
    ],
    [
        r"(.*)bailes e cortejos(.*)|(.*)bailes?(.*)|(.*)cortejos?(.*)",
        [
            "Bailes e cortejos são o coração da Regência! Você prefere danças românticas ou encontros clandestinos?"
        ]
    ],
    [
        r"(.*)esc[aâ]ndalos e segredos(.*)|(.*)esc[aâ]ndalos?(.*)|(.*)segredos?(.*)",
        [
            "Escândalos e segredos agitam a sociedade! Você gosta mais de reputações em jogo ou de amores proibidos?"
        ]
    ],
    [
        r"(.*)nobreza(.*)|(.*)nobres?(.*)",
        [
            "Romances com nobreza são cheios de glamour e dever! Você prefere casamentos arranjados que viram amor ou paixões que desafiam títulos?"
        ]
    ],
    [
        r"(.*)personagens comuns(.*)|(.*)comuns?(.*)|(.*)sociedade(.*)",
        [
            "Personagens comuns trazem uma perspectiva realista! Você gosta mais de histórias de superação ou de amores que transcendem classes?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)reencontro ap[oó]s anos(.*)|(.*)reencontro(.*)",
        [
            "Reencontros após anos são cheios de nostalgia e segundas chances! É emocionante ver o amor florescer novamente. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)amizade evolui naturalmente(.*)|(.*)evolui naturalmente(.*)",
        [
            "Uma amizade que evolui naturalmente para o amor é tão genuína e tocante! Adoro essa progressão suave. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)encontro casual(.*)|(.*)casual(.*)",
        [
            "Encontros casuais que levam ao amor são cheios de destino e surpresa! É como se o universo conspirasse a favor. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)for[cç]ados a trabalhar juntos(.*)|(.*)trabalhar juntos(.*)",
        [
            "Ser forçado a trabalhar junto e encontrar o amor no processo é uma jornada divertida! A tensão inicial se transforma lindamente. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)competem pelo mesmo objetivo(.*)|(.*)mesmo objetivo(.*)",
        [
            "Competir pelo mesmo objetivo cria uma dinâmica eletrizante! A linha entre rivalidade e atração é fina. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)estilos opostos(.*)|(.*)opostos?(.*)",
        [
            "Estilos opostos que se atraem são um clássico! Os opostos realmente se completam. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)mal-entendido do passado(.*)|(.*)mal-entendido(.*)|(.*)passado(.*)",
        [
            "Um mal-entendido do passado adiciona camadas de emoção e redenção! É gratificante ver a verdade prevalecer. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)personalidades conflitantes(.*)|(.*)conflitantes?(.*)",
        [
            "Personalidades conflitantes geram faíscas e crescimento mútuo! O amor que nasce do conflito é poderoso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)dan[cç]as rom[aâ]nticas(.*)|(.*)dan[cç]as?(.*)",
        [
            "Danças românticas são o cenário perfeito para o amor florescer! A elegância e a proximidade criam magia. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)encontros clandestinos(.*)|(.*)clandestinos?(.*)",
        [
            "Encontros clandestinos trazem emoção e risco! O amor proibido tem seu charme. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)reputa[cç][õo]es em jogo(.*)|(.*)reputa[cç][õo]es?(.*)",
        [
            "Reputações em jogo adicionam drama e urgência à história! O equilíbrio entre amor e dever é delicado. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)amores proibidos(.*)|(.*)proibidos?(.*)",
        [
            "Amores proibidos são intensos e desafiadores! Lutar contra as convenções é uma prova de amor. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)casamentos arranjados.*amor(.*)|(.*)arranjados?(.*)",
        [
            "Casamentos arranjados que viram amor são uma jornada de descoberta! Ver o afeto crescer é lindo. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)paix[õo]es que desafiam t[ií]tulos(.*)|(.*)desafiam t[ií]tulos(.*)",
        [
            "Paixões que desafiam títulos mostram que o amor não conhece barreiras! É inspirador e romântico. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)hist[oó]rias de supera[cç][aã]o(.*)|(.*)supera[cç][aã]o(.*)",
        [
            "Histórias de superação são emocionantes e inspiradoras! Ver os personagens triunfarem é gratificante. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)amores que transcendem classes(.*)|(.*)transcendem classes(.*)",
        [
            "Amores que transcendem classes sociais são poderosos e atemporais! O amor vence todas as barreiras. E qual outro gênero você gosta?"
        ]
    ],

    # Nível 1: Tema principal - Terror
    [
        r"(.*)terror(.*)",
        [
            "Terror é o gênero que nos faz perder o sono! Você prefere o medo vindo de forças sobrenaturais ou de algo que mexe com a sua mente?"
        ]
    ],

    # Nível 2: Subtemas de Terror
    [
        r"(.*)for[çc]as sobrenaturais(.*)|(.*)sobrenaturais(.*)",
        [
            "O sobrenatural sempre traz um arrepio a mais! Você gosta mais de assombrações ou de criaturas do inferno?"
        ]
    ],
    [
        r"(.*)mexe com a mente(.*)|(.*)mente(.*)",
        [
            "O terror que brinca com a cabeça é intenso! Você prefere sentir uma tensão que não explica ou ser enganado por truques psicológicos?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)assombra[çc][õo]es(.*)|(.*)esp[ií]ritos(.*)",
        [
            "Assombrações têm aquele charme assustador! Você prefere espíritos que voltam por vingança ou aqueles que estão presos em um looping eterno?"
        ]
    ],
    [
        r"(.*)criaturas do inferno(.*)|(.*)inferno(.*)|(.*)dem[oô]nios(.*)",
        [
            "Criaturas do inferno são puro terror! Você gosta mais de casos de possessão ou de acordos sombrios com entidades?"
        ]
    ],
    [
        r"(.*)tens[aã]o que n[aã]o explica(.*)|(.*)tens[aã]o que n[aã]o se explica(.*)|(.*)sem explica[çc][aã]o(.*)",
        [
            "Tensão sem explicação deixa a gente sem chão! Você prefere quando o medo vem de dentro ou quando ninguém parece confiável?"
        ]
    ],
    [
        r"(.*)truques? psicol[oó]gicos?(.*)|(.*)psicol[oó]gicos(.*)",
        [
            "Truques psicológicos são geniais e perturbadores! Você gosta mais de alguém sendo reprogramado ou de um controle invisível que domina?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)volta[m] por vingan[çc]a(.*)|(.*)vingan[çc]a(.*)",
        [
            "Espíritos vingativos são implacáveis! Você acha mais assustador quando eles punem com razão ou quando atacam sem critério?"
        ]
    ],
    [
        r"(.*)presos em um looping eterno(.*)|(.*)looping eterno(.*)",
        [
            "Espíritos presos em um looping são de gelar! Você prefere quando alguém tenta libertá-los ou quando eles apenas assombram sem fim?"
        ]
    ],
    [
        r"(.*)casos de possess[aã]o(.*)|(.*)possess[aã]o(.*)",
        [
            "Possessão é o auge do medo! Você gosta mais de rituais para expulsar o mal ou da batalha dentro da pessoa possuída?"
        ]
    ],
    [
        r"(.*)acordos sombrios com entidades(.*)|(.*)acordos sombrios(.*)",
        [
            "Acordos sombrios têm um preço alto! Você prefere quem tenta burlar o trato ou quem abraça as consequências?"
        ]
    ],
    [
        r"(.*)medo vem de dentro(.*)|(.*)vem de dentro(.*)",
        [
            "Medo vindo de dentro é sufocante! Você acha pior quando a pessoa perde o senso de realidade ou quando tudo parece um pesadelo fabricado?"
        ]
    ],
    [
        r"(.*)ningu[eé]m parece confi[aá]vel(.*)|(.*)n[aã]o confi[aá]vel(.*)",
        [
            "Quando ninguém é confiável, o terror é constante! Você prefere segredos em uma vila isolada ou em um lugar onde não há saída?"
        ]
    ],
    [
        r"(.*)algu[eé]m sendo reprogramado(.*)|(.*)reprogramado(.*)",
        [
            "Reprogramar a mente é assustadoramente real! Você gosta mais de uma multidão manipulada ou de uma pessoa transformada em arma?"
        ]
    ],
    [
        r"(.*)controle invis[ií]vel que domina(.*)|(.*)controle invis[ií]vel(.*)",
        [
            "Controle invisível é o terror sutil! Você prefere um vilão com planos cruéis ou um teste que foge ao controle?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)punem com raz[aã]o(.*)|(.*)com raz[aã]o(.*)",
        [
            "Espíritos que punem com razão têm um toque de justiça sombria! É quase poético, mas ainda assusta. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)atacam sem crit[eé]rio(.*)|(.*)sem crit[eé]rio(.*)",
        [
            "Espíritos que atacam sem critério são o caos puro! Ninguém escapa desse terror. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tenta libert[aá]-los(.*)|(.*)libert[aá]-los(.*)",
        [
            "Tentar libertar espíritos presos é heroico e arrepiante! Uma luz no meio do medo. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)assombram sem fim(.*)|(.*)sem fim(.*)",
        [
            "Assombrações sem fim são o pesadelo que não termina! O terror em looping. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)rituais para expulsar o mal(.*)|(.*)expulsar o mal(.*)",
        [
            "Rituais de expulsão são tensos e épicos! O confronto com o mal em carne viva. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)batalha dentro da pessoa possu[ií]da(.*)|(.*)dentro da pessoa(.*)",
        [
            "A batalha interna de um possuído é pura emoção! O terror na alma. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tenta burlar o trato(.*)|(.*)burlar o trato(.*)",
        [
            "Burlar o trato com uma entidade é ousado demais! Mas o preço sempre vem. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)abra[cç]a as consequ[eê]ncias(.*)|(.*)consequ[eê]ncias(.*)",
        [
            "Abraçar as consequências de um acordo é sombrio e fascinante! A queda em câmera lenta. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)perde o senso de realidade(.*)|(.*)senso de realidade(.*)",
        [
            "Perder o senso de realidade é o fundo do poço do terror! A mente vira inimiga. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tudo parece um pesadelo fabricado(.*)|(.*)pesadelo fabricado(.*)",
        [
            "Um pesadelo fabricado é uma prisão mental! O medo de não saber o que é real. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)segredos em uma vila isolada(.*)|(.*)vila isolada(.*)",
        [
            "Segredos em vilas isoladas são sufocantes! O terror está em cada olhar. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)lugar onde n[aã]o h[aá] sa[ií]da(.*)|(.*)sem sa[ií]da(.*)",
        [
            "Um lugar sem saída é claustrofóbico e genial! O medo sem escapatória. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)multid[aã]o manipulada(.*)|(.*)manipulada(.*)",
        [
            "Uma multidão manipulada é o terror em massa! A humanidade perdida. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)pessoa transformada em arma(.*)|(.*)transformada em arma(.*)",
        [
            "Uma pessoa transformada em arma é cruel e brilhante! A mente como ferramenta do mal. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)vil[aã]o com planos cru[eé]is(.*)|(.*)planos cru[eé]is(.*)",
        [
            "Um vilão cruel com controle invisível é clássico e aterrorizante! O mestre do medo. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)teste que foge ao controle(.*)|(.*)foge ao controle(.*)",
        [
            "Um teste que foge ao controle é o caos em forma de terror! A ciência vira monstro. E qual outro gênero você gosta?"
        ]
    ],
    
    # Nível 1: Tema principal - Suspense
    [
        r"(.*)suspense(.*)",
        [
            "Suspense é aquele gênero que nos deixa grudados na história! Você prefere tramas cheias de conspirações ou investigações cheias de pistas?"
        ]
    ],

    # Nível 2: Subtemas de Suspense
    [
        r"(.*)conspira[çc][õo]es(.*)|(.*)conspira[çc][aã]o(.*)",
        [
            "Conspirações são um labirinto de segredos! Você gosta mais de intrigas políticas ou segredos corporativos?"
        ]
    ],
    [
        r"(.*)investiga[çc][õo]es(.*)|(.*)pistas(.*)",
        [
            "Investigações mantêm a tensão no ar! Você prefere casos de assassinatos misteriosos ou desaparecimentos inexplicáveis?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)intrigas pol[ií]ticas(.*)|(.*)pol[ií]ticas(.*)",
        [
            "Intrigas políticas são cheias de traições! Você gosta mais quando envolvem jogos de poder ou revoltas secretas?"
        ]
    ],
    [
        r"(.*)segredos corporativos(.*)|(.*)corporativos(.*)",
        [
            "Segredos corporativos criam um suspense intenso! Você prefere esquemas financeiros ou experimentos proibidos?"
        ]
    ],
    [
        r"(.*)assassinatos misteriosos(.*)|(.*)assassinatos(.*)",
        [
            "Assassinatos misteriosos são de tirar o fôlego! Você gosta mais de crimes com muitos suspeitos ou um assassino que deixa pistas?"
        ]
    ],
    [
        r"(.*)desaparecimentos inexplic[aá]veis(.*)|(.*)desaparecimentos(.*)",
        [
            "Desaparecimentos inexplicáveis são intrigantes! Você prefere buscas em cidades pequenas ou em lugares isolados?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)jogos de poder(.*)|(.*)poder(.*)",
        [
            "Jogos de poder são uma dança perigosa! Você acha mais envolvente quando alguém manipula nos bastidores ou quando há confrontos diretos?"
        ]
    ],
    [
        r"(.*)revoltas secretas(.*)|(.*)revoltas(.*)",
        [
            "Revoltas secretas têm uma energia explosiva! Você prefere quando são planejadas por anos ou quando surgem de traições inesperadas?"
        ]
    ],
    [
        r"(.*)esquemas financeiros(.*)|(.*)financeiros(.*)",
        [
            "Esquemas financeiros são um suspense calculado! Você gosta mais de fraudes milionárias ou de chantagens arriscadas?"
        ]
    ],
    [
        r"(.*)experimentos proibidos(.*)|(.*)proibidos(.*)",
        [
            "Experimentos proibidos são assustadoramente fascinantes! Você prefere quando envolvem ciência perigosa ou segredos do passado?"
        ]
    ],
    [
        r"(.*)muitos suspeitos(.*)|(.*)suspeitos(.*)",
        [
            "Crimes com muitos suspeitos são um quebra-cabeça! Você gosta mais quando todos têm motivos ou quando ninguém parece culpado?"
        ]
    ],
    [
        r"(.*)assassino que deixa pistas(.*)|(.*)deixa pistas(.*)",
        [
            "Um assassino que deixa pistas é provocador! Você prefere mensagens enigmáticas ou armadilhas para os investigadores?"
        ]
    ],
    [
        r"(.*)cidades pequenas(.*)|(.*)cidade pequena(.*)",
        [
            "Cidades pequenas escondem segredos sombrios! Você prefere quando todos se conhecem ou quando há estranhos no meio?"
        ]
    ],
    [
        r"(.*)lugares isolados(.*)|(.*)isolados(.*)",
        [
            "Lugares isolados aumentam a tensão! Você gosta mais de buscas em florestas ou em construções abandonadas?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)manipula nos bastidores(.*)|(.*)bastidores(.*)",
        [
            "Manipular nos bastidores é a arte do suspense! Um mestre das sombras puxando as cordas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)confrontos diretos(.*)|(.*)confrontos(.*)",
        [
            "Confrontos diretos são pura adrenalina! A tensão explode na cara dos personagens. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)planejadas por anos(.*)|(.*)planejadas(.*)",
        [
            "Revoltas planejadas por anos são calculadas e impactantes! A paciência dos conspiradores é de arrepiar. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)trai[çc][õo]es inesperadas(.*)|(.*)trai[çc][õo]es(.*)",
        [
            "Traições inesperadas viram a trama de cabeça para baixo! Nada como um choque bem dado. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)fraudes milion[aá]rias(.*)|(.*)fraudes(.*)",
        [
            "Fraudes milionárias são um jogo de números e nervos! A ganância leva a lugares sombrios. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)chantagens arriscadas(.*)|(.*)chantagens(.*)",
        [
            "Chantagens arriscadas são um fio de navalha! Um erro e tudo desmorona. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)ci[eê]ncia perigosa(.*)|(.*)ci[eê]ncia(.*)",
        [
            "Ciência perigosa é o limite da curiosidade humana! O suspense de brincar com o proibido. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)segredos do passado(.*)|(.*)passado(.*)",
        [
            "Segredos do passado voltam com força! Desenterrar o que foi escondido é sempre tenso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)todos t[eê]m motivos(.*)|(.*)motivos(.*)",
        [
            "Quando todos têm motivos, ninguém está seguro! Um suspense onde cada um é um enigma. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)ningu[eé]m parece culpado(.*)|(.*)culpado(.*)",
        [
            "Ninguém parecer culpado é o ápice da dúvida! A tensão de não saber em quem confiar. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)mensagens enigm[aá]ticas(.*)|(.*)enigm[aá]ticas(.*)",
        [
            "Mensagens enigmáticas são um convite ao caos! Decifrá-las é como correr contra o tempo. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)armadilhas para os investigadores(.*)|(.*)armadilhas(.*)",
        [
            "Armadilhas para investigadores são cruéis e brilhantes! O assassino sempre um passo à frente. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)todos se conhecem(.*)|(.*)se conhecem(.*)",
        [
            "Quando todos se conhecem, os segredos são pessoais! O suspense corta como faca. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)estranhos no meio(.*)|(.*)estranhos(.*)",
        [
            "Estranhos no meio bagunçam tudo! A desconfiança reina em cada olhar. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)florestas(.*)",
        [
            "Florestas escondem perigos em cada sombra! A natureza vira palco de suspense. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)constru[çc][õo]es abandonadas(.*)|(.*)abandonadas(.*)",
        [
            "Construções abandonadas são cenários perfeitos para o medo! Cada rangido é uma ameaça. E qual outro gênero você gosta?"
        ]
    ],
    # Nível 1: Tema principal - Drama
    [
        r"(.*)drama(.*)",
        [
            "Drama é o gênero que toca o coração e faz refletir! Você prefere histórias sobre conflitos familiares ou dilemas pessoais?"
        ]
    ],

    # Nível 2: Subtemas de Drama
    [
        r"(.*)conflitos familiares(.*)|(.*)familiares(.*)",
        [
            "Conflitos familiares são cheios de emoção! Você gosta mais de histórias sobre heranças disputadas ou segredos de gerações?"
        ]
    ],
    [
        r"(.*)dilemas pessoais(.*)|(.*)pessoais(.*)",
        [
            "Dilemas pessoais nos fazem mergulhar na alma dos personagens! Você prefere tramas sobre crises de identidade ou escolhas morais difíceis?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)heran[çc]as disputadas(.*)|(.*)heran[çc]as(.*)",
        [
            "Heranças disputadas criam tensões intensas! Você gosta mais quando a disputa divide irmãos ou quando envolve segredos de estranhos?"
        ]
    ],
    [
        r"(.*)segredos de gera[çc][õo]es(.*)|(.*)gera[çc][õo]es(.*)",
        [
            "Segredos de gerações revelam histórias profundas! Você prefere quando são traumas do passado ou promessas não cumpridas?"
        ]
    ],
    [
        r"(.*)crises de identidade(.*)|(.*)identidade(.*)",
        [
            "Crises de identidade são tão humanas! Você gosta mais quando o personagem busca seu lugar no mundo ou quando questiona quem realmente é?"
        ]
    ],
    [
        r"(.*)escolhas morais dif[ií]ceis(.*)|(.*)morais(.*)",
        [
            "Escolhas morais difíceis são de cortar o coração! Você prefere quando envolvem sacrifícios por outros ou conflitos entre dever e desejo?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)divide irm[aã]os(.*)|(.*)irm[aã]os(.*)",
        [
            "Disputas entre irmãos são carregadas de emoção! Você acha mais intenso quando há rivalidade antiga ou quando surge por ganância?"
        ]
    ],
    [
        r"(.*)segredos de estranhos(.*)|(.*)estranhos(.*)",
        [
            "Segredos envolvendo estranhos trazem surpresas! Você prefere quando conectam famílias ou quando revelam traições inesperadas?"
        ]
    ],
    [
        r"(.*)traumas do passado(.*)|(.*)traumas(.*)",
        [
            "Traumas do passado ecoam por gerações! Você gosta mais quando são histórias de luto ou de injustiças nunca resolvidas?"
        ]
    ],
    [
        r"(.*)promessas n[aã]o cumpridas(.*)|(.*)promessas(.*)",
        [
            "Promessas não cumpridas carregam peso emocional! Você prefere quando levam a culpa ou a busca por redenção?"
        ]
    ],
    [
        r"(.*)busca seu lugar no mundo(.*)|(.*)lugar no mundo(.*)",
        [
            "Buscar um lugar no mundo é uma jornada poderosa! Você gosta mais quando é sobre aceitação ou sobre desafiar expectativas?"
        ]
    ],
    [
        r"(.*)questiona quem realmente [eé](.*)|(.*)quem realmente(.*)",
        [
            "Questionar quem realmente é mexe com tudo! Você prefere quando é uma descoberta interna ou quando há revelações externas?"
        ]
    ],
    [
        r"(.*)sacrif[ií]cios por outros(.*)|(.*)sacrif[ií]cios(.*)",
        [
            "Sacrifícios por outros são de partir o coração! Você acha mais forte quando são por amor ou por um ideal maior?"
        ]
    ],
    [
        r"(.*)conflitos entre dever e desejo(.*)|(.*)dever e desejo(.*)",
        [
            "Conflitos entre dever e desejo são tão complexos! Você prefere quando o dever vence ou quando o desejo toma conta?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)rivalidade antiga(.*)|(.*)rivalidade(.*)",
        [
            "Rivalidade antiga entre irmãos é uma ferida que não cicatriza! Traz tanta profundidade ao drama. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)surge por gan[aâ]ncia(.*)|(.*)gan[aâ]ncia(.*)",
        [
            "Ganância dividindo irmãos é uma trama poderosa! Mostra o pior e o melhor da família. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)conectam fam[ií]lias(.*)|(.*)conectam(.*)",
        [
            "Segredos que conectam famílias são emocionantes! Unem pessoas de formas inesperadas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)trai[çc][õo]es inesperadas(.*)|(.*)trai[çc][õo]es(.*)",
        [
            "Traições inesperadas abalam tudo! O drama ganha vida com essas reviravoltas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)luto(.*)",
        [
            "Traumas de luto são tão reais e comoventes! Fazem a gente refletir sobre a vida. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)injusti[çc]as nunca resolvidas(.*)|(.*)injusti[çc]as(.*)",
        [
            "Injustiças nunca resolvidas carregam um peso único! O drama brilha nesses conflitos. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)culpa(.*)",
        [
            "Culpa por promessas não cumpridas é de cortar o coração! Traz tanta humanidade à história. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)busca por reden[çc][aã]o(.*)|(.*)reden[çc][aã]o(.*)",
        [
            "A busca por redenção é uma jornada incrível! O drama floresce com esse desejo de reparar. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)aceita[çc][aã]o(.*)",
        [
            "Aceitação é um tema tão bonito no drama! Ver alguém encontrar seu lugar é inspirador. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)desafiar expectativas(.*)|(.*)expectativas(.*)",
        [
            "Desafiar expectativas é libertador! O drama ganha força com essa coragem. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)descoberta interna(.*)|(.*)interna(.*)",
        [
            "Uma descoberta interna é transformadora! O drama brilha quando o personagem se encontra. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)revela[çc][õo]es externas(.*)|(.*)externas(.*)",
        [
            "Revelações externas mudam tudo! O drama cresce com essas viradas inesperadas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)por amor(.*)|(.*)amor(.*)",
        [
            "Sacrifícios por amor são de tirar o fôlego! Nada é mais intenso no drama. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)ideal maior(.*)|(.*)ideal(.*)",
        [
            "Sacrifícios por um ideal maior são nobres e comoventes! O drama ganha profundidade assim. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)dever vence(.*)|(.*)dever(.*)",
        [
            "Quando o dever vence, o drama fica agridoce! Uma escolha cheia de peso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)desejo toma conta(.*)|(.*)desejo(.*)",
        [
            "O desejo tomando conta é pura paixão! O drama vibra com essa intensidade. E qual outro gênero você gosta?"
        ]
    ],
    # Nível 1: Tema principal - Narrativa Literária
    [
        r"(.*)narrativa liter[aá]ria(.*)",
        [
            "Narrativa literária é um mergulho profundo na experiência humana! Você prefere histórias que exploram a busca por significado ou as complexidades da memória?"
        ]
    ],

    # Nível 2: Subtemas de Narrativa Literária
    [
        r"(.*)busca por significado(.*)|(.*)significado(.*)",
        [
            "A busca por significado é tão universal! Você gosta mais de jornadas introspectivas ou de reflexões sobre o lugar na sociedade?"
        ]
    ],
    [
        r"(.*)complexidades da mem[oó]ria(.*)|(.*)mem[oó]ria(.*)",
        [
            "As complexidades da memória criam narrativas ricas! Você prefere histórias sobre lembranças fragmentadas ou narrativas que revisitam o passado?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)jornadas introspectivas(.*)|(.*)introspectivas(.*)",
        [
            "Jornadas introspectivas são um convite à reflexão! Você gosta mais quando o personagem enfrenta dúvidas existenciais ou quando busca autocompreensão?"
        ]
    ],
    [
        r"(.*)lugar na sociedade(.*)|(.*)sociedade(.*)",
        [
            "Reflexões sobre o lugar na sociedade são profundas! Você prefere tramas sobre marginalização ou sobre conformidade e rebeldia?"
        ]
    ],
    [
        r"(.*)lembran[çc]as fragmentadas(.*)|(.*)fragmentadas(.*)",
        [
            "Lembranças fragmentadas são como um quebra-cabeça emocional! Você gosta mais quando tentam reconstruir a verdade ou quando aceitam a incerteza?"
        ]
    ],
    [
        r"(.*)revisitam o passado(.*)|(.*)passado(.*)",
        [
            "Revisitar o passado é sempre intenso! Você prefere quando revela arrependimentos ou quando reconstrói relações perdidas?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)d[uú]vidas existenciais(.*)|(.*)existenciais(.*)",
        [
            "Dúvidas existenciais mexem com a alma! Você acha mais fascinante quando questionam o propósito da vida ou quando lidam com a mortalidade?"
        ]
    ],
    [
        r"(.*)autocompreens[aã]o(.*)|(.*)autocompreender(.*)",
        [
            "A busca por autocompreensão é transformadora! Você prefere quando é um processo solitário ou quando envolve conexões com outros?"
        ]
    ],
    [
        r"(.*)marginaliza[çc][aã]o(.*)|(.*)marginalizados(.*)",
        [
            "Histórias de marginalização são poderosas! Você gosta mais quando mostram resiliência ou quando exploram injustiças sociais?"
        ]
    ],
    [
        r"(.*)conformidade e rebeldia(.*)|(.*)rebeldia(.*)",
        [
            "Conformidade versus rebeldia é um conflito vibrante! Você prefere quando o personagem resiste às normas ou quando encontra um meio-termo?"
        ]
    ],
    [
        r"(.*)reconstruir a verdade(.*)|(.*)verdade(.*)",
        [
            "Reconstruir a verdade é como montar um mosaico! Você gosta mais quando a verdade é libertadora ou quando é dolorosa?"
        ]
    ],
    [
        r"(.*)aceitam a incerteza(.*)|(.*)incerteza(.*)",
        [
            "Aceitar a incerteza é tão humano! Você prefere quando isso traz paz ou quando deixa um vazio inquietante?"
        ]
    ],
    [
        r"(.*)arrependimentos(.*)",
        [
            "Arrependimentos do passado são de cortar o coração! Você gosta mais quando levam à redenção ou quando permanecem como lições?"
        ]
    ],
    [
        r"(.*)reconstr[óo]i rela[çc][õo]es perdidas(.*)|(.*)rela[çc][õo]es perdidas(.*)",
        [
            "Reconstruir relações perdidas é emocionante! Você prefere quando há perdão ou quando o passado impede a reconciliação?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)prop[oó]sito da vida(.*)|(.*)prop[oó]sito(.*)",
        [
            "Questionar o propósito da vida é uma jornada profunda! Traz um peso lindo à narrativa literária. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)mortalidade(.*)",
        [
            "Lidar com a mortalidade é tão visceral! Faz a gente refletir sobre cada momento. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)processo solit[aá]rio(.*)|(.*)solit[aá]rio(.*)",
        [
            "Um processo solitário de autocompreensão é introspectivo e forte! Uma viagem única ao eu. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)conex[õo]es com outros(.*)|(.*)conex[õo]es(.*)",
        [
            "Autocompreensão através de conexões é tão rica! Os outros como espelhos da alma. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)resili[eê]ncia(.*)",
        [
            "Resiliência frente à marginalização é inspiradora! Mostra a força do espírito humano. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)injusti[çc]as sociais(.*)|(.*)injusti[çc]as(.*)",
        [
            "Explorar injustiças sociais dá voz aos silenciados! Um tema poderoso na narrativa literária. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)resiste [aà]s normas(.*)|(.*)normas(.*)",
        [
            "Resistir às normas é uma rebeldia com propósito! Faz a narrativa vibrar com coragem. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)encontra um meio-termo(.*)|(.*)meio-termo(.*)",
        [
            "Encontrar um meio-termo é tão humano e complexo! Equilíbrio em meio ao caos. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)libertadora(.*)",
        [
            "Uma verdade libertadora é como um raio de luz! Transforma a narrativa em algo especial. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)dolorosa(.*)",
        [
            "Uma verdade dolorosa corta fundo! Dá uma intensidade única à história. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)traz paz(.*)|(.*)paz(.*)",
        [
            "Aceitar a incerteza e encontrar paz é sereno e profundo! Um desfecho que acalma a alma. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)vazio inquietante(.*)|(.*)inquietante(.*)",
        [
            "Um vazio inquietante deixa a gente pensando por dias! A narrativa literária brilha assim. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)reden[çc][aã]o(.*)",
        [
            "Arrependimentos que levam à redenção são transformadores! Uma jornada de cura no drama. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)permanecem como li[çc][õo]es(.*)|(.*)li[çc][õo]es(.*)",
        [
            "Arrependimentos como lições são tão reais! Ensinam sem precisar de finais felizes. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)perd[aã]o(.*)",
        [
            "Perdão em relações perdidas é emocionante! Traz esperança à narrativa. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)passado impede a reconcilia[çc][aã]o(.*)|(.*)reconcilia[çc][aã]o(.*)",
        [
            "Quando o passado impede a reconciliação, o peso é real! Um drama que marca. E qual outro gênero você gosta?"
        ]
    ],
    # Nível 1: Tema principal - Ação
    [
        r"(.*)a[cç][aã]o(.*)",
        [
            "Ação é pura adrenalina do começo ao fim! Você prefere histórias com perseguições alucinantes ou combates épicos?"
        ]
    ],

    # Nível 2: Subtemas de Ação
    [
        r"(.*)persegui[çc][õo]es alucinantes(.*)|(.*)persegui[çc][õo]es(.*)",
        [
            "Perseguições alucinantes aceleram o coração! Você gosta mais de corridas contra o tempo ou de fugas impossíveis?"
        ]
    ],
    [
        r"(.*)combates [ée]picos(.*)|(.*)combates(.*)",
        [
            "Combates épicos são cheios de energia! Você prefere batalhas em equipe ou duelos mano a mano?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)corridas contra o tempo(.*)|(.*)contra o tempo(.*)",
        [
            "Corridas contra o tempo são tensas! Você gosta mais quando é para impedir uma catástrofe ou para salvar alguém?"
        ]
    ],
    [
        r"(.*)fugas imposs[ií]veis(.*)|(.*)fugas(.*)",
        [
            "Fugas impossíveis são de tirar o fôlego! Você prefere quando envolvem improvisação genial ou planejamento meticuloso?"
        ]
    ],
    [
        r"(.*)batalhas em equipe(.*)|(.*)equipe(.*)",
        [
            "Batalhas em equipe mostram união e estratégia! Você gosta mais quando há confiança total entre os membros ou quando há tensões internas?"
        ]
    ],
    [
        r"(.*)duelos mano a mano(.*)|(.*)mano a mano(.*)",
        [
            "Duelos mano a mano são intensos! Você prefere quando são movidos por vingança ou por honra?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)impedir uma cat[aá]strofe(.*)|(.*)cat[aá]strofe(.*)",
        [
            "Impedir uma catástrofe é adrenalina pura! Você acha mais emocionante quando é uma ameaça global ou um plano de um vilão?"
        ]
    ],
    [
        r"(.*)salvar algu[eé]m(.*)|(.*)salvar(.*)",
        [
            "Salvar alguém contra o tempo é heroico! Você prefere quando é uma missão pessoal ou quando envolve um estranho?"
        ]
    ],
    [
        r"(.*)improvisa[çc][aã]o genial(.*)|(.*)improvisa[çc][aã]o(.*)",
        [
            "Improvisação genial é sempre surpreendente! Você gosta mais quando usa o ambiente ou quando depende de pura astúcia?"
        ]
    ],
    [
        r"(.*)planejamento meticuloso(.*)|(.*)meticuloso(.*)",
        [
            "Planejamento meticuloso torna a fuga perfeita! Você prefere quando tudo sai conforme o plano ou quando algo dá errado?"
        ]
    ],
    [
        r"(.*)confian[çc]a total(.*)|(.*)confian[çc]a(.*)",
        [
            "Confiança total na equipe é inspiradora! Você gosta mais quando é uma unidade militar ou um grupo improvisado?"
        ]
    ],
    [
        r"(.*)tens[õo]es internas(.*)|(.*)tens[õo]es(.*)",
        [
            "Tensões internas na equipe adicionam fogo à ação! Você prefere quando vêm de traições ou de egos conflitantes?"
        ]
    ],
    [
        r"(.*)vingan[çc]a(.*)",
        [
            "Duelos por vingança são carregados de emoção! Você gosta mais quando o motivo é uma perda pessoal ou uma injustiça antiga?"
        ]
    ],
    [
        r"(.*)honra(.*)",
        [
            "Duelos por honra são cheios de dignidade! Você prefere quando seguem um código ou quando são impulsivos?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)amea[çc]a global(.*)|(.*)global(.*)",
        [
            "Uma ameaça global eleva a ação a outro nível! Salvar o mundo é sempre eletrizante. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)plano de um vil[aã]o(.*)|(.*)vil[aã]o(.*)",
        [
            "Enfrentar o plano de um vilão é um jogo de gato e rato! A ação brilha nesses confrontos. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)miss[aã]o pessoal(.*)|(.*)pessoal(.*)",
        [
            "Uma missão pessoal para salvar alguém é cheia de coração! A ação ganha alma assim. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)envolve um estranho(.*)|(.*)estranho(.*)",
        [
            "Salvar um estranho traz heroísmo puro! Ação com um toque de humanidade. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)usa o ambiente(.*)|(.*)ambiente(.*)",
        [
            "Usar o ambiente na improvisação é genial! Transforma a ação em algo criativo e vibrante. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)pura ast[uú]cia(.*)|(.*)ast[uú]cia(.*)",
        [
            "Pura astúcia em uma fuga é brilhante! A mente como arma na ação. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tudo sai conforme o plano(.*)|(.*)conforme o plano(.*)",
        [
            "Quando tudo sai conforme o plano, a ação é satisfatória! Uma coreografia perfeita. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)algo d[aá] errado(.*)|(.*)d[aá] errado(.*)",
        [
            "Algo dando errado mantém a ação imprevisível! A tensão só aumenta. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)unidade militar(.*)|(.*)militar(.*)",
        [
            "Uma unidade militar em ação é disciplinada e intensa! A confiança leva a cenas épicas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)grupo improvisado(.*)|(.*)improvisado(.*)",
        [
            "Um grupo improvisado traz caos e união! A ação ganha vida com essa dinâmica. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)trai[çc][õo]es(.*)",
        [
            "Tensões por traições na equipe são explosivas! A ação vira um campo minado. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)egos conflitantes(.*)|(.*)conflitantes(.*)",
        [
            "Egos conflitantes na equipe são um show à parte! A ação ganha camadas com esses choques. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)perda pessoal(.*)|(.*)perda(.*)",
        [
            "Vingança por uma perda pessoal é visceral! A ação pulsa com essa motivação. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)injusti[çc]a antiga(.*)|(.*)injusti[çc]a(.*)",
        [
            "Vingança por uma injustiça antiga é poderosa! A ação ganha peso histórico. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)seguem um c[oó]digo(.*)|(.*)c[oó]digo(.*)",
        [
            "Duelos por honra com um código são elegantes! A ação brilha com essa disciplina. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)impulsivos?(.*)",
        [
            "Duelos impulsivos por honra são explosivos! A ação crua e cheia de paixão. E qual outro gênero você gosta?"
        ]
    ],
    # Nível 1: Tema principal - Humor/Comédia
    [
        r"(.*)humor(.*)|(.*)com[eé]dia(.*)",
        [
            "Humor e comédia são perfeitos pra alegrar o dia! Você prefere histórias com situações absurdas ou com personagens excêntricos?"
        ]
    ],

    # Nível 2: Subtemas de Humor/Comédia
    [
        r"(.*)situa[çc][õo]es absurdas(.*)|(.*)absurdas(.*)|(.*)absurdo(.*)",
        [
            "Situações absurdas garantem risadas sem fim! Você gosta mais de mal-entendidos hilários ou de eventos completamente fora da curva?"
        ]
    ],
    [
        r"(.*)personagens exc[eê]ntricos(.*)|(.*)exc[eê]ntricos(.*)|(.*)peculiares(.*)",
        [
            "Personagens excêntricos roubam a cena! Você prefere quando são desajeitados adoráveis ou mestres do sarcasmo?"
        ]
    ],

    # Nível 3: Detalhando os Subtemas
    [
        r"(.*)mal-entendidos hil[aá]rios(.*)|(.*)mal-entendidos(.*)|(.*)confus[õo]es(.*)",
        [
            "Mal-entendidos hilários são um prato cheio! Você gosta mais quando levam a trocas de identidade ou a planos que dão errado?"
        ]
    ],
    [
        r"(.*)eventos completamente fora da curva(.*)|(.*)fora da curva(.*)|(.*)loucos(.*)",
        [
            "Eventos fora da curva são pura comédia! Você prefere quando viram caos organizado ou quando são surpresas imprevisíveis?"
        ]
    ],
    [
        r"(.*)desajeitados ador[aá]veis(.*)|(.*)desajeitados(.*)|(.*)ador[aá]veis(.*)",
        [
            "Desajeitados adoráveis conquistam qualquer um! Você gosta mais quando se metem em encrencas ou quando tentam impressionar e falham?"
        ]
    ],
    [
        r"(.*)mestres do sarcasmo(.*)|(.*)sarcasmo(.*)|(.*)ironia(.*)",
        [
            "Mestres do sarcasmo são geniais! Você prefere quando usam tiradas rápidas ou quando criam rivalidades cômicas?"
        ]
    ],

    # Nível 4: Detalhando as Respostas do Nível 3
    [
        r"(.*)trocas de identidade(.*)|(.*)identidade(.*)",
        [
            "Trocas de identidade são risadas garantidas! Você acha mais divertido quando são acidentais ou quando são parte de um esquema?"
        ]
    ],
    [
        r"(.*)planos que d[aã]o errado(.*)|(.*)d[aã]o errado(.*)|(.*)planos errados(.*)",
        [
            "Planos que dão errado são o coração da comédia! Você prefere quando tudo desmorona rápido ou quando vira uma bola de neve?"
        ]
    ],
    [
        r"(.*)caos organizado(.*)|(.*)caos(.*)",
        [
            "Caos organizado é uma arte cômica! Você gosta mais quando parece que vai colapsar ou quando milagrosamente dá certo?"
        ]
    ],
    [
        r"(.*)surpresas imprevis[ií]veis(.*)|(.*)imprevis[ií]veis(.*)|(.*)surpresas(.*)",
        [
            "Surpresas imprevisíveis mantêm o riso solto! Você prefere quando são reviravoltas malucas ou quando vêm de coincidências absurdas?"
        ]
    ],
    [
        r"(.*)metem em encrencas(.*)|(.*)encrencas(.*)",
        [
            "Se meter em encrencas é a cara dos desajeitados! Você gosta mais quando é por pura trapalhada ou quando tentam consertar o erro?"
        ]
    ],
    [
        r"(.*)tentam impressionar e falham(.*)|(.*)impressionar(.*)|(.*)falham(.*)",
        [
            "Tentar impressionar e falhar é hilário! Você prefere quando é em público ou quando é pra conquistar alguém?"
        ]
    ],
    [
        r"(.*)tiradas r[aá]pidas(.*)|(.*)tiradas(.*)",
        [
            "Tiradas rápidas são o ápice do sarcasmo! Você gosta mais quando são improvisadas ou quando atingem o ponto fraco de alguém?"
        ]
    ],
    [
        r"(.*)rivalidades c[oô]micas(.*)|(.*)rivalidades(.*)",
        [
            "Rivalidades cômicas são puro entretenimento! Você prefere quando são amigáveis ou quando têm uma pitada de vingança?"
        ]
    ],

    # Nível 5: Finalizando com Comentários e Pergunta sobre Outro Gênero
    [
        r"(.*)acidentais(.*)",
        [
            "Trocas de identidade acidentais são uma confusão deliciosa! A comédia floresce no inesperado. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)parte de um esquema(.*)|(.*)esquema(.*)",
        [
            "Trocas de identidade como esquema são um show de risadas! A comédia brilha na ousadia. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)desmorona r[aá]pido(.*)|(.*)desmorona(.*)",
        [
            "Planos que desmoronam rápido são hilários! A comédia ganha vida na correria. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)bola de neve(.*)",
        [
            "Um plano virando bola de neve é comédia pura! Tudo cresce e explode em riso. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)parece que vai colapsar(.*)|(.*)colapsar(.*)",
        [
            "Caos que parece colapsar é tensão cômica no auge! A comédia vive desses momentos. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)milagrosamente d[aá] certo(.*)|(.*)d[aá] certo(.*)",
        [
            "Caos que milagrosamente dá certo é genial! A comédia surpreende com esses finais. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)reviravoltas malucas(.*)|(.*)malucas(.*)",
        [
            "Reviravoltas malucas são o tempero da comédia! Sempre arrancam gargalhadas. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)coincid[eê]ncias absurdas(.*)|(.*)coincid[eê]ncias(.*)",
        [
            "Coincidências absurdas são ouro no humor! A comédia brilha com esses acasos. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)pura trapalhada(.*)|(.*)trapalhada(.*)",
        [
            "Encrencas por pura trapalhada são adoráveis! O humor vive dessas gafes. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)tentam consertar o erro(.*)|(.*)consertar(.*)|(.*)erro(.*)",
        [
            "Tentar consertar o erro e piorar tudo é comédia clássica! Sempre diverte. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)em p[uú]blico(.*)|(.*)p[uú]blico(.*)",
        [
            "Falhar em público é constrangedor e hilário! A comédia ganha com essas situações. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)conquistar algu[eé]m(.*)|(.*)conquistar(.*)",
        [
            "Falhar tentando conquistar alguém é tão humano! O humor brilha nesses tropeços. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)improvisadas(.*)",
        [
            "Tiradas improvisadas são puro talento cômico! O sarcasmo ganha vida na espontaneidade. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)atingem o ponto fraco(.*)|(.*)ponto fraco(.*)",
        [
            "Tiradas que atingem o ponto fraco são afiadas! A comédia corta fundo com inteligência. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)amig[aá]veis(.*)",
        [
            "Rivalidades amigáveis são leves e divertidas! O humor floresce nessa troca. E qual outro gênero você gosta?"
        ]
    ],
    [
        r"(.*)pitada de vingan[çc]a(.*)|(.*)vingan[çc]a(.*)",
        [
            "Rivalidades com uma pitada de vingança são hilárias! O humor ganha um toque picante. E qual outro gênero você gosta?"
        ]
    ],


]
