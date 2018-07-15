import json
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
    

def parse_file(file_name):
    
    history = {}

    with open (file_name) as file:
        
        for line in file:
            parser = line.rstrip("\n").split(",")
            name = parser[1]

            if name in history:
                history[name].append({
                    "date": parser[0],
                    "weight": parser[2] 
                })
            else:
                history[name] = [{
                    "date": parser[0],
                    "weight": parser[2] 
                }]

    for name in history:
        x = []
        y = []
        for workout in history[name]:
            x.append(workout["date"])
            y.append(workout["weight"])

        plt.plot(x, y, label=name)

    plt.legend(loc=1)
    plt.ylabel('Weight')
    plt.xlabel('Date')
    plt.savefig("workout.png")
    plt.show()



