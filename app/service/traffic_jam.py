from functools import reduce
from typing import List, Dict

from app.dbs.redis.redis_traffic_repository import get_traffic_jam_by_points


def find_traffic_jam_in_route(steps: List[Dict[str, List[int]]]):
    coordinates_str = [f"{coord[0]},{coord[1]}" for item in steps for coord in [item['coordinates']]]
    return list(filter(lambda x: x, [get_traffic_jam_by_points(x) for x in coordinates_str]))


def find_short_route_by_traffic_jam(routes: Dict[str, List[Dict[str, List[int]]]]):
    def sum_duration(accumulator, item):
        return accumulator + int(item.get('duration', 0))

    traffic_jam = {k: find_traffic_jam_in_route(v["steps"]) for k, v in routes.items()}
    print("a")
    # duration_routing = {k:reduce(sum_duration,traffic_jam}
    # return min(duration_routing,key=duration_routing.get)