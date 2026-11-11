"""Run from any directory: python analysis/research.py (pandas + scipy)."""
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
movies = pd.read_csv(root / 'data/movies.csv')
ratings = pd.read_csv(root / 'data/ratings.csv')
stats = ratings.groupby('movieId').rating.agg(n='size', mean='mean').reset_index()
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
