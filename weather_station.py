class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations = []


    def latest_observation(self):
        if self.__observations:
            return self.__observations[-1]
        else:
            return ""


    def number_of_observations(self):
        if self.__observations:
            return len(self.__observations)
        else:
            return 0

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
