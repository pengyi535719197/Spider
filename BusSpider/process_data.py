import pandas as pd
import json

def process_data():
    data = pd.read_table("buses.txt", header=None)
    buses = []
    for bus in list(data[0]):
        bus = json.loads(bus)
        province = bus['province']
        city = bus['city']
        bus_line = bus['bus_line']
        start_station = bus['bus_start_station']
        end_station = bus['bus_end_station']
        stations = bus['bus_stationNames']
        bus = [province, city, bus_line, start_station, end_station, stations]
        buses.append(bus)

    buses_line = pd.DataFrame(buses,columns=['省', '市', '线路', '起始站', '终点站', '沿途站点'])
    buses_line.to_excel('buses.xlsx')










if __name__ == "__main__":
    process_data()
