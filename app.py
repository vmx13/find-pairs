from flask import Flask, request, jsonify
from marshmallow import Schema, fields
app = Flask(__name__)


class UserSchema(Schema):
    numbers = fields.List(fields.Int(strict=True, required=True))
    target = fields.Integer(required=True, strict=True)


# POST API to return list of indices whose sum is equals to the given target
@app.route('/find-pairs', methods=['POST'])
def find_pairs():
    print(__name__)
    schema = UserSchema()
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    numbers = data['numbers']
    target = data['target']
    
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((i,j))
    return jsonify(pairs), 200


if __name__ == '__main__':
    app.run()


# note :
# I tried to use marshmallow for validation.
# I can use pydantic structure as well but time doesnt allowed :,
# if time permitted I could have used async await to handle multiple requests parallely.

