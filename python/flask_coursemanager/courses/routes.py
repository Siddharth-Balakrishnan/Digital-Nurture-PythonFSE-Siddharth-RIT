from flask import Blueprint, request, jsonify
from extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def list_courses():
    # Query all courses from the database
    courses = Course.query.all()
    # Serialize them using our custom to_dict() method
    return make_response_json([c.to_dict() for c in courses])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400

    required_fields = ['name', 'code', 'credits', 'department_id']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            'status': 'error', 
            'message': f'Missing required fields: {", ".join(missing_fields)}'
        }), 400
        
    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id'] # Linking it to a department!
    )
    
    db.session.add(new_course)
    db.session.commit()
    
    return make_response_json(new_course.to_dict(), 201)

@courses_bp.route('/<int:course_id>/', methods=['GET', 'PUT', 'DELETE'])
def course_detail(course_id):
    # This automatically returns our custom 404 JSON error if the ID doesn't exist!
    course = Course.query.get_or_404(course_id)

    if request.method == 'GET':
        return make_response_json(course.to_dict())
        
    elif request.method == 'PUT':
        data = request.get_json()
        if 'name' in data: course.name = data['name']
        if 'code' in data: course.code = data['code']
        if 'credits' in data: course.credits = data['credits']
        if 'department_id' in data: course.department_id = data['department_id']
        
        db.session.commit()
        return make_response_json(course.to_dict())
        
    elif request.method == 'DELETE':
        db.session.delete(course)
        db.session.commit()
        return make_response_json({'message': 'Course successfully deleted'})

@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_enrolled_students(course_id):
    # Verify course exists
    course = Course.query.get_or_404(course_id)
    
    students = Student.query.join(Enrollment).filter(Enrollment.course_id == course_id).all()
    
    return make_response_json([s.to_dict() for s in students])