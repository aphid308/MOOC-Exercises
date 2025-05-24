class Country:
    """ This class models a single country with population """
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

class RunningEvent:
    """ The class models a foot race event of a length of n metres  """
    def __init__(self, length: int, name: str = "no name"):
        self.length = length
        self.name = name

    def __repr__(self):
        return f"{self.length} m. ({self.name})"

if __name__ == "__main__":
    finland = Country("Finland", 6000000)
    malta = Country("Malta", 500000)
    sweden = Country("Sweden", 10000000)
    iceland = Country("Iceland", 350000)

    countries = [finland, malta, sweden, iceland]

    bigger_countries = [country.name for country in countries if country.population > 5000000]
    for country in bigger_countries:
        print(country)
    # Running Events
    lengths = [100, 200, 1500, 3000, 42195]
    # use comprehension to create new RunningEvent objects from length (name is default)
    events = [RunningEvent(length) for length in lengths]

    # Print out all events
    print(events)

    # Pick one from the list and give it a name
    marathon = events[-1]  # the last item in the list
    marathon.name = "Marathon"

    # Print out everything again, including the new name
    print(events)