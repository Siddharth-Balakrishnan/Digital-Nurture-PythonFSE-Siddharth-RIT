from flask import Blueprint, jsonify

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

@courses_bp.route('/', methods=['GET'])
def list_courses():
    return jsonify([])