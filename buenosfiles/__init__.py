from flask import Flask
from buenosfiles.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    from buenosfiles.errors.handlers import errors
    from buenosfiles.ultimos.routes import ultimos
    from buenosfiles.about.routes import about
    from buenosfiles.cat.technologia.routes import tech
    from buenosfiles.cat.naturaleza.routes import naturaleza



    app.register_blueprint(about)
    app.register_blueprint(errors)
    app.register_blueprint(ultimos)
    app.register_blueprint(naturaleza)
    app.register_blueprint(tech)


    return app
