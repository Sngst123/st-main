import re

def check_coordinates(latitude, longitude):
    return 50 <= latitude <= 80 and 20 <= longitude <= 45

def main():
    try:
        with open('coordinates.txt', 'r') as file:
            for line in file:
                match = re.match(r'\((-?\d+\.\d+), (-?\d+\.\d+)\)', line)
                if match:
                    latitude, longitude = map(float, match.groups())
                    latitude = round(latitude, 6)
                    longitude = round(longitude, 6)
                    if check_coordinates(latitude, longitude):
                        print((latitude, longitude))
    except FileNotFoundError:
        print("Файл 'coordinates.txt' не найден.")

if __name__ == "__main__":
    main()
