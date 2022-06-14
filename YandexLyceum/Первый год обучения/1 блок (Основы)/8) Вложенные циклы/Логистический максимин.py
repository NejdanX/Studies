count_road = int(input())
max_height_car = 0
road_number = 0
for i in range(count_road):
    count_tunnel = int(input())
    min_height_tunnel_on_road = 100000
    for j in range(count_tunnel):
        height_tunnel = int(input())
        if(min_height_tunnel_on_road > height_tunnel):
            min_height_tunnel_on_road = height_tunnel
    if(max_height_car < min_height_tunnel_on_road):
        max_height_car = min_height_tunnel_on_road
        road_number = i + 1
print(road_number, max_height_car)