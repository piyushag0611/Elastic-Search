# Elastic-Search
This repo is to create an elastic search object which carries out search on a database of movies. The purpose is to show a demonstration of elastic search for GSOC application. I have followed the [coursera lectures](https://www.coursera.org/learn/database-architecture-scale-nosql-elasticsearch-postgresql/home/week/3), for an introduction to elastic search. Luckily, they also show how to make an elastic search object. 

I have used their provided code and modified it to feed the elastic search object on a database of movies. I obtain the movies dataset from [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), and used the first 400 movies, since this is just for demonstration and it was taking time.

To run this search tool, all that you need to do is:

1. Install Elastic Search by pip install elasticsearch.
2. Download repo and run elastictool.py
3. You will be asked to Enter command. Enter command as 'search x' (without quotes and x as any string)

Elastic Search will then spit out the search results from the movie database. 
