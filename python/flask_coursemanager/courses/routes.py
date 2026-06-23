from flask import Blueprint, request, jsonify

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def list_courses():
    return make_response_json([])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400

    required_fields = ['name', 'code', 'credits']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            'status': 'error', 
            'message': f'Missing required fields: {", ".join(missing_fields)}'
        }), 400
        
    mock_new_course = {
        'id': 1,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }
    
    return make_response_json(mock_new_course, 201)

@courses_bp.route('/<int:course_id>/', methods=['GET', 'PUT', 'DELETE'])
def course_detail(course_id):
    if request.method == 'GET':
        return make_response_json({'message': f'Fetch course {course_id}'})
    elif request.method == 'PUT':
        return make_response_json({'message': f'Update course {course_id}'})
    elif request.method == 'DELETE':
        return make_response_json({'message': f'Delete course {course_id}'}, 200)