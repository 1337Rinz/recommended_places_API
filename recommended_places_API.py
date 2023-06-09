# pip install flask pandas scikit-learn
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Flask application
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Load the dataset and perform data preprocessing
df = pd.read_csv('https://raw.githubusercontent.com/1337Rinz/DATA_for_machine_learning/main/dataHUE.csv', delimiter=';')
df = df.fillna('')
df_encoded = pd.get_dummies(df.drop(columns=['địa điểm tham quan']))
similarity_matrix = cosine_similarity(df_encoded.T)

# Define the API endpoint for recommending places
@app.route('/recommend', methods=['POST'])
def recommend_places():
    # Get user input from the request
    user_input = request.json

    # Create a DataFrame for the user input
    user_df = pd.DataFrame(user_input, index=[0])

    # Encode the user's input
    user_encoded = pd.get_dummies(user_df)

    # Recommend places to visit for the user
    similar_items_indices = similarity_matrix[user_encoded.values.argmax()].argsort()[::-1]
    recommended_places = []
    for idx in similar_items_indices:
        places = df['địa điểm tham quan'].iloc[idx].split(', ')
        for place in places:
            if place not in recommended_places:
                recommended_places.append(place)
                if len(recommended_places) >= 5:
                    break
        if len(recommended_places) >= 5:
            break

    # Convert the recommendations to JSON format
    output = {'top_recommended_places': recommended_places}

    # Return the JSON response
    return jsonify(output)

# Run the Flask application
if __name__ == '__main__':
    app.run()

