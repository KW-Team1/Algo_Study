num1 = input()
num2 = input()

output1 = int(num1) * (int(num2) % 10)
output2 = int(num1) * int(((int(num2) % 100) / 10))
output3 = int(num1) * int(((int(num2) % 1000) / 100))

output4 = output1 + (output2 * 10) + (output3 * 100)

print(output1)
print(output2)
print(output3)
print(output4)