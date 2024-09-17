import re
import csv
from imdb import Cinemagoer


ia = Cinemagoer()

def parse_data_movie(movie_id):
    movie = ia.get_movie(movie_id, info='main')

    print(f'Extraindo infos de {movie}')

    # infos que sempre (?) existirão
    info = {
        'tipo': movie['kind'],
        'titulo': movie['title'],
        'ano': movie['year'],
        'nota': movie['rating'],
        'genero_principal': movie['genres'][0],
        'duracao': movie['runtimes'][0],
        'votos': movie['votes']
    }

    # um filme pode sair do top 250 e perder essa info
    try:
        info['pos_ranking'] = movie['top 250 rank']
    except KeyError:
        info['pos_ranking'] = ''

    # nem todo filme tem as 3 informações de orçamento
    try:
        info['orcamento'] = re.sub(r'[^\d+]', '', movie['box office']['Budget'])
    except KeyError:
        info['orcamento'] = ''

    try:
        info['faturamento_1a_sem_US'] = movie['box office']['Opening Weekend United States']
    except KeyError:
        info['faturamento_1a_sem_US'] = ''
    try:

        info['faturamento_total'] = movie['box office']['Cumulative Worldwide Gross']
    except KeyError:
        info['faturamento_total'] = ''
    
    return info

if __name__ == '__main__':
    file = 'top250moviesID.txt'

    with open(file, 'r') as f:
        data = f.readlines()

    data = [d[:-1] for d in data]

    movies = list()
    for d in data:
        movies.append(parse_data_movie(d))

    with open('foo.csv', 'w') as f:
        writer = csv.writer(f, delimiter=";", quotechar='"')

        cabecalho = movies[0].keys()
        writer.writerow(cabecalho)

        for movie in movies:
            linha = movie.values()
            writer.writerow(linha)
