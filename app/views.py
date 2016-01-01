from app import app, db
from flask import jsonify, abort, make_response, request, url_for

from .models import Tag

def make_public_tag(tag):
    new_tag = {}
    for field in tag.serialise:
        if field == 'id':
            new_tag['uri'] = url_for('get_tag', tag_id=tag.id, _external=True)
        else:
            new_tag[field] = tag.serialise[field]
    return new_tag

@app.route('/assured/api/v1.0/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify({'tags': map(make_public_tag, tags)})

@app.route('/assured/api/v1.0/tags/<int:tag_id>', methods=['GET'])
def get_tag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag == None:
        abort(404)
    return jsonify({'tag': make_public_tag(tag)})

@app.route('/assured/api/v1.0/tags/auth', methods=['GET'])
def auth():
    if not request.json:
        abort(400)
    if not 'uid' in request.json or type(request.json['uid']) is not unicode:
        abort(400)
    tag = Tag.query.filter_by(uid=request.json['uid']).first()
    if tag is None:
        abort(404)
    return jsonify({'tag': make_public_tag(tag)})

@app.route('/assured/api/v1.0/tags', methods=['POST'])
def create_tag():
    if not request.json or 'uid' not in request.json or 'name' not in request.json:
        abort(400)
    if not isinstance(request.json['name'], (str, unicode)):
        abort(400)
    if 'access_room1' in request.json and not isinstance(request.json['access_room1'], bool):
        abort(400)
    tag = Tag(
        name = request.json['name'],
        uid = request.json['uid'],
        access_room1 =  request.json.get('access_room1', False), # Default: no access
        inside_room1 = False
    )
    db.session.add(tag)
    db.session.commit()
    return jsonify({'tag': make_public_tag(Tag.query.get(tag.id))}), 201

@app.route('/assured/api/v1.0/tags/<int:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag == None:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not unicode:
        abort(400)
    if 'uid' in request.json and type(request.json['uid']) is not unicode:
        abort(400)
    if 'access_room1' in request.json and type(request.json['access_room1']) is not bool:
        abort(400)
    if 'inside_room1' in request.json and type(request.json['inside_room1']) is not bool:
        abort(400)
    tag.name = request.json.get('name', tag.name)
    tag.uid = request.json.get('uid', tag.uid)
    tag.access_room1 = request.json.get('access_room1', tag.access_room1)
    tag.inside_room1 = request.json.get('inside_room1', tag.inside_room1)
    db.session.commit()
    return jsonify({'tag': make_public_tag(tag)})

@app.route('/assured/api/v1.0/tags/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag == None:
        abort(404)
    db.session.delete(tag)
    db.session.commit()
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
