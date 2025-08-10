from threading import activeCount


def generate_mission_summary(missions):
    """Generate mission summary report"""
    total = len(missions)
    active = len([m for m in missions if m["status"] == "Active"])
    complete = len([m for m in missions if m["status"] == "Complete"])

    report = f"""
    === MISSION INTELLIGENCE SUMMARY ===
    Total Missions: {total}
    Active Missions: {active}
    Completed Missions: {complete}
    Pending Missions: {total - active - complete}
    ==================================
    """
    return report.strip()


def export_data_to_file(data, filename):
    """Export processed data to file"""
    with open(filename,'w') as f:
        f.write(str(data))
    return f"Data export to {filename}"