class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print("국가 클래스 메소드")


class Korea(Country):
    """Sub Class"""

    def __init__(self, name, population, capital):

        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        super().show()
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )

if __name__ == '__main__':
    kor = Korea('대한민국', 50000, '서울')
    kor.show()
    print(kor.name)
    print(kor.population)