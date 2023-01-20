from fastapi import FastAPI
import string
import pandas as pd


class diccionarios:   
    def dict_titles(self, list_plataform):
        lis_palabra= []
        flat_list = []
        numkeywords = 0
        dkeywords = dict()
        words = list_plataform
        new_words = []
        for word in words:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter,"")   
            new_words.append(word)
        for i in new_words:
            i = str(i)
            a= i.split()
            lis_palabra.append(a)
        for item in lis_palabra:
            flat_list += item
            for palabra in flat_list:
                numkeywords += 1
                dkeywords[palabra] = dkeywords.get(palabra, 0) + 1
        return dkeywords

amazon = pd.read_csv("https://raw.githubusercontent.com/valdez101/Primer_proyecto/master/amazon_prime_titles-score_Arreglado.csv")
disney = pd.read_csv("https://raw.githubusercontent.com/valdez101/Primer_proyecto/master/disney_plus_titles-score_Arreglado.csv")
hulu = pd.read_csv("https://raw.githubusercontent.com/valdez101/Primer_proyecto/master/hulu_titles-score%20(2)_Arreglado.csv")
netflix = pd.read_csv("https://raw.githubusercontent.com/valdez101/Primer_proyecto/master/netflix_titles-score_Arreglado.csv")

amazon['title']= amazon['title'].str.lower()
disney['title']= disney['title'].str.lower()
hulu['title']= hulu['title'].str.lower()
netflix['title']= netflix['title'].str.lower()

    
list_amazon = list(amazon['title'])
list_disney = list(disney['title'])
list_hulu = list(hulu['title'])
list_netflix = list(netflix['title'])

d = diccionarios()

dict_amazon = d.dict_titles([list_amazon])
dict_disney = d.dict_titles([list_disney])
dict_hulu = d.dict_titles([list_hulu])
dict_netflix = d.dict_titles([list_netflix])

app= FastAPI(title= 'most watched and ranked movies by platform', 
             description= 'Prueba de resultados en distintas plataformas, segun querys del TL', 
             version='1.0.1')

@app.get('/')
async def index():
    return 'Primer proyecto individual - JValdez'

@app.get('/about')
async def about():
    return 'Primer proyecto individual de DS JValdez'


@app.get('/get_word_count/{plataforma}/{keywords}') # pregunta 1
async def get_word_count(plataforma, keywords):   
    if (plataforma == 'amazon'):
        keywords = keywords.lower()
        for i in dict_amazon.keys():
            if i == keywords:
                cantidad=dict_amazon[i]
                return ('amazon', cantidad)
    elif (plataforma == 'disney'):
        keywords = keywords.lower()
        for i in dict_disney.keys():
            if i == keywords:
                cantidad=dict_disney[i]
                return ('disney', cantidad)
    elif (plataforma == 'hulu'):
        keywords = keywords.lower()
        for i in dict_hulu.keys():
            if i == keywords:
                cantidad=dict_hulu[i]
                return ('hulu', cantidad)
    elif (plataforma == 'netflix'):
        keywords = keywords.lower()
        for i in dict_netflix.keys():
            if i == keywords:
                cantidad=dict_netflix[i]
                return ('netflix', cantidad)
    else:
        return 'La plataforma ingresada fue incorrecta, revisar la consulta'
    
@app.get('/get_score_count/{plataforma}/{score}/{year}') # pregunta 2
async def get_score_count(plataforma, score, year):
    if (plataforma == 'amazon'):
        data_amazon = amazon[['score', 'release_year']]
        score = int(score)
        year = int(year)
        respst = data_amazon[(data_amazon['score'] > score) & (data_amazon['release_year'] == year)]
        cantidad = int(len(respst))
        return ('amazon', cantidad)
    elif (plataforma == 'disney'):
        data_disney = disney[['score', 'release_year']]
        score = int(score)
        year = int(year)
        respst = data_disney[(data_disney['score'] > score) & (data_disney['release_year'] == year)]
        cantidad = int(len(respst))
        return ('disney', cantidad)
    elif (plataforma == 'hulu'):
        data_hulu = hulu[['score', 'release_year']]
        score = int(score)
        year = int(year)
        respst = data_hulu[(data_hulu['score'] > score) & (data_hulu['release_year'] == year)]
        cantidad = int(len(respst))
        return ('hulu', cantidad)
    elif (plataforma == 'netflix'):
        data_netflix = netflix[['score', 'release_year']]
        score = int(score)
        year = int(year)
        respst = data_netflix[(data_netflix['score'] > score) & (data_netflix['release_year'] == year)]
        cantidad = int(len(respst))
        return ('netflix', cantidad)
    else:
        return 'La plataforma ingresada fue incorrecta'
    
