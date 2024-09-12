from pysolar.solar import get_altitude, get_radiation_direct
import datetime
import unreal

# Pysolar calculations
latitude = 42.206
longitude = -71.382
date = datetime.datetime.now(datetime.timezone.utc)

altitude = get_altitude(latitude, longitude, date)
radiation = get_radiation_direct(date, altitude)

# Unreal Engine integration
sun_actor = unreal.EditorLevelLibrary.get_all_level_actors()[0]  # Assuming the first actor is the sun
sun_actor.set_actor_rotation(unreal.Rotator(altitude, 0, 0))

# Print values for debugging
print(f"Sun altitude: {altitude}")
print(f"Solar radiation: {radiation}")
