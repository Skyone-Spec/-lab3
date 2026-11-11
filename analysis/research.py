"""Run from any directory: python analysis/research.py (pandas + scipy)."""
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
movies = pd.read_csv(root / 'data/movies.csv')
ratings = pd.read_csv(root / 'data/ratings.csv')
stats = ratings.groupby('movieId').rating.agg(n='size', mean='mean', sd=lambda x: x.std(ddof=0)).reset_index()
mu = ratings.rating.mean()
stats['weighted'] = (stats.n * stats['mean'] + 25 * mu) / (stats.n + 25)

def top_ids(pool, key):
    return set(pool.sort_values([key, 'n', 'movieId'], ascending=[False, False, True]).head(12).movieId)

print('movies', len(movies), 'rated_movies', len(stats), 'ratings', len(ratings), 'users', ratings.userId.nunique())
print('single_rating_movies', int((stats.n == 1).sum()), 'global_mean', round(mu, 6))
print('Spearman n vs mean', stats[['n','mean']].corr(method='spearman').iloc[0, 1])
print('minimum_n, eligible_movies, top12_overlap (m=25)')
for n in [1, 2, 3, 5, 10, 20, 50, 100]:
    pool = stats[stats.n >= n]
    print(n, len(pool), len(top_ids(pool, 'mean') & top_ids(pool, 'weighted')), sep=', ')

from itertools import combinations
records = stats[stats.n >= 50].merge(movies, on='movieId').to_dict('records')
pairs = ((a,b) for a,b in combinations(records,2) if abs(a['mean']-b['mean']) <= .01)
a,b = max(pairs, key=lambda pair: abs(pair[0]['sd']-pair[1]['sd']))
print('Illustrative pair: >=50 ratings each, mean difference <=0.01; largest SD difference')
for film in [a,b]:
    print({key:film[key] for key in ['movieId','title','n','mean','sd']})
