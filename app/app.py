from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import os
from functools import wraps

# Configuración inicial
app = Flask(__name__)
CORS(app)  # Habilita CORS

# Configuración de Swagger
api = Api(
    app,
    version='1.0',
    title='API DevSecOps',
    description='API con ejemplos de seguridad',
    doc='/swagger-ui',
    security='api_key',
    authorizations={
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }
)

# --- Seguridad ---
def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if api_key != os.getenv('API_KEY', '123-secure-key'):
            return {'error': 'API Key inválida'}, 403
        return func(*args, **kwargs)
    return wrapper

# Modelos para Swagger
secure_model = api.model('SecureResponse', {
    'message': fields.String(required=True, example='Acceso autorizado')
})

# Namespace
ns = api.namespace('api', description='Endpoints principales')

# --- Endpoints ---
@ns.route('/secure')
class SecureEndpoint(Resource):
    @ns.doc(security=['api_key'])
    @ns.marshal_with(secure_model)
    @require_api_key
    def get(self):
        """Endpoint seguro con autenticación"""
        return {'message': 'Acceso autorizado'}

@ns.route('/vulnerable')
class VulnerableEndpoint(Resource):
    @ns.doc(params={'input': 'Texto de entrada'})
    def get(self):
        """Ejemplo de vulnerabilidad XSS"""
        user_input = request.args.get('input', '')
        return f'<div>{user_input}</div>', 200

# Configuración para Gunicorn
application = app  # ¡Esta línea es crucial!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
