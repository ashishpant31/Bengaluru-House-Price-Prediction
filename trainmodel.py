import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. Load your data
# Make sure 'Cleaned_data.csv' is in the same directory
data = pd.read_csv('Cleaned_data.csv')

# 2. Define the features (X) and target (y)
X = data[['location', 'total_sqft', 'bath', 'bhk']]
y = data['price']

# 3. Create a ColumnTransformer to handle preprocessing
# This is the crucial part that was likely wrong in your original script.
# We are passing the actual objects (e.g., OneHotEncoder()), not strings.
preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'), ['location']),
        ('scaler', StandardScaler(), ['total_sqft', 'bath', 'bhk'])
    ],
    remainder='passthrough'
)

# 4. Create the final pipeline
# This pipeline chains the preprocessing and the Ridge model.
pipe = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])

# 5. Train the model by fitting the pipeline to your data
# The pipeline will automatically apply the transformations and train the model.
pipe.fit(X, y)

# 6. Save the trained pipeline to a pickle file
# This will overwrite your old, corrupted RidgeModel.pkl file.
with open('RidgeModel.pkl', 'wb') as f:
    pickle.dump(pipe, f)

print("New RidgeModel.pkl file has been created successfully!")