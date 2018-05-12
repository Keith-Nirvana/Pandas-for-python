# -*- coding:utf-8 -*-

import zipfile
import pandas as pd
import requests


class Solution():
	def solve(self):
		countries = 0
		medianNumber = 0.00
		return [countries, medianNumber]

	def request(self):
		# Get the zip file
		ret = requests.get("https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip")

		# Load it to the local folder
		with open("wp08266.zip", "wb") as code:
			code.write(ret.content)

		# Extract the file to read
		z = zipfile.ZipFile("wp08266.zip", "r")
		z.extract("Financial Reform Dataset Dec 2008.dta")

		# Handle the data
		df = pd.read_stata("Financial Reform Dataset Dec 2008.dta")
		countries = df.groupby('country')
		year = df.groupby('country').count().median()['year']

		return [len(countries), year]

		# Second solution
		# df = pd.read_stata("Financial Reform Dataset Dec 2008.dta")['country']
		# countries = len(set(df))
		# number = pd.DataFrame([list(df).count(item) for item in set(df)]).median().at[0]
		# return [countries, number]
