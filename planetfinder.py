from astropy.coordinates import get_body_barycentric, SkyCoord, Galactocentric, ICRS
from astropy.time import Time
from astropy import units as u


user_planet = None


planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]

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

print_ascii_art()

def print_small_ascii_art():
    art = """
 ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓    ██▓███    ▄████  ██▓███  
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒   ▓██░  ██▒ ██▒ ▀█▒▓██░  ██▒
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ▓██░ ██▓▒▒██░▄▄▄░▓██░ ██▓▒
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ▒██▄█▓▒ ▒░▓█  ██▓▒██▄█▓▒ ▒
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ▒██▒ ░  ░░▒▓███▀▒▒██▒ ░  ░
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒    ▒▓▒░ ░  ░ ░▒   ▒ ▒▓▒░ ░  ░
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░    ░▒ ░       ░   ░ ░▒ ░     
░      ░     ░   ▒    ░ ░  ░    ░       ░    ░▒ ▒ ░░     ░░       ░ ░   ░ ░░       
       ░         ░  ░   ░       ░  ░    ░     ░ ░                       ░          
                      ░                      ░░ ░                                    
   """
    print(art)
    
print_small_ascii_art()



def main():

    print("Type '$co' to get current galactic coordinates of a planet.")
    print("Type '$loc <planet>' to change your planet (e.g., '$loc Mars').")
    print("Type '$exit' to quit.\n")

    while True:
        command = input(">>> ").strip()

        if command.startswith("$co"):
            if user_planet is None:
                print("❌ No planet selected. Use '$loc <planet>' to set a planet first.\n")
                continue
            try:
                lon, lat, dist = get_planet_galactic_coords(user_planet)
                print(f"\n📍 Galactic Coordinates of {user_planet.capitalize()}:")
                print(f"  Longitude (ℓ): {lon:.2f}°")
                print(f"  Latitude (b): {lat:.2f}°")
                print(f"  Distance from Galactic Center: {dist:.2f} kpc (~{dist*3.262:.2f} kly)\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
        elif command.startswith("$loc "):
            planet = command[5:].strip()
            set_planet_from_name(planet)
        elif command == "$exit":
            print("Goodbye! Stay stellar. 🌌")
            break
        else:
            print("Unknown command. Try '$co', '$loc <planet>', or '$exit'.\n")


if __name__ == "__main__":
    main()
