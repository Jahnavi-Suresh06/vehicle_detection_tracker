
from VehicleDetectionTracker.VehicleDetectionTracker import VehicleDetectionTracker

video_path = "traffic.mp4"

def show_result(result):
    print("\nVehicles detected in frame:",
          result["number_of_vehicles_detected"])

    for vehicle in result["detected_vehicles"]:
        print(
            "ID:", vehicle["vehicle_id"],
            "| Type:", vehicle["vehicle_type"],
            "| Confidence:", round(vehicle["detection_confidence"], 3),
            "| Speed estimate:", vehicle["speed_info"]
        )

tracker = VehicleDetectionTracker()
tracker.process_video(video_path, result_callback=show_result)
