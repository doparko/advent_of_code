# Day 11 Seating on the Ferry

#############################################

def part1_status(map, row, seat, r, s):
  num_rows = len(map)
  if (r < 0 or r > (len(map)-1) or s < 0 or s > (len(map[0])-1)):
    return(0)
  elif map[r][s] == 'L' or map[r][s] == '.':
    return(0)
  else:    
    return(1)

#############################################

def status(map, row, seat, dir_r, dir_s):
  num_rows = len(map)
  if (dir_r < 0 or dir_r > (len(map)-1) or dir_s < 0 or dir_s > (len(map[0])-1)):
    return(0)

  else:
    if map[dir_r][dir_s] == 'L':
      return(0)
    elif map[dir_r][dir_s] == '#':
      return(1)
    inc_r = dir_r - row
    inc_s = dir_s - seat
    while map[dir_r][dir_s] == '.':
      dir_r += inc_r
      dir_s += inc_s
      if (dir_r < 0 or dir_r > (len(map)-1) or dir_s < 0 or dir_s > (len(map[0])-1)):
        return(0)
      if map[dir_r][dir_s] == 'L':
        return(0)
      elif map[dir_r][dir_s] == '#':
        return(1)

#############################################

def occupied_adjacent(map, row, seat):
  num_occupied = 0
  for r in range (row-1, row+2):
    for s in range (seat-1, seat+2):
      if (s == seat and r == row):
        continue 
      num_occupied += status(map, row, seat, r, s)  # For Part 1, call part1_status; for Part 2, call status.
  return(num_occupied)

#############################################

def get_new_map(map):
  new_map = []
  for row in range(0, len(map)):
    new_map.append("")
    for seat in range(0, len(map[row])):
      next_status = map[row][seat]
      if next_status == '.':
        new_map[row] += next_status
        continue
      if map[row][seat] == 'L':
        if occupied_adjacent(map, row, seat) == 0:
          next_status = "#"
      else:
        if occupied_adjacent(map, row, seat) >= 5:  # For Part 1, this is 4; for Part 2, this is 5.
          next_status = "L"
      new_map[row] += next_status

  return(new_map)

#############################################

def print_map(map):
  for row in map:
    print(row)
  print("\n")

#############################################

def different(map1, map2):
  for i in range (len(map1)):
    for j in range (len(map1[0])):
      if (map1[i][j] != map2[i][j]):
        return(True)
  return(False)

#############################################

def find_seats(map):
  new_map = get_new_map(map)
  while (different(map, new_map)):
    map = new_map
    new_map = get_new_map(map)

  total_occupied_seats = 0  
  for row in range(len(map)):
    for seat in range(len(map[row])):
      if map[row][seat] == "#":
        total_occupied_seats += 1
  return(total_occupied_seats)

#############################################
filename = '2020_d11.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

#list11 = in11.strip().split('\n')
total_occupied_seats = find_seats(datas)
print(f"Total occupied seats: {total_occupied_seats}.")