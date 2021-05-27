class HashTable:

    def average_temperature(self, lt, index):
        avg_tem = 0
        lst = [int(i) for i in list(lt.values())[1:]]
        for i in range(index):
            avg_tem += lst[i]
        return avg_tem / index

    def maximum_temperature(self, lt):
        lst = [int(i) for i in list(lt.values())[1:]]
        lst.sort(reverse=True)
        return lst[0]

    def tem_search(self, dsct, key):
        return dsct[key]


weather_report = {}

if __name__ == '__main__':
    with open("D:/Personal/python_practice/nyc_weather.csv", "r") as f:
        for line in f:
            token = line.split(",")
            day = token[0]
            temperature = token[1].replace("\n", "")
            weather_report[day] = temperature

        print(weather_report)

        h = HashTable()
        print(h.maximum_temperature(weather_report))
        print(h.average_temperature(weather_report, 7))
        print(h.tem_search(weather_report, 'Jan 9'))
        print(h.tem_search(weather_report, 'Jan 6'))
