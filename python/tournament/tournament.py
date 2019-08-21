def tally(rows):
  teams = {}
  for r in rows:
    match = r.split(';')
    #check if teams exist. Add if not
    if match[0] not in teams.keys():
      teams[match[0]] = [0,0,0,0,0]
    if match[1] not in teams.keys():
      teams[match[1]] = [0,0,0,0,0]

    #add tallies for teams
    teams[match[0]][0] += 1
    teams[match[1]][0] += 1

    if match[2] == 'win':
      teams[match[0]][1] += 1
      teams[match[0]][4] += 3
      teams[match[1]][3] += 1

    elif match[2] == 'loss':
      teams[match[0]][3] += 1
      teams[match[1]][1] += 1
      teams[match[1]][4] += 3

    else:
      teams[match[0]][2] += 1
      teams[match[0]][4] += 1
      teams[match[1]][2] += 1
      teams[match[1]][4] += 1

  results = ['Team                           | MP |  W |  D |  L |  P']
  
  sorted_names = sorted(teams, key = lambda x: (-teams[x][4], x))

  for n in sorted_names:
    name_format = '{:<31}|'.format(n)
    mp_format = ' {:^3}|'.format(teams[n][0])
    w_format = ' {:^3}|'.format(teams[n][1])
    d_format = ' {:^3}|'.format(teams[n][2])
    l_format = ' {:^3}|'.format(teams[n][3])
    p_format = '{:>3}'.format(teams[n][4])
    
    team_stats = name_format+mp_format+w_format+d_format+l_format+p_format
    results.append(team_stats)

  return results