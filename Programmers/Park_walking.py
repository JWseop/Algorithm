# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# Lv.1
# 문제: 공원 걷기

def find_start_point(park):
    for h, row in enumerate(park):
        for w, cell in enumerate(row):
            if cell == 'S':
                return h, w

def is_valid_position(park, h, w):
    H, W = len(park), len(park[0])
    if 0 <= h < H and 0 <= w < W and park[h][w] != 'X':
        return True
    return False

def can_move(park, current_h, current_w, dh, dw, movement):
    for _ in range(movement):
        current_h, current_w = current_h + dh, current_w + dw
        if not is_valid_position(park, current_h, current_w):
            return False
    return True

def solution(park, routes):
    H, W = len(park), len(park[0])
    direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    current_h, current_w = find_start_point(park)

    for route in routes:
        d, movement = route[0], int(route[2:])
        dh, dw = direction[d]

        if can_move(park, current_h, current_w, dh, dw, movement):
            current_h, current_w = current_h + dh * movement, current_w + dw * movement

    return [current_h, current_w]