# -*- coding:utf-8 -*-

import pandas as pd
import requests
import zipfile


class Solution():
	def solve(self):
		ret = requests.get("http://files.grouplens.org/datasets/movielens/ml-latest-small.zip")

		with open("ml-latest-small.zip", "wb") as code:
			code.write(ret.content)

		z = zipfile.ZipFile("ml-latest-small.zip", "r")
		z.extractall()

		movies = pd.read_csv("ml-latest-small/movies.csv")
		ratings = pd.read_csv("ml-latest-small/ratings.csv")

		id1_movie = movies[movies.movieId == 1]['title'].at[0]
		id1_movie_type_count = len(movies[movies.movieId == 1]['genres'].at[0].split("|"))

		# first method, add a similar line as index
		most_rated_movie = ratings.groupby(['movieId'], sort = True).count()
		most_rated_movie['Base'] = pd.Series(list(range(movies.count()['movieId'])))
		index = most_rated_movie.max()['userId']
		movie_id = most_rated_movie[most_rated_movie.userId == index]['Base']
		result = movies[movies.movieId == int(movie_id)]['title'].values[0]

		# second, use index.values
		merge_result = pd.merge(movies, ratings, on = "movieId")
		df = merge_result.loc[:, ('movieId', 'title', 'rating')]
		after_groupby = df.groupby('movieId').count()
		target_index = after_groupby[after_groupby.rating == after_groupby.max().values[0]]
		result = movies[movies.movieId == target_index.index.values[0]]['title'].values[0]

		return [id1_movie, id1_movie_type_count, result]
