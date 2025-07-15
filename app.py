from flask import Flask
from routes.student_routes import student_bp
from routes.health_routes import health_bp
from utils.error_handlers import register_error_handlers
from datetime import datetime
import os

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(student_bp, url_prefix='/students')
    app.register_blueprint(health_bp)

    # Register error handlers
    register_error_handlers(app)

    return app

app = create_app()

if __name__ == '__main__':

    print("Starting Student Management API...")
    print("Make sure Ollama is running on localhost:11434 with llama3 model")
    print("API will be available at http://localhost:5000")
    print("\nAvailable endpoints:")
    print("POST   /students           - Create a new student")
    print("GET    /students           - Get all students")
    print("GET    /students/{id}      - Get student by ID")
    print("PUT    /students/{id}      - Update student by ID")
    print("DELETE /students/{id}      - Delete student by ID")
    print("GET    /students/{id}/summary - Generate AI summary for student")
    print("GET    /health             - Health check")

    app.run(
            debug=False,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
            threaded=True
        )
