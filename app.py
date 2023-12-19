from flask import Flask , render_template , request , jsonify
import text_sentiment_prediction
from predict_bot_response import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('C:/Users/swapn/Desktop/Byjus Coding/Project 122/templates/index.html')

@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
        
    else:

        sentiment , path = text_sentiment_prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment': sentiment,
                    'path' : path}
        
        return jsonify(response)
    
@app.route('/save' , methods = ['POST'])
def save():

    data = request.json.get('date')
    product = request.json.get('product')
    review = request.json.get('review')
    sentiment = request.json.get('sentiment')

    data_entry = date + "," + product + "," + review + "," + sentiment

    f = open('C:/Users/swapn/Desktop/Byjus Coding/Project 122/static/assets/data_files/updated_product_dataset.csv' ,'a')

    f.write(data_entry + '\n')

    f.close()

    return jsonify({'status' : 'success' ,
                    'message': 'Data Logged'})

@app.route("/", methods=[""])
def bot():

    input_text = request.json.get("user_bot_input_text")
   
    bot_res = bot_response(input_text)

    response = {
            "bot_response": bot_res
        }

    return jsonify(response)
     
if __name__ == '__main__':
    app.run(debug=True)
