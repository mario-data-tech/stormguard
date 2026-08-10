"""Lógica de decisión: Cruza activos con alertas climáticas."""

def is_point_in_polygon(lat, lon, polygon):
    """Algoritmo de Ray-Casting para saber si un punto está dentro de un polígono."""
    n = len(polygon)
    inside = False
    if not polygon:
        return False
    p1x, p1y = polygon[0][0], polygon[0][1]
    
    for i in range(n + 1):
        p2x, p2y = polygon[i % n][0], polygon[i % n][1]
        if lat > min(p1y, p2y):
            if lat <= max(p1y, p2y):
                if lon <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (lat - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or lon <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def check_fleet_risk(fleet_assets, active_alerts):
    """
    Recibe lista de activos y lista de alertas activas.
    Devuelve los activos en riesgo.
    """
    risks = []
    for asset in fleet_assets:
        for alert in active_alerts:
            polygon = alert.get("polygon", [])
            if is_point_in_polygon(asset['lat'], asset['lon'], polygon):
                risks.append({
                    "asset_id": asset['id'],
                    "alert_type": alert.get("type", "Severe Weather"),
                    "severity": alert.get("severity", "Unknown"),
                    "recommended_action": "DETENER/DESVIAR"
                })
    return risks
