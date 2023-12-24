import heapq


INF = 1e12


class Route:
    def __init__(self, start_village, start_time, end_village, end_time) -> None:
        self.start_village = start_village
        self.start_time = start_time
        self.end_village = end_village
        self.end_time = end_time

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __le__(self, other):
        return self.end_time <= other.end_time


def getAvailableRoute(
    bus_schedule: list[Route], start_village_num, time
) -> list[Route]:
    lst = []
    for bus_route in bus_schedule:
        if (
            bus_route.start_village == start_village_num
            and bus_route.start_time >= time
        ):
            lst.append(bus_route)

    return lst


if __name__ == "__main__":
    N = int(input())
    S, F = tuple(map(int, input().split(" ", 1)))
    R = int(input())
    S -= 1
    F -= 1

    bus_schedule = []
    for _ in range(R):
        a, ta, b, tb = tuple(map(int, input().split(" ", 3)))
        a -= 1
        b -= 1

        bus_schedule.append(Route(a, ta, b, tb))

    dp = [INF for _ in range(N + 1)]
    dp[S] = 0

    pq = []
    [
        heapq.heappush(pq, (route.end_time, route))
        for route in getAvailableRoute(bus_schedule, S, 0)
    ]
    while len(pq) > 0:
        _, current = heapq.heappop(pq)

        if current.end_time < dp[current.end_village]:
            dp[current.end_village] = current.end_time

        if current.start_village == F:
            break

        available = getAvailableRoute(
            bus_schedule, current.end_village, current.end_time
        )
        for x in available:
            heapq.heappush(pq, (x.end_time, x))

    print(-1 if dp[F] == INF else dp[F])
