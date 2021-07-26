def color(act_composite, act_english, act_math, c_act_composite, c_act_english, c_act_math, selectivity, yield):
    if selectivity < 15 or yield > 60:
        print('red')
    if act_composite > c_act_composite and act_english > c_act_english and act_math > c_act_math and selectivity > 15 and selectivity < 25:
        print('yellow')
    else:
        print('green')