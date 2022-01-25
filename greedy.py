""" Условие задачи в папке Results (greedy_station_set)"""

def FindBestStation(states_needed, stations):

    """ итоговый набор станций """
    final_stations = set()

    while states_needed:
        best_station = None
        towns_covered = set()
        for station, states in stations.items():
            covered = states_needed & states # города не входящие в покрытие, но покрываемые текущей станцией
            if len(covered) > len(towns_covered):
                best_station = station
                towns_covered = covered
        states_needed -= towns_covered # станции, входящие в покрытия не нужны больше
        final_stations.add(best_station)
    return (final_stations)


if __name__ == '__main__':

    towns_needed = set(['MSC', 'KRA', 'SCH', 'VLG', 'SRT', 'SAM', 'MRM', 'StP'])
    stations = {}
    stations['1A'] = set (['MSC', 'KRA', 'SCH'])
    stations['2B'] = set (['StP', 'MRM', 'mt'])
    stations['3C'] = set (['MRM', 'SAM', 'SRT'])
    stations['4D'] = set (['SCH', 'VLG', 'SRT'])
    stations['5F'] = set (['StP', 'MSC', 'KRA', 'SCH'])

    print("Необходимый минимум станций для покрытия всех городов:",FindBestStation (towns_needed , stations ))