from astropy.coordinates import get_body_barycentric, SkyCoord, Galactocentric
from astropy.time import Time
from astropy import units as u

user_planet = None

planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]

planet_info = {
    "mercury": {"radius_km": 2439.7, "mass_kg": 3.30e23, "gravity_m_s2": 3.7, "orbital_period_days": 88, "avg_temp_c": 167, "moons": 0},
    "venus": {"radius_km": 6051.8, "mass_kg": 4.87e24, "gravity_m_s2": 8.87, "orbital_period_days": 225, "avg_temp_c": 464, "moons": 0},
    "earth": {"radius_km": 6371.0, "mass_kg": 5.97e24, "gravity_m_s2": 9.81, "orbital_period_days": 365.25, "avg_temp_c": 15, "moons": 1},
    "mars": {"radius_km": 3389.5, "mass_kg": 6.42e23, "gravity_m_s2": 3.71, "orbital_period_days": 687, "avg_temp_c": -65, "moons": 2},
    "jupiter": {"radius_km": 69911, "mass_kg": 1.90e27, "gravity_m_s2": 24.79, "orbital_period_days": 4333, "avg_temp_c": -110, "moons": 95},
    "saturn": {"radius_km": 58232, "mass_kg": 5.68e26, "gravity_m_s2": 10.44, "orbital_period_days": 10759, "avg_temp_c": -140, "moons": 146},
    "uranus": {"radius_km": 25362, "mass_kg": 8.68e25, "gravity_m_s2": 8.69, "orbital_period_days": 30687, "avg_temp_c": -195, "moons": 28},
    "neptune": {"radius_km": 24622, "mass_kg": 1.02e26, "gravity_m_s2": 11.15, "orbital_period_days": 60190, "avg_temp_c": -200, "moons": 16},
    "pluto": {"radius_km": 1188.3, "mass_kg": 1.31e22, "gravity_m_s2": 0.62, "orbital_period_days": 90560, "avg_temp_c": -225, "moons": 5}
}

def get_planet_galactic_coords(planet_name):
    now = Time.now()
    planet = get_body_barycentric(planet_name, now)
    sc = SkyCoord(planet)
    galactic = sc.galactic
    galcen = sc.transform_to(Galactocentric())
    distance_kpc = galcen.cartesian.norm().to(u.kpc).value
    return galactic.l.degree, galactic.b.degree, distance_kpc

def set_planet_from_name(planet_name):
    global user_planet
    if planet_name.lower() not in planets:
        print(f"❌ Invalid planet name. Available options: {', '.join(planets)}")
        return
    user_planet = planet_name.lower()
    print(f"📍 Planet set to: {user_planet.capitalize()}")

def print_ascii_art():
    art = """
    ▄███████▄  ▄█          ▄████████ ███▄▄▄▄      ▄████████     ███            ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████
  ███    ███ ███         ███    ███ ███▀▀▀██▄   ███    ███ ▀█████████▄       ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███
  ███    ███ ███         ███    ███ ███   ███   ███    █▀     ▀███▀▀██       ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███
  ███    ███ ███         ███    ███ ███   ███  ▄███▄▄▄         ███   ▀      ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀█████████▀  ███       ▀███████████ ███   ███ ▀▀███▀▀▀         ███         ▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███        ███         ███    ███ ███   ███   ███    █▄      ███           ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████
  ███        ███▌    ▄   ███    ███ ███   ███   ███    ███     ███           ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███
 ▄████▀      █████▄▄██   ███    █▀   ▀█   █▀    ██████████    ▄████▀         ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███
             ▀                                                                                                                   ███    ███
    """
    print(art)

def print_small_ascii_art():
    art = """
 ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓    ██▓███    ▄████  ██▓███  
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒   ▓██░  ██▒ ██▒ ▀█▒▓██░  ██▒
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ▓██░ ██▓▒▒██░▄▄▄░▓██░ ██▓▒
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ▒██▄█▓▒ ▒░▓█  ██▓▒██▄█▓▒ ▒
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ▒██▒ ░  ░░▒▓███▀▒▒██▒ ░  ░
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒    ▒▓▒░ ░  ░ ░▒   ▒ ▒▓▒░ ░  ░
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ░    ░       ░    ░▒ ░░     ░░       ░   ░ ░▒ ░     
░      ░     ░   ▒    ░ ░  ░    ░       ░    ░▒ ▒ ░░     ░░       ░ ░   ░ ░░       
       ░         ░  ░   ░       ░  ░    ░     ░ ░                       ░          
                      ░                      ░░ ░                                    
   """
    print(art) # why isnt this showing up

