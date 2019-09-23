weight = float(input("What is your weight on Kg?"))
height = float(input("What is your height in m?"))
IMC = weight/(height**2)
if IMC <= 18.5:
    print("Your body mass index is ", IMC, ", it is lower than normal.")
elif IMC > 18.5 and IMC < 25:
    print("Your body mass index is ", IMC, ", it is normal.")
elif IMC >= 25 and IMC < 29.9:
    print("Your body mass index is ", IMC, ", it is higher than normal.")
elif IMC >= 29.9:
    print("Your body mass index is ", IMC, ", you have obesity")