@app.get('/get_second_score/{plataform}') # pregunta 3
async def get_second_score(plataform):
    if (plataform == 'amazon'):
        score_amazon = amazon[['title', 'score']]
        score_2 = score_amazon.sort_values(['score', 'title'], ascending=[False, True])
        title = score_2.iloc[1][0]
        score = int(score_2.iloc[1][1])
        return (title, score)
    elif (plataform == 'disney'):
        score_disney = disney[['title', 'score']]
        score_2 = score_disney.sort_values(['score', 'title'], ascending=[False, True])
        title = score_2.iloc[1][0]
        score = int(score_2.iloc[1][1])
        return (title, score)
    elif (plataform == 'hulu'):
        score_hulu = hulu[['title', 'score']]
        score_2 = score_hulu.sort_values(['score', 'title'], ascending=[False, True])
        title = score_2.iloc[1][0]
        score = int(score_2.iloc[1][1])
        return (title, score)
    elif (plataform == 'netflix'):
        score_netflix = netflix[['title', 'score']]
        score_2 = score_netflix.sort_values(['score', 'title'], ascending=[False, True])
        title = score_2.iloc[1][0]
        score = int(score_2.iloc[1][1])
        return (title, score)
    else:
        return 'La plataforma ingresada no es correcta'

@app.get('/get_longest/{plataform}/{duration}/{year}')
async def get_longest(plataform, duration, year):
    if (plataform == 'amazon'):
        year_amazon = amazon[['title', 'duration_int', 'duration_type', 'release_year']]
        if (type(year) == str):
            year = int(year)
            year_example = year_amazon[year_amazon['release_year'] == year]
            if (type(duration) == str):
                year_example_2 = year_example[year_example['duration_type'] == duration]
                respuest = year_example_2.sort_values('duration_int', ascending=False)
                title=respuest.iloc[0][0]
                durat= respuest.iloc[0][1]
                duration_type = respuest.iloc[0][2]
            return (title, durat, duration_type)
    elif (plataform == 'disney'):
        year_disney = disney[['title', 'duration_int', 'duration_type', 'release_year']]
        if (type(year) == int):
            year = int(year)
            year_example = year_disney[year_disney['release_year'] == year]
            if (type(duration) == str):
                year_example_2 = year_example[year_example['duration_type'] == duration]
                respuest = year_example_2.sort_values('duration_int', ascending=False)
                title=respuest.iloc[0][0]
                durat= respuest.iloc[0][1]
                duration_type = respuest.iloc[0][2]
            return (title, durat, duration_type)
    elif (plataform == 'hulu'):
        year_hulu = hulu[['title', 'duration_int', 'duration_type', 'release_year']]
        if (type(year) == int):
            year = int(year)
            year_example = year_hulu[year_hulu['release_year'] == year]
            if (type(duration) == str):
                year_example_2 = year_example[year_example['duration_type'] == duration]
                respuest = year_example_2.sort_values('duration_int', ascending=False)
                title=respuest.iloc[0][0]
                durat= respuest.iloc[0][1]
                duration_type = respuest.iloc[0][2]
            return (title, durat, duration_type)
    elif (plataform == 'netflix'):
        year_netflix = netflix[['title', 'duration_int', 'duration_type', 'release_year']]
        if (type(year) == str):
            year = int(year)
            year_example = year_netflix[year_netflix['release_year'] == year]
            if (type(duration) == str):
                year_example_2 = year_example[year_example['duration_type'] == duration]
                respuest = year_example_2.sort_values('duration_int', ascending=False)
                title=respuest.iloc[0][0]
                durat= respuest.iloc[0][1]
                duration_type = respuest.iloc[0][2]
            return (title, durat, duration_type)
    else:
        return 'La plataforma ingresada no es correcta'
    
@app.get('/get_rating_count/{rating}')
async def get_rating_count(rating):
    if type(rating == str):
        year_example = amazon[amazon['rating'] == rating]
        cantidad = [len(year_example)]
        resp = rating
        return (resp, cantidad)