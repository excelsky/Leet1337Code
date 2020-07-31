def l7(datelink, rollups):
    ans = {key: [] for key in rollups}
    for key, value in rollups.items():
        if len(value) == 2:
            ans[key] = [max(i) for i in zip(datelink[value[0]], datelink[value[1]])]
        else:
            ans[key] = [max(i) for i in zip(datelink[value[0]], datelink[value[1]], datelink[value[2]])]
    return ans



datelink = {"ios": [1,0,0,1,0,0,1]
      , "android": [0,1,0,1,1,0,1]
          , "web": [1,0,1,0,1,0,1]}

rollups = {"overall": ["ios", "android", "web"]
          , "mobile": ["ios", "android"]}



output = {"overall": [1,1,1,1,1,0,1]
         , "mobile": [1,1,0,1,1,0,1]}

assert l7(datelink, rollups) == output