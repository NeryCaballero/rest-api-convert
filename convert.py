from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

'''  REST API with one endpoint /convert expects a JSON body containing a list of ASCII characters
returns a JSON response containing a list of integers based on the provided list of characters,
For each ASCII alphabet character below H or h, the corresponding integer should be the character ASCII
code multiplied by 10, otherwise it should be 0.
'''


@app.route('/convert', methods=['POST'])
def get_ascii():
    content = request.json
    df = pd.DataFrame(content)
    ascii_list = []
    for row in df.iterrows():
        ascii_number = ord(row[1][0])
        if ascii_number in range(97, 104) or ascii_number in range(65, 72):
            ascii_list.append(ascii_number * 10)
        else:
            ascii_list.append(int(0))
    df['ascii'] = ascii_list
    ascii_list_to_return = df['ascii'].tolist()
    print('TYPE: ', jsonify(ascii_list_to_return))
    return jsonify(ascii_list_to_return)


if __name__ == '__main__':
    app.run(debug=True)
