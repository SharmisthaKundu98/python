strategy_text = (open("C:/Users/kshar/Documents/python/AOC2022/day2/strategy.txt","r")).read()
strategy_full_data = strategy_text.split("\n")
strategy_data = [row.split() for row in strategy_full_data]
# new_rule = {"X":"lose  0","Y":"draw  3","Z":"win  6"}

strategy_string_data = ["".join(row) for row in strategy_data]

strategy_scores ={"AX": 3,"AY": 1+3,"AZ": 2+6,"BX": 1,"BY": 2+3,"BZ": 3+6,"CX": 2,"CY": 3+3,"CZ": 1+6}

my_score = 0
for strategy in strategy_string_data:
    my_score += strategy_scores[strategy]
print("Total score of yours in that Rock-paper-scissor game : ",my_score)   


