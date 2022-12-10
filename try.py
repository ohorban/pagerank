import gensim.downloader
vectors = gensim.downloader.load('glove-twitter-25')
print([str(w[0]) for w in vectors.most_similar('weapons')])
