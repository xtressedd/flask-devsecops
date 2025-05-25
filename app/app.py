from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para Swagger UI

# Configuración de Swagger
api = Api(
    app,
    version='1.0',
    title='API DevSecOps',
    description='Documentación interactiva de la API',
    doc='/swagger-ui',  # Ruta para la UI de Swagger
    contact_email="domingojosejuancesar@gmail.com"
)

# Modelo para documentación (Schema)
secure_model = api.model('SecureEndpoint', {
    'message': fields.String(description='Mensaje de respuesta')
})

# Namespace para agrupar endpoints
ns = api.namespace('api', description='Endpoints principales')

# Endpoint con documentación Swagger
@ns.route('/secure')
class SecureEndpoint(Resource):
    @ns.doc(security=[{'api_key': []}])
    @ns.response(200, 'Éxito', secure_model)
    @ns.response(403, 'API Key inválida')
    def get(self):
        """Endpoint seguro que requiere API Key"""
        api_key = request.headers.get('X-API-KEY')
        if api_key == "123-secure-key":
            return {"message": "Acceso autorizado"}
        return {"error": "API Key inválida"}, 403

# Endpoint vulnerable (para ejemplo)
@ns.route('/vulnerable')
class VulnerableEndpoint(Resource):
    @ns.doc(params={'input': 'Texto de entrada'})
    def get(self):
        """Endpoint con vulnerabilidad intencional (XSS)"""
        user_input = request.args.get('input')
        return f"Input recibido: {user_input}"

# Endpoint raíz
@app.route('/')
def home():
    return "API DevSecOps Funcionando ✅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
