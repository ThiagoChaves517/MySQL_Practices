from mysql.connector import MySQLConnection, Error
from config import read_config
from faker import Faker
from faker.providers import DynamicProvider
import inserts_livraria as insertLiv
import random
from datetime import date, timedelta

book_names_provider = DynamicProvider(
     provider_name="book_names",
     elements=[
        "Diario de Um Banana"
        "Caminhos Perdidos",
        "Segredos do Horizonte",
        "Jornada Alem do Mapa",
        "O Despertar da Expedicao",
        "Em Busca do Tesouro Perdido",
        "Trilhas do Desconhecido",
        "O Misterio das Ruínas Antigas",
        "Exploradores da Terra Proibida",
        "Rumo ao Desconhecido",
        "O Legado do Explorador",
        "Na Rota do Desafio",
        "Alem da Fronteira",
        "O Enigma do Vale Oculto",
        "Aventuras do Horizonte",
        "Em Busca da Cidade Perdida",
        "O Tesouro das Profundezas",
        "O Desafio das Montanhas",
        "Pistas do Passado",
        "Na Trilha da Coragem",
        "O Segredo da Ilha Misteriosa",
        "Expedição ao Desconhecido",
        "O Misterio do Mapa Antigo",
        "O Legado do Navegador",
        "Fronteiras do Infinito",
        "Travessia ao Desconhecido",
        "Os Segredos do Navio Fantasma",
        "O Vale das Maravilhas",
        "O Enigma do Templo Esquecido",
        "Viagem ao Coracao da Selva",
        "O Desafio do Explorador Solitario",
        "Caminho para a Aventura",
        "A Busca pelo Mundo Desconhecido",
        "As Ruinas do Tempo",
        "O Despertar do Explorador",
        "Aventura nas Estrelas",
        "Trilhas do Destino",
        "O Segredo da Passagem Secreta",
        "O Legado dos Desbravadores",
        "Desafios do Desconhecido",
        "Coracao de Aventureiro",
        "A Trilha da Sobrevivencia",
        "O Misterio da Floresta Encantada",
        "Caminhos da Descoberta",
        "Os Tesouros do Deserto",
        "Jornada ao Mundo Perdido",
        "O Enigma da Pedra Sagrada",
        "Explorando Novos Horizontes",
        "Aventuras na Terra Selvagem",
        "A Busca do Lendario",
        "Em Busca das Lendas Perdidas",
        "Destinos Entrelacados",
        "Promessas do Coracao",
        "Passos do Amor",
        "Segredos do Crepusculo",
        "Entre Risos e Suspiros",
        "Laços Inquebraveis",
        "Doce Obsessao",
        "Ecos do Romance",
        "Labirinto de Emocoes",
        "Estrelas e Paixao",
        "Para Sempre ao Teu Lado",
        "Melodias do Coracao",
        "Encantos do Destino",
        "Coracoes Entrelacados",
        "No Ritmo do Amor",
        "Sombras do Desejo",
        "Amores Desencontrados",
        "Florescer do Sentimento",
        "Promessas de Lua Cheia",
        "Danca dos Sentidos",
        "Abracos Sob o Luar",
        "O Refugio do Amor",
        "Amanhecer da Paixao",
        "Encontro das Almas",
        "Nos Trilhos do Amor",
        "Harmonia do Romance",
        "Estações do Coracao",
        "Doce Encontro",
        "Silhuetas do Amor",
        "Vento e Carinho",
        "Meu Eterno Amor",
        "Beijos a Meia-Noite",
        "Cumplicidade do Coracao",
        "Paginas de Afeto",
        "A Chama da Paixao",
        "Jardim dos Sentimentos",
        "Nos Braços do Destino",
        "Sonhos Compartilhados",
        "Lagrimas de Felicidade",
        "Na Rota do Romance",
        "O Suspiro do Amor",
        "O Sussurro do Coracao",
        "Segredos do Abraco",
        "A Promessa de um Beijo",
        "Raizes do Sentimento",
        "Estrelas Cadentes",
        "Lacos do Passado",
        "Nas Ondas da Paixao",
        "Cantos do Amor",
        "O Encanto da Conexao",
        "Alem do Horizonte Estelar", 
        "Cosmos Desconhecido", 
        "Rumo a Singularidade", 
        "Ecos do Universo", 
        "Mundos Paralelos", 
        "Vanguarda do Amanha", 
        "Estradas da Galaxia", 
        "Chamas do Cosmos", 
        "Alem do Limiar Espacial", 
        "Maquinas da Consciencia", 
        "Abismo Temporal", 
        "Ondas do Futuro", 
        "Aurora do Além", 
        "Cidades Astrais", 
        "Trilhas da Exploracao", 
        "Ecos do Vazio", 
        "Entre as Estrelas", 
        "Horizontes Inexplorados", 
        "Amanhecer Cibernetico", 
        "Universos Convergentes", 
        "A Colheita das Estrelas", 
        "Alem do Nexus", 
        "Nevoa Cósmica", 
        "Portais do Infinito", 
        "Estrada para o Cosmos", 
        "Arcanjo do Espaco", 
        "Anjos Mecanicos", 
        "Rumo ao Eden Cibernetico", 
        "Ecos do Infinito", 
        "Fronteiras do Tempo", 
        "Viajantes Estelares", 
        "Estradas da Infinidade", 
        "Amanhecer Mecanico", 
        "A Mente da Maquina", 
        "Alem da Fronteira Quantica", 
        "Caminhos do Universo", 
        "No Vortice do Tempo", 
        "Trilhas do Espaço-Tempo", 
        "Cidade das Estrelas", 
        "Oraculo Cibernetico", 
        "Horizontes do Eter", 
        "Destino Alem das Estrelas", 
        "Universo Cosmico", 
        "Estradas do Hiperespaço", 
        "Alem do Cosmo Conhecido", 
        "Rumo ao Infinito", 
        "Espiritos Ciberneticos", 
        "Codigos do Cosmos", 
        "Legado Estelar", 
        "Cosmos Sintetico",
        "Reinos Encantados",
        "Alem do Veu Magico",
        "A Dança dos Dragoes",
        "A Floresta dos Segredos",
        "Estrelas Cadentes do Reino",
        "O Portal dos Feitiços",
        "Luzes da Magia Antiga",
        "A Lenda do Guardiao",
        "No Limiar da Fantasia",
        "Sombras da Magia",
        "O Legado dos Elfos",
        "As Fronteiras do Reino",
        "Encantos e Misterios",
        "O Chamado da Espada Magica",
        "Jardins da Ilusao",
        "O Despertar do Poder",
        "A Torre dos Magos",
        "Segredos da Terra dos Gigantes",
        "O Tesouro do Dragao Dourado",
        "Entre Sombras e Encantos",
        "O Feitiço da Lua",
        "O Reino Perdido de Avalon",
        "As Profundezas do Reino Elfico",
        "O Misterio do Circulo de Pedras",
        "As Cronicas de Eloria",
        "A Magia das Estrelas",
        "Os Guardioes da Aurora",
        "A Estrada para Faeryland",
        "Encantamentos da Lua Cheia",
        "O Herdeiro do Reino das Sombras",
        "Dragoes Alem da Montanha",
        "A Profecia dos Quatro Reinos",
        "O Legado de Numenor",
        "Portais do Mundo Magico",
        "O Reino dos Sonhos",
        "A Maldição da Escuridao",
        "As Trilhas do Destino Magico",
        "Na Sombra do Castelo Proibido",
        "A Jornada do Heroi Encantado",
        "O Labirinto dos Espiritos",
        "A Guerra dos Reinos",
        "Entre os Ventos Encantados",
        "O Resgate da Fada Perdida",
        "O Misterio do Orbe de Cristal",
        "No Rastro das Fadas",
        "A Saga do Herdeiro do Fogo",
        "A Profecia dos Artefatos Magicos",
        "Reis e Feiticeiros",
        "O Poder do Elixir Secreto",
        "Cronicas do Reino Encantado",
        "O Eco dos Pesadelos",
        "As Sombras do Medo",
        "A Porta do Abismo",
        "A Escuridão Interior",
        "Os Segredos do Pavor",
        "No Limite da Insanidade",
        "A Maldição do Antigo Cemiterio",
        "Alem da Noite Profunda",
        "A Sombra do Desespero",
        "O Despertar dos Horrores",
        "O Labirinto do Terror",
        "Espiritos na Escuridao",
        "As Profundezas do Desespero",
        "Pesadelos Recorrentes",
        "A Marca da Loucura",
        "No Limiar da Loucura",
        "A Casa das Almas Perdidas",
        "O Canto dos Demonios",
        "Sombras do Alem",
        "As Ruinas do Medo",
        "Entre Asas e Maldicoes",
        "Labirinto do Medo",
        "Na Sombra da Aflicao",
        "A Maldicao da Noite Infinita",
        "O Despertar das Trevas",
        "O Vale dos Esquecidos",
        "Sob o Dominio do Horror",
        "O Legado da Escuridao",
        "O Despertar do Caos",
        "Ruinas do Desespero",
        "O Fim da Inocencia",
        "Na Trilha do Desespero",
        "A Beira do Abismo",
        "O Refugio do Pavor",
        "Pesadelos Infinitos",
        "Labirinto dos Pesadelos",
        "O Ultimo Suspiro",
        "Entre Sombras e Espiritos",
        "As Profundezas do Pesadelo",
        "O Legado dos Condenados",
        "Sussurros na Escuridao",
        "Sob o Olhar do Medo",
        "A Maldicao da Noite Eterna",
        "A Marca do Horror",
        "O Canto das Almas Malditas",
        "Nas Profundezas do Medo",
        "Espiritos da Escuridao",
        "Alem do Limiar do Horror",
        "Maldição nas Profundezas",
        "Na Escuridao da Noite Eterna",
        "Enigmas do Passado",
        "Segredos Obscuros",
        "O Misterio da Mansão Abandonada",
        "Sombras da Intriga",
        "A Verdade Escondida",
        "O Enigma do Relogio Parado",
        "Jogo de Misterios",
        "Nas Sombras do Crime",
        "O Segredo do Lago Sombrio",
        "Rastros da Incognita",
        "O Caso do Quadro Desaparecido",
        "A Pista Perdida",
        "O Misterio do Manuscrito Antigo",
        "Segredos Enterrados",
        "A Sombra do Detetive",
        "O Enigma do Veu Negro",
        "Intrigas da Noite",
        "A Chave do Enigma",
        "O Desaparecimento de Emily Green",
        "O Misterio da Casa da Colina",
        "Rastros na Neblina",
        "Enigma no Beco Escuro",
        "O Segredo da Carta Anonima",
        "As Sombras da Verdade",
        "O Enigma do Espelho Quebrado",
        "O Misterio do Bilhete Criptografado",
        "A Luz da Desconfianca",
        "Entre Fios do Misterio",
        "O Desaparecimento de Mr. Johnson",
        "Rastros na Areia",
        "O Enigma da Reliquia Perdida",
        "A Passagem Secreta",
        "Misterio na Vila Abandonada",
        "O Segredo do Cofre Trancado",
        "O Misterio do Dispositivo Desconhecido",
        "Intrigas e Segredos",
        "A Carta Enigmatica",
        "Rastros do Passado Oculto",
        "O Desaparecimento de Sarah Brown",
        "Entre Sombras e Segredos",
        "O Enigma do Codigo Perdido",
        "Misterios da Lua Cheia",
        "O Segredo do Velho Farol",
        "A Sala Esquecida",
        "Desvendando a Conspiracao",
        "O Mistério do Livro Proibido",
        "Enigmas da Cidade Esquecida",
        "Rastros na Floresta",
        "O Segredo do Colar Desaparecido",
        "O Enigma do Mapa Antigo",
        "Nomes para Livros de Humor",
        "Risadas Sem Fim",
        "Sorrisos em Pagina",
        "Piadas e Proezas",
        "O Lado Engraçado da Vida",
        "Comedias do Cotidiano",
        "Zombarias e Zueiras",
        "Trocadilhos e Trapalhadas",
        "Rindo a Cada Capitulo",
        "Um Livro Pra Rir",
        "Humor de Ponta a Ponta",
        "Risadas em Sequencia",
        "Parodias e Palhacadas",
        "Rir e o Melhor Remedio",
        "Situacoes Comicas",
        "Piadas de Todas as Cores",
        "O Mundo e uma Comedia",
        "Engraçadices do Dia a Dia",
        "Paginas Divertidas",
        "Rindo ate a Ultima Pagina",
        "Ironias e Incomodos",
        "Palhaçadas em Tinta",
        "Comedia e Confusao",
        "Anedotas e Aventuras",
        "Rindo Alto com Historias",
        "Humor Sutil",
        "Trapalhadas Cotidianas",
        "Zombarias e Risadas",
        "Comedias da Vida Real",
        "Risadas Sem Limites",
        "Humor e Bons Momentos",
        "Sorrisos em Cada Capitulo",
        "A Graça Esta no Livro",
        "Risos Atemporais",
        "Doses Diarias de Humor",
        "Piadas e Ironias",
        "Rir Sem Parar",
        "Comédias e Caos",
        "Rindo do Inusitado",
        "Humor em Cada Paragrafo",
        "Engraçadices e Traquinagens",
        "Alegria em Paginas",
        "Escritos Comicos",
        "Divertimento e Diabruras",
        "Risadas no Papel",
        "Palavras Engraçadas",
        "Loucuras e Comedias",
        "Momentos Engraçados",
        "Situações Risonhas",
        "Comicos do Dia a Dia",
        "Humor em Toda a Extensao"
    ],
)
languages_provider = DynamicProvider(
     provider_name="languages",
     elements=["Ingles", "Portugues", "Espanhol", "Alemao", "Frances", "Japones", "Chines", "Malgaxe", "Holandes", "Braille"],
)

