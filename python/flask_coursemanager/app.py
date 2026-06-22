from flask import Flask
from config import Config
from courses.routes import courses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(courses_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
