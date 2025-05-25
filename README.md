Proyecto DevSecOps con Flask, Docker y Terraform
# 🚀 Flask DevSecOps Project

¡Hola! 👋 Este es un proyecto de ejemplo que integra **Flask con prácticas DevSecOps**, demostrando cómo implementar seguridad desde el desarrollo hasta el despliegue. Perfecto para aprender o como base para tus propios proyectos.

## 🔍 ¿De qué va este proyecto?
Imagina que quieres construir una API web (eso que usan las apps para comunicarse), pero que sea segura desde el primer momento y fácil de desplegar. ¡Eso es exactamente lo que hicimos aquí!

Este proyecto es como un "kit de inicio" que combina:

- Flask (para crear la API en Python, super liviana).

- Docker (para empaquetarla y que funcione en cualquier lado).

- Pruebas de seguridad (porque hoy todo necesita protección).

- Terraform (para desplegar en la nube con solo un comando).

Lo especial: todo está pensado para que aprendas o lo uses como base, con:

- ✅ Documentación interactiva (gracias a Swagger: abre http://localhost:5000/swagger-ui y juega con la API).

- 🛡️ Hardening de contenedores (Docker seguro por diseño).

- 🤖 Automatización (GitHub Actions se encarga de probar todo al hacer cambios).

## 🎯 ¿Para quién es?
Si estás aprendiendo DevSecOps: Aquí verás cómo integrar seguridad sin volverte loco.

Si necesitas un boilerplate: Usa esto como punto de partida para tu próxima API.

Si te gusta "ver para creer": Ejecútalo localmente en 2 pasos (¡Docker lo hace fácil!).

## 💡 ¿Por qué me gusta este proyecto?
Porque junta lo técnico (DevSecOps real) con lo práctico (documentación clara, estructura organizada). Es como un Lego: tú decides si solo lo pruebas, lo amplías, o lo usas para enseñar a otros.

¿Te animas a trastear con él? ¡El primer paso está abajo! 👇

docker run -p 5000:5000 flask-devsecops

(Y si algo no cuadra, me avisas 😊).


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
├── app/                # El código de la API (con endpoints seguros y uno "vulnerable" a propósito para aprender)
├── docker/             # La receta para construir el contenedor (como una caja fuerte para tu app)
├── terraform/          # La magia para desplegar en AWS (si quieres llevarlo a la nube, es opcional) 
├── .github/workflows/  # Los robots que prueban todo automáticamente cuando haces un cambio ✨ (Pipelines CI/CD)
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
  (PRONTO HABRÁN NUEVAS IMPLEMENTACIONES)
