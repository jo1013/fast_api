from fastapi import FastAPI
import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds



def reco(user_id,num_recommendations=15):
    # 데이터파일
    df_ratings = pd.read_csv('/home/fast_api/datas/ratings.csv')
    df_movies = pd.read_csv('/home/fast_api/datas/movies.csv')
    #필요 데이터 pivot
    df_user_movie_ratings = df_ratings.pivot(
    index = 'userId',
    columns = 'movieId',
    values = 'rating'
    ).fillna(0)
    
    
    
    matrix = df_user_movie_ratings.values
    user_ratings_mean = np.mean(matrix, axis = 1)
    matrix_user_mean = matrix - user_ratings_mean.reshape(-1,1)
    pd.DataFrame(matrix_user_mean, columns = df_user_movie_ratings.columns).head()
    
    U, sigma, Vt = svds(matrix_user_mean, k = 12 )
    sigma = np.diag(sigma)
    svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = df_user_movie_ratings.columns)
    
    ori_movies_df = df_movies
    ori_ratings_df = df_ratings 
    
    user_row_number = user_id - 1
    #평점 순으로 정렬
    sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False) 
    
    user_data = ori_ratings_df[ori_ratings_df.userId == user_id]
    user_history = user_data.merge(ori_movies_df, on = 'movieId').sort_values(['rating'], ascending=False)
    recommendations = ori_movies_df[~ori_movies_df['movieId'].isin(user_history['movieId'])]
    # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations을 합친다. 
    recommendations = recommendations.merge( pd.DataFrame(sorted_user_predictions).reset_index(), on = 'movieId')
    # 컬럼 이름 바꾸고 정렬해서 return
    recommendations = recommendations.rename(columns = {user_row_number: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommendations, :]
    

    df = recommendations.iloc[:,:1]
    dit_movid = df.to_dict()
    return dit_movid
