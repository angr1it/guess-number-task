import math


def calcArcLength(radius: float, angle: float) -> float:
    return radius * angle


def calcAngle(first: tuple, second: tuple) -> float:
    angle = math.atan2(first[1], first[0]) - math.atan2(second[1], second[0])

    return abs(angle)


def calcRadius(coords: tuple) -> float:
    return math.sqrt(coords[0] ** 2 + coords[1] ** 2)


if __name__ == "__main__":
    nums = tuple(map(int, input().split(" ")))
    assert len(nums) == 4

    first = (nums[0], nums[1])
    second = (nums[2], nums[3])

    r1 = calcRadius(first)
    r2 = calcRadius(second)

    angle = calcAngle(first, second)
    arc = calcArcLength(min(r1, r2), angle)
    diff = abs(r1 - r2)

    result = min(r1 + r2, diff + arc)

    print(f"{result:.12f}")
