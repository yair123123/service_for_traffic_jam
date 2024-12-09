from flask import blueprints, request, jsonify

from app.service.traffic_jam import find_short_route_by_traffic_jam

traffic_blueprint = blueprints.Blueprint("traffic",__name__)

@traffic_blueprint.route("/get_traffic_jam",methods=["POST"])
def get_traffic_jam():
    routes = {f'route_{i}': sublist for i, sublist in enumerate(request.json)}
    short_route = find_short_route_by_traffic_jam(routes)
    return jsonify(routes[short_route])