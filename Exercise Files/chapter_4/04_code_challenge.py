from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer

import pandas as pd

def engineer_features(df):
    # Count Vectorizer for titles
    cvec = CountVectorizer()
    titles = cvec.fit_transform(df['title'])
    t_df = pd.DataFrame(titles.toarray(), columns=cvec.get_feature_names_out())

    # One-hot encoding for genres
    dvec = DictVectorizer(sparse=False)
    genres = dvec.fit_transform(df[['genre']].to_dict('records'))
    g_df = pd.DataFrame(genres, columns = dvec.get_feature_names_out())

    # Calculate price per sale
    df['price_per_sale'] = df['price'] / df['sales']

    engineered_df = pd.concat([df, t_df, g_df], axis=1)
    engineered_df = engineered_df.drop(['title', 'genre'], axis=1)

    return engineered_df
