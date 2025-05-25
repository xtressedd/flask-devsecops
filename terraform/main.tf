provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "flask_app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  user_data     = file("user_data.sh")  # Script para instalar Docker y ejecutar tu imagen
}

resource "aws_security_group" "flask_sg" {
  name        = "flask-devsecops-sg"
  description = "Permitir HTTPS y SSH"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["tu_ip_publica/32"]  # Cambia esto
  }
}


