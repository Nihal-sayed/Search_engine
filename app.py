from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def search_csv(query, csv_file):
    # Load CSV file into a pandas DataFrame
    df = pd.read_csv('video_subtitles.csv')

    # Search for the query in the DataFrame
    if query.lower() in df.values.flatten():
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['query']
    csv_file = "video_subtitles.csv"  # Specify the path to your CSV file
    is_present = search_csv(user_query, csv_file)

    return render_template('result.html', query=user_query, is_present=is_present)

if __name__ == "__main__":
    app.run(debug=True)
