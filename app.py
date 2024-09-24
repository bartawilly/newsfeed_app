from flask import Flask, request, jsonify
from services.post_service import PostService

app = Flask(__name__)

# Endpoint to add a new post
@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    user_id = data.get('user_id')
    content = data.get('content')

    if not user_id or not content:
        return jsonify({'error': 'Missing user_id or content'}), 400

    post_id = PostService.create_post(user_id, content)
    if post_id:
        return jsonify({'message': 'Post created', 'post_id': post_id}), 201
    else:
        return jsonify({'error': 'Failed to create post'}), 500

# Endpoint to get a post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_post(post_id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify({'error': 'Post not found'}), 404

# Endpoint to update a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Missing content'}), 400

    success = PostService.update_post(post_id, content)
    if success:
        return jsonify({'message': 'Post updated'}), 200
    else:
        return jsonify({'error': 'Failed to update post'}), 500

# Endpoint to delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    success = PostService.delete_post(post_id)
    if success:
        return jsonify({'message': 'Post deleted'}), 200
    else:
        return jsonify({'error': 'Failed to delete post'}), 500

if __name__ == '__main__':
    app.run(debug=True)