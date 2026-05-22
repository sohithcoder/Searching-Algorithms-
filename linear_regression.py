#indep :
x_data = [1,2,3,4,5]
#dep :
y_data = [2,4,5,4,5]

def calculate_mean(data):
    return sum(data)/len(data)

x_mean = calculate_mean(x_data)
y_mean = calculate_mean(y_data)

num = 0
den = 0

for i in range(len(x_data)):
    x_diff = x_data[i]-x_mean
    y_diff = y_data[i]-y_mean

    num += x_diff*y_diff
    den += x_diff**2
m = num/den

c = y_mean - (m*x_mean)

def predict(inp):
    return (m*inp)+c
xp = 6
result = predict(xp)
print(result)
#simple linear
#multiple linear
#polynomial
#logistic(bridge)
#non linear(multilayer perception)
