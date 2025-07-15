from flask import Blueprint, jsonify
from datetime import datetime
from services.student_service import student_service

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_students': student_service.get_student_count()
    }), 200
