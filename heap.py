import heapq

def min_cost_for_cables(cables):
    
    if not cables:
        return 0
    
    
    heapq.heapify(cables)
    total_min_cost = 0


    while len(cables) > 1:

        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)


        cost = first_cable + second_cable
        total_min_cost +=cost


        heapq.heappush(cables,cost)
        print("Після додавання",cables)

    return total_min_cost

if __name__ == "__main__":
    cables =[19,5,5,3,1]


print("Мінімальні витрати на об'єднання кабелів:", min_cost_for_cables(cables))
