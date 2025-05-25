Proyecto DevSecOps con Flask, Docker y Terraform
# 🚀 Flask DevSecOps Project

¡Hola! 👋 Este es un proyecto de ejemplo que integra **Flask con prácticas DevSecOps**, demostrando cómo implementar seguridad desde el desarrollo hasta el despliegue. Perfecto para aprender o como base para tus propios proyectos.

## 🌟 Características principales

- **API Flask** con endpoints seguros y documentación Swagger integrada.
- **Dockerización** con buenas prácticas de seguridad (usuario no-root, hardening).
- **Pipeline CI/CD** con pruebas de seguridad automatizadas.
- **Infraestructura como código** con Terraform (AWS).
- **Documentación interactiva** gracias a Swagger UI.

## 🛠️ Tecnologías utilizadas

| Área           | Tecnologías                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Backend        | Python, Flask, Flask-RESTX (Swagger)                                        |
| Seguridad      | Bandit (SAST), OWASP ZAP (DAST), Hardening de contenedores                  |
| Infraestructura| Docker, Terraform (AWS)                                                     |
| CI/CD          | GitHub Actions                                                              |

## 🚀 Cómo empezar

### Prerrequisitos
- Docker instalado
- Python 3.9+
- Cuenta en AWS (para Terraform, opcional)

### Ejecución local
```bash
# Clona el repositorio
git clone https://github.com/tuusuario/flask-devsecops.git
cd flask-devsecops

# Construye y ejecuta con Docker
docker build -t flask-devsecops .
docker run -p 5000:5000 flask-devsecops

# Accede a la API
curl http://localhost:5000
Documentación de la API
Una vez en ejecución, visita la UI interactiva de Swagger:

http://localhost:5000/swagger-ui
📂 Estructura del proyecto
flask-devsecops/
├── app/                # Código fuente de la aplicación Flask
├── docker/             # Configuración de Docker
├── terraform/          # Infraestructura en AWS (opcional)
├── .github/workflows/  # Pipelines CI/CD
└── README.md           # Este archivo
🤝 ¿Cómo contribuir?
¡Las contribuciones son bienvenidas! Sigue estos pasos:

Haz un fork del proyecto

Crea una rama (git checkout -b feature/nueva-funcionalidad)

Haz commit de tus cambios (git commit -m 'Añade nueva funcionalidad')

Haz push a la rama (git push origin feature/nueva-funcionalidad)

Abre un Pull Request

📄 Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

Hecho con ❤️ por Domingo José Juan César | 🔗 www.linkedin.com/in/domingo-josé-juan-césar-5a3a71158 | ✉️ domingojosejuancesar@gmail.com
```markdown
  ![CI/CD](https://github.com/xtressedd/flask-devsecops/actions/workflows/devsecops.yml/badge.svg)
