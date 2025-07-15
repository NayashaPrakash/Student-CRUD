from flask import Blueprint, request, jsonify
from services.student_service import student_service
from services.ollama_service import ollama_service
from utils.validators import validate_student_data
import logging

student_bp = Blueprint('students', __name__)
logging.basicConfig(level=logging.DEBUG)

# Create a new student
@student_bp.route('', methods=['POST'])
def create_student():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Validate incoming student data
        errors = validate_student_data(data)
        if errors:
            return jsonify({'errors': errors}), 400

        # Create student via service
        student = student_service.create_student(
            name=data['name'],
            age=data['age'],
            email=data['email'],
            interests=data.get('interests', []),
            achievements=data.get('achievements', []),
            courses=data.get('courses', [])
        )

        # Return success response with student data
        return jsonify({
            'message': 'Student created successfully',
            'student': student.to_dict()
        }), 201

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# Get list of all students
@student_bp.route('', methods=['GET'])
def get_all_students():
    try:
        students = student_service.get_all_students()
        student_list = [student.to_dict() for student in students]

        return jsonify({
            'students': student_list,
            'total': len(student_list)
        }), 200

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# Get a single student by ID
@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        student = student_service.get_student_by_id(student_id)

        if not student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({'student': student.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# Update an existing student by ID
@student_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Validate provided fields (partial update allowed)
        errors = validate_student_data(data, required_fields=[])
        if errors:
            return jsonify({'errors': errors}), 400

        # Update student using provided fields
        student = student_service.update_student(
            student_id=student_id,
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email'),
            interests=data.get('interests'),
            achievements=data.get('achievements'),
            courses=data.get('courses')
        )

        if not student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({
            'message': 'Student updated successfully',
            'student': student.to_dict()
        }), 200

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# Delete a student by ID
@student_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student = student_service.delete_student(student_id)

        if not student:
            return jsonify({'error': 'Student not found'}), 404

        return jsonify({'message': 'Student deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# Generate a summary for a student by ID using Ollama service
@student_bp.route('/<int:student_id>/summary', methods=['GET'])
def get_student_summary(student_id):
    try:
        student = student_service.get_student_by_id(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        # Prepare student data for summary generation
        student_data = student.to_dict() if hasattr(student, 'to_dict') else student
        logging.debug(f"Generating summary for student: {student_data}")

        # Call external service to generate summary
        summary = ollama_service.generate_student_summary(student_data)
        logging.debug(f"Summary received: {summary}")

        return jsonify({
            'student': student_data,
            'summary': summary
        }), 200

    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
