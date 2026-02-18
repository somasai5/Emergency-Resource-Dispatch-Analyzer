Zone = input("Enter the name of the Zone :")
n = int(input("Enter the number of the resources :"))
resourceRequests = []
print("Enter the integers representing resources :")
for i in range(n):
    resourceRequests +=[int(input())]

low_Demand = []
moderate_Demand = []
high_Demand = []
invalid_requests = []

totalValid=0
totalNoDemand=0
personalization=0
totalInvalid=0

for resource in resourceRequests:
    if resource>50:
        high_Demand += [resource]
        totalValid = totalValid + 1
    elif resource>20:
        moderate_Demand += [resource]
        totalValid = totalValid + 1
    elif resource>0:
        low_Demand += [resource]
        totalValid = totalValid + 1
    elif resource<0:
        invalid_requests = invalid_requests + [resource]
        totalInvalid = totalInvalid+1
    else:
        totalNoDemand += 1

print("\nLow Demand :",low_Demand)
print("Moderate Demand :",moderate_Demand)
print("High Demand :",high_Demand)
print("Invalid Requests :",invalid_requests)

L = len(Zone.replace(" ", ""))
PLI = L%4

if PLI == 1:
    personalization = len(low_Demand)
    low_Demand = []
elif PLI == 2:
    personalization = len(moderate_Demand)
    moderate_Demand = []
elif PLI == 3:
    personalization = len(high_Demand)
    high_Demand = []
else:
    personalization = len(invalid_requests)
    invalid_requests = []


print("\n After personalization :")
print("low Demand :",low_Demand)
print("moderate Demand :",moderate_Demand)
print("high Demand :",high_Demand)
print("critical Demand :",invalid_requests)

print("\nTotal valid :",totalValid)
print("Total ignored :",totalNoDemand)
print("Total invalid :",totalInvalid)
print("Removed due to personalization :",personalization)