fake = Faker()
fake.add_provider(book_names_provider)
fake.add_provider(languages_provider)

def random_date(start_year, start_month, start_day, end_year, end_month, end_day):
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + timedelta(days=rand_days)
    return random_date

def connect(config):
    """ Connect to MySQL database """
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**config)

        ###
        # Código para gerar ISBNs de forma rápida e única.
        potential_ISBNs = [fake.isbn13() for _ in range(2000)]
        unique_ISBNs = list(set(potential_ISBNs))

        while(len(unique_ISBNs) < 1000):
            potential_ISBNs = [fake.isbn13() for _ in range(2000)]
            unique_ISBNs = set(potential_ISBNs)
        ###

        if conn.is_connected():
            print('Connection is established.')
            with conn.cursor() as cursor:
                #Inserção dos dados meu BD no MySQL:
                for i in range(0, 100): # 100 Autores
                    insertLiv.insert_author(cursor, fake.name(), random_date(1300, 1, 1, 2030, 12, 31), fake.country(), fake.paragraph(nb_sentences=5))

                print('The authors were just inserted...')

                for i in range(0, 400): # 400 Livros
                    insertLiv.insert_book(cursor, fake.book_names(), fake.languages(), random.randint(1400, 2024))
                
                print('The books were just inserted...')

                j = 1
                counter = 0
                for i in range(0, 400): # 400 Livros e seus autores
                    if(counter >= 3 and j < 100):
                        j += 1
                        counter = 0

                    counter += 1
                    insertLiv.insert_in_the_write_table(cursor, i+1, j)
                    

                print('The books and their authors are now connected...')

                for i in range(0, 50): # 50 Editoras
                    insertLiv.insert_editor(cursor, fake.name(), fake.phone_number(), fake.address().replace('\n', " - "))

                print('The editors were just inserted...')

                for i in range(0, 1000): # 1000 Edições
                    insertLiv.insert_edition(cursor, unique_ISBNs[i], random.uniform(1000.00, 0.00), random.randint(1400, 2024), random.randint(1, 10000), random.randint(1, 400), random.randint(1, 50), random.randint(1, 10000))

                print('The editions were just inserted...')

            conn.commit()

        else:
            print('Connection is failed.')

    except Error as error:
        print(error)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection is closed.')


if __name__ == '__main__':
    config = read_config()
    connect(config)