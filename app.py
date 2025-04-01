from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/concat', methods=['GET'])
def concatenate_strings():
    # Get the 'str1' and 'str2' parameters from the URL query
    str1 = request.args.get('str1', '')
    str2 = request.args.get('str2', '')

    # Concatenate the strings
    result = str1 + str2

    # Return the JSON response
    return jsonify({"concatenated_string": result})

if __name__ == '__main__':
    app.run(debug=True)