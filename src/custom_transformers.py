from sklearn.base import BaseEstimator , TransformerMixin

class createTitle(BaseEstimator , TransformerMixin):
    
    def fit(self , X , y = None):
        return self
    
    def transform(self , X , y=None):

        X_transformed = X.copy()
        # Extract the title
        X_transformed['Title'] = X_transformed['Name'].apply(lambda x : x.split(',')[1].split('.')[0].replace(' ' , '').casefold())

        # merge the synonms
        X_transformed['Title'] = X_transformed['Title'].replace(['mlle', 'ms'], 'miss')
        X_transformed['Title'] = X_transformed['Title'].replace('mme', 'mrs')

        # Create a other category
        rare_titles = ['don', 'rev', 'dr', 'major', 'lady', 'sir', 'col', 'capt', 'thecountess', 'jonkheer']
        X_transformed['Title'] = X_transformed['Title'].replace(rare_titles, 'Rare')

        return X_transformed
    

class createFamily(BaseEstimator , TransformerMixin):

    def binFamily(self , x : int) -> str:
        if x == 1:
            return 'alone'
        if x >=2 and x <= 4:
            return 'small'
        return 'large'

    def fit(self , X , y = None):
        return self
    
    def transform(self , X , y = None):

        X_transformed = X.copy()
        # Create the family size column
        X_transformed['FamilySize'] = X_transformed['SibSp'] + X_transformed['Parch'] + 1

        X_transformed['FamilyGroup'] = X_transformed['FamilySize'].apply(self.binFamily)

        return X_transformed
    
class createDeck(BaseEstimator , TransformerMixin):

    def fit(self, X , y=None):
        return self
    
    def transform(self , X , y = None):

        X_transformed = X.copy()

        X_transformed['Deck'] = X_transformed['Cabin'].apply(lambda x : x[0] if type(x) == str else 'U')

        return X_transformed
    

from sklearn.base import BaseEstimator, TransformerMixin

class ColumnDropper(BaseEstimator, TransformerMixin):

    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(self.columns, axis=1 , errors = 'ignore')