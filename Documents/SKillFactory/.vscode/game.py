import numpy as np

number = np.random.randint(1, 101)

"Количество попыток угадывания"

count = 0 

while True:
    count += 1
    predict_number= int(input("Угaдай число от 1 до 100   "))
    print ("Это число", number)
    if predict_number > number:
        print ("число должно быть меньше")
        
    elif predict_number < number:
        print ("Число должно быть больше")
        
    else: 
        print (f"Ты угадал число {number} за {count} попыток")
        break
    
    "228"