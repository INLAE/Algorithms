def dijkstras():
    # описание графа
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 4
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["c"] = 2

    graph["b"] = {}
    graph["b"]["c"] = 6

    graph["c"] = {}
    graph["c"]["d"] = 3
    graph["c"]["e"] = 7

    graph['d'] = {}
    graph["d"]["e"] = 3

    graph['e'] = {}
    graph["e"]["f"] = 1

    graph['f'] = {}
    graph["f"]["g"] = 2
    graph["f"]["end"] = 4

    graph['g'] = {}
    graph["g"]["end"] = 1

    graph["end"] = {}

    # бесконечность выдаём за незнание веса пути
    infinity = float("inf")
    # таблица весов от начала к узлу
    costs = {"a": 4, "b": 2,
             "c": infinity, "d": infinity, "e": infinity,
             "f": infinity, "g": infinity, "end": infinity}

    # таблица родителей
    parents = {"a": "start", "b": "start", "end": None}

    # массив для отработанных узлов
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        # пройдёмся по каждому узлу
        for node in costs:
            cost = costs[node]
            # самый низкий вес и не отработанный
            if cost < lowest_cost and node not in processed:
                # ставим как новый узел с наименьшей стоимостью
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # Найти самый дешёвый необработанный узел.
    node = find_lowest_cost_node(costs)
    # пока не отработаем все узлы
    while node is not None:
        cost = costs[node]
        # проход по всем соседям узла
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # если легче добраться до соседа через этот узел
            if costs[n] > new_cost:
                # ... обновить вес узла.
                costs[n] = new_cost
                # этот узел стал новым родителем для этого соседа.
                parents[n] = node
        # отмечаем обработанный узел
        processed.append(node)
        # найти следующий узел для обработки и вперёд
        node = find_lowest_cost_node(costs)

    print("Стоимость (суммарный вес) от старта до каждого узла:"'\n', costs)
    print("Кратчайшее расстояние от начала до конца:", costs.get('end'))


if __name__ == '__main__':
    """Тест"""
    dijkstras()