def query_object_by_name(name, obj_type="object"):
    try:
        coord = SkyCoord.from_name(name)
        gal = coord.galactic
        print(f"\n🔭 Galactic Coordinates of {obj_type.title()} '{name}':")
        print(f"  Longitude (ℓ): {gal.l.degree:.2f}°")
        print(f"  Latitude (b): {gal.b.degree:.2f}°")
        print(f"  RA: {coord.ra.to_string(unit=u.hour)}  |  Dec: {coord.dec.to_string(unit=u.deg)}")
        print()
    except Exception as e:
        print(f"❌ Could not resolve {obj_type} '{name}': {e}")

def display_command_help(command=None):
    """
    Display help for the commands. If command is provided, display help for that specific command.
    """
    command_help = {
        "$co": {
            "description": "Get the current galactic coordinates of the selected planet.",
            "usage": "$co",
            "example": "Usage: $co\n\nThis command returns the galactic coordinates (ℓ, b) and distance (in kpc) of the current planet you've selected."
        },
        "$loc": {
            "description": "Set the current planet by its name.",
            "usage": "$loc <planet_name>",
            "example": "Usage: $loc Mars\n\nThis command sets the selected planet to 'Mars'. The available planets are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto."
        },
        "$star": {
            "description": "Find and query information about a specific star by name.",
            "usage": "$star <star_name>",
            "example": "Usage: $star Sirius\n\nThis command provides details about the Sirius star, including its spectral type, temperature, and distance."
        },
        "$gal": {
            "description": "Get galactic coordinates for a specified galaxy, star, or celestial object.",
            "usage": "$gal <object_name>",
            "example": "Usage: $gal Andromeda\n\nThis command returns the galactic coordinates (ℓ, b) and distance (in kpc) for the Andromeda galaxy."
        },
        "$blackhole": {
            "description": "Get information about a specific black hole, including mass, distance, and event horizon size.",
            "usage": "$blackhole <blackhole_name>",
            "example": "Usage: $blackhole Sagittarius A\n\nThis command returns detailed information about the 'Sagittarius A' black hole, including its mass and distance from Earth."
        },
        "$nebula": {
            "description": "Find and query information about a specific nebula.",
            "usage": "$nebula <nebula_name>",
            "example": "Usage: $nebula Orion\n\nThis command returns details about the Orion Nebula, such as its type, size, and distance from Earth."
        },
        "$planetfinder --help": {
            "description": "Display help for all available commands in the PlanetFinder program.",
            "usage": "$planetfinder --help",
            "example": "Usage: $planetfinder --help\n\nThis command displays a detailed list of all available commands, including descriptions and usage examples."
        },
    }

    if command:
        
        if command in command_help:
            print(f"\n{command_help[command]['usage']}")
            print(f"Description: {command_help[command]['description']}")
            print(f"Example: {command_help[command]['example']}")
        else:
            print(f"❌ No help available for the command: {command}")
    else:
        
        print("PlanetFinder Command Help:")
        print("-------------------------")
        for cmd, info in command_help.items():
            print(f"\n{info['usage']}")
            print(f"  Description: {info['description']}")
            print(f"  Example: {info['example']}")

def main():
    print_ascii_art()  
    print("Welcome to PlanetFinder; made by pgp! Type '$planetfinder --help' to see all available commands.")
    while True:
        command = input(">>> ").strip()
        if command == "$planetfinder --help":
            display_command_help()
        elif command.startswith("$planetfinder --help "):
           
            specific_command = command[len("$planetfinder --help "):].strip()
            display_command_help(specific_command)
        elif command.startswith("$loc"):
            planet_name = command.split()[1]
            set_planet_from_name(planet_name)
        elif command == "$co":
            if user_planet:
                l, b, distance = get_planet_galactic_coords(user_planet)
                print(f"Galactic Coordinates of {user_planet.capitalize()}:")
                print(f"Longitude (ℓ): {l:.2f}°, Latitude (b): {b:.2f}°, Distance: {distance:.2f} kpc")
            else:
                print("❌ Please set a planet first using $loc <planet_name>")
        elif command == "$smallascii":
            print_small_ascii_art()  
        elif command == "$exit":
            print("Goodbye! 🌌")
            break
        else:
            print("Unknown command. Try '$planetfinder --help' for a list of commands.\n")

if __name__ == "__main__":
    main()
