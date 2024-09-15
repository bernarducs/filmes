from imdb import Cinemagoer

ia = Cinemagoer()

def parse_data_movie(movie_id):
    movie = ia.get_movie(movie_id, info='main')
    return {
        'tipo': movie['kind'],
        'titulo': movie['title'],
        'ano': movie['year'],
        'generos': movie['genres'],
        'duracao': movie['runtimes'],
        'pos_ranking': movie['top 250 rank'],
        'votos': movie['votes'],
        'orcamento': movie['box office']['Budget'],
        'faturamento_1a_sem_US': movie['box office']['Opening Weekend United States'],
        'faturamento_total': movie['box office']['Cumulative Worldwide Gross'],
    }
