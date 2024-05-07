from time import time
import math

start=time()

word="Artificial Interligence"
text=word.split()
a=" "
for i in text:
    a=a+str(i[0].upper())
print(a)


end=time()


# mesuring excution time
end=time()
excution_time=end-start
exact_execution_time=abs(excution_time)

print(f"Execution time is  {excution_time}")
print("Exact time is ",exact_execution_time)