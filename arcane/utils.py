from flask import jsonify

def to_json(rows):
    """
    Convert rows from the query to a json object
    """
    
    data = []
    for row in rows:
        data.append(dict(row))
    return jsonify(data)