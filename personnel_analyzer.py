def load_personnel_data():
    """Sample personal data"""
    return [
        {"id":"p001", "name": " Smith","rank":"Capitan","unit":"Alpha","clearance":"Secret"},
        {"id":"p002", "name": "Johnson","rank":"Lieutenant","unit":"Bravo","clearance":"Top Secret"},
        {"id":"p003", "name": "Williams","rank":"Sergeant","unit":"Alpha","clearance":"Confidential"},
        {"id":"p004", "name": "Brown","rank":"Major","unit":"Charline","clearance":"Top Secret"}
    ]

def filter_by_clearance(personnel, clearance_level):
    """Filter personal by clearance"""
    return [p for p in personnel if p["clearance"] == clearance_level]

def group_by_unit(personnel):
    units = {}
    for person in personnel:
        unit = person["unit"]
        if unit not in units:
            units[unit] = []
        units[unit].append(person["name"])
    return units

