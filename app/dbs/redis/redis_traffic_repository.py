from app.dbs.settings.config import r
def get_traffic_jam_by_points(lat_lon_key):
    return r.hgetall(lat_lon_key)