from app.dbs.settings.config import r
def get_traffic_jam_by_points(lat_lon_key):
    a = r.hgetall(lat_lon_key)
    lat,lon = lat_lon_key.split(",")
    return {"lat":lat,"lon":lon,**a} if a else None
