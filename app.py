from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos (Render PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = "TU_URL_DE_RENDER"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "clave-super-secreta"

    db.init_app(app)

    # Importar modelos
    from models import Usuario, Folio, DocumentoInterno

    @app.route("/")
    def home():
        return "SICOF-1 está funcionando correctamente"

    return app

app = create_app()
