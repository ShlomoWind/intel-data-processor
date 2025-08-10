def load_mission_data():
    # sample mission data
    return[
    {"id":"M001","location":"Kabul","status":"Complete","priority":"High"},
    {"id":"M002","location":"Baghdad","status":"Active","priority":"Medium"},
    {"id":"M003","location":"Damascus","status":"Pending","priority":"High"},
    {"id":"M004","location":"Tehran","status":"Complete","priority":"Low"}]

def filter_by_status(mission,status):
    # filter missions by status
    return [m for m in mission if m["status"] == status]

def count_by_priority(missions):
    # count missions by priority level
    counts = {"High":0,"Medium":0,"Low":0}
    for mission in missions:
        counts[mission["priority"]] += 1
    return counts