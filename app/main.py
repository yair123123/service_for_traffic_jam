from flask import Flask

from app.routes.check_traffic_jam_route import traffic_blueprint

app = Flask(__name__)

app.register_blueprint(traffic_blueprint,url_prefix="/api/traffic")

if __name__ == '__main__':
    app.run()