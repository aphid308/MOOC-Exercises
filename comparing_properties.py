class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
        self.total_price = self.price_per_sqm * self.square_metres

    def bigger(self, compared_to: "RealProperty"):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to: "RealProperty"):
        return abs(self.total_price - compared_to.total_price)

    def more_expensive(self, compared_to: "RealProperty"):
        return self.total_price > compared_to.total_price


if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))