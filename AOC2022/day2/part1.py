strategy_text = (open("C:/Users/kshar/Documents/python/AOC2022/day2/strategy.txt","r")).read()
strategy_full_data = strategy_text.split("\n")
strategy_data = [row.split() for row in strategy_full_data]

strategy_string_data = ["".join(row) for row in strategy_data]

strategy_scores ={"AX": 4,"AY":8,"AZ": 3,"BX":1,"BY": 5,"BZ": 9,"CX": 7,"CY": 2,"CZ": 6}

my_score = 0
for strategy in strategy_string_data:
    my_score += strategy_scores[strategy]
print("Total score of yours in that Rock-paper-scissor game : ",my_score)   


