PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    user_age = int(input("Enter your age:"))
    
    #PETURKSBOUIPO
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Petruksbouipo where the voting is {PETURKSBOUIPO_AGE}.")
    
    
    #STANLAU
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    

    #MAYENGUA
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == "__main__":
    main()
    
