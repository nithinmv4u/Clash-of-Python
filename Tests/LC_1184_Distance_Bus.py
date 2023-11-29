from typing import List

def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
    clockwise=0
    anticlockwise=0
    if start>destination:
        clock=distance[start:]+distance[:destination]
        anticlock=distance[destination:start]
    else:
        clock=distance[start:destination]
        anticlock=distance[destination:]+distance[:start]
    print(clock,anticlock)
    for i in range(len(clock)):
        clockwise=clockwise+clock[i]
    for i in range(len(anticlock)):
        anticlockwise=anticlockwise+anticlock[i]
    if clockwise<=anticlockwise:
        return clockwise
    else:
        return anticlockwise

distance=[1,2,3,4]
start=3
destination=1
result=distanceBetweenBusStops(distance,start,destination)
print(result)