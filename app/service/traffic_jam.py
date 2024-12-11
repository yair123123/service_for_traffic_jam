from functools import reduce
from typing import List, Dict

from app.dbs.redis.redis_traffic_repository import get_traffic_jam_by_points


routes = {
    "routes": [
        {
            "directions": [
                [32.0590333, 34.7868434],
                [31.768319, 35.213740],
                [32.0853, 34.7818]
            ],
            "points": [
                [32.0590333, 34.7868434],
                [31.768319, 35.213740],
                [32.0853, 34.7818]
            ]
        },
        {
            "directions": [
                [32.328704, 34.877957],
                [31.951569, 34.773371],
                [32.080006, 34.770982]
            ],
            "points": [
                [32.328704, 34.877957],  # נתניה
                [31.951569, 34.773371],  # אשדוד
                [32.080006, 34.770982]  # פתח תקווה
            ]
        },
        {
            "directions": [
                [32.164158, 34.855313],  # רמת גן
                [32.073532, 34.792146],  # חולון
                [31.9330, 34.7884]  # באר שבע
            ],
            "points": [
                [32.164158, 34.855313],  # רמת גן
                [32.073532, 34.792146],  # חולון
                [31.9330, 34.7884]  # באר שבע
            ]
        }
    ]
}
def find_traffic_jam_in_route(steps: List[Dict[str, List[int]]]):
    coordinates_str = [f"{coord[0]},{coord[1]}" for coord in steps["directions"]]
    return list(filter(lambda x: x, [get_traffic_jam_by_points(x) for x in coordinates_str]))




def find_short_route_by_traffic_jam(routes):
    def sum_duration(accumulator, item):
        return accumulator + int(item.get('duration', 0))

    traffic_jam = {i: find_traffic_jam_in_route(routes["routes"][i]) for i in range(len( routes["routes"]))}
    print("a")
    duration_routing = {k:reduce(sum_duration,v,0) for k,v in traffic_jam.items()}
    route_id = min(duration_routing,key=duration_routing.get)
    return{"route_id": route_id,"traffic_jam":traffic_jam[route_id]}