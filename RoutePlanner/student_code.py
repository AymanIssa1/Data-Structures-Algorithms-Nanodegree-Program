import heapq
import math


# Brute force attempt
def shortest_path(M, start, goal):
    print("shortest path called")
    if start == goal:
        return [start]

    minHeap = [(calculate_route_cost(M.intersections[start], M.intersections[goal]), [start])]

    while len(minHeap) != 0:
        heapq.heapify(minHeap)
        print(minHeap)
        current_cost, current_path = heapq.heappop(minHeap)

        current_intersection = current_path[len(current_path) - 1]
        if current_intersection == goal:
            minHeap.append((current_cost, current_path))
            break

        for route in M.roads[current_intersection]:
            if route not in current_path:
                path = [_ for _ in current_path]
                path.append(route)
                minHeap.append((
                    route_cost(current_cost, M.intersections[current_intersection], M.intersections[route],
                               M.intersections[goal]), path))

    heapq.heapify(minHeap)
    return heapq.heappop(minHeap)[1]


def route_cost(prevous_cost, current_intersection, next_intersection, goal_intersection):
    return prevous_cost + calculate_route_cost(current_intersection, next_intersection) + calculate_route_cost(
        next_intersection, goal_intersection)


from queue import PriorityQueue

# Optimized attempt
def shortest_path2(M, start, goal):
    print("shortest path called")
    if start == goal:
        return [start]

    path_queue = PriorityQueue()
    path_queue.put(start, 0)

    previous_intersections_map = {start: None}
    intersections_costs_map = {start: 0}

    while not path_queue.empty():
        current_intersection = path_queue.get()

        for next_intersection in M.roads[current_intersection]:
            new_route_cost = intersections_costs_map[current_intersection] + calculate_route_cost(
                M.intersections[current_intersection], M.intersections[next_intersection])

            if next_intersection not in intersections_costs_map or new_route_cost < intersections_costs_map[
                next_intersection]:
                intersections_costs_map[next_intersection] = new_route_cost
                total_route_cost = new_route_cost + calculate_route_cost(M.intersections[current_intersection],
                                                                         M.intersections[next_intersection])
                path_queue.put(next_intersection, total_route_cost)
                previous_intersections_map[next_intersection] = current_intersection

    # creating path...
    current_intersection = goal
    path = [current_intersection]
    while current_intersection is not None:
        current_intersection = previous_intersections_map[current_intersection]
        path.append(current_intersection)
    path.reverse()
    return path


def calculate_route_cost(intersections1, intersections2):
    return math.sqrt((intersections2[0] - intersections1[0]) ** 2 + (intersections2[1] - intersections1[1]) ** 2)
