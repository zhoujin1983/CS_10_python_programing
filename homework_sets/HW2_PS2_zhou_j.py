#Jin Zhou
#1091825
#Homework 2 Program Set 2
#This program compares the federal income input by the user by using the progressive tax system

#input income
income = int(input("Enter income as an integer with no commas: "))

#processing/caculation and output
while income!=-1:
    if 0<=income<=9325:
        tax_17 = income * .10
    elif 9326<=income<=37950:
        tax_17 = 9325*0.1+(income-9325)*0.15
    elif 37951<=income<=91900:
        tax_17 = 9325*0.1+(37950-9325)*0.15+(income-37950)*0.25
    elif 91901<=income<=191650:
        tax_17 = 9325*0.1+(37950-9325)*0.15+(91900-37950)*0.25+(income-91900)*0.28
    elif 191651<=income<=416700:
        tax_17 = 9325*0.1+(37950-9325)*0.15+(91900-37950)*0.25+(191650-91900)*0.28+(income-191650)*0.33
    elif 416701<=income<=418400:
        tax_17 = 9325*0.1+(37950-9325)*0.15+(91900-37950)*0.25+(191650-91900)*0.28+(416700-191650)*0.33+(income-416700)*0.35
    else:
        tax_17 = 9325*0.1+(37950-9325)*0.15+(91900-37950)*0.25+(191650-91900)*0.28+(416700-191650)*0.33+(418400-416700)*0.35+(income-418400)*0.396


    if 0<=income<=9525:
        tax_18 = income * .10
    elif 9526<=income<=38700:
        tax_18 = 9525*0.1+(income-9525)*0.12
    elif 38701<=income<=82500:
        tax_18 = 9525*0.1+(38700-9525)*0.12+(income-38700)*0.22
    elif 82501<=income<=157500:
        tax_18 = 9525*0.1+(38700-9525)*0.12+(82500-38700)*0.22+(income-82500)*0.24
    elif 157501<=income<=200000:
        tax_18 = 9525*0.1+(38700-9525)*0.12+(82500-38700)*0.22+(157500-82500)*0.24+(income-157500)*0.32
    elif 200001<=income<=500000:
        tax_18 = 9525*0.1+(38700-9525)*0.12+(82500-38700)*0.22+(157500-82500)*0.24+(200000-157500)*0.32+(income-200000)*0.35
    else:
        tax_18 = 9525*0.1+(38700-9525)*0.12+(82500-38700)*0.22+(157500-82500)*0.24+(200000-157500)*0.32+(500000-200000)*0.35+(income-500000)*0.37
        
    dif = tax_18 - tax_17
    percent = abs(dif/tax_17)*100
    print("Income:",format(income,'.2f'))
    print("2017 tax:", format(tax_17,'.2f'))
    print("2018 tax:", format(tax_18,'.2f'))
    print("Difference:", format(dif,'.2f'))
    print("Difference (percent):", format(percent,'.2f'))
    print(" ")
    income = int(input("Enter income as an integer with no commas: "))


##Test run 1    
##Enter income as an integer with no commas: 8000
##Income: 8000.00
##2017 tax: 800.00
##2018 tax: 800.00
##Difference: 0.00
##Difference (percent): 0.00
## 
##Enter income as an integer with no commas: 15000
##Income: 15000.00
##2017 tax: 1783.75
##2018 tax: 1609.50
##Difference: -174.25
##Difference (percent): 9.77
## 
##Enter income as an integer with no commas: 40000
##Income: 40000.00
##2017 tax: 5738.75
##2018 tax: 4739.50
##Difference: -999.25
##Difference (percent): 17.41
## 
##Enter income as an integer with no commas: 100000
##Income: 100000.00
##2017 tax: 20981.75
##2018 tax: 18289.50
##Difference: -2692.25
##Difference (percent): 12.83
## 
##Enter income as an integer with no commas: 200000
##Income: 200000.00
##2017 tax: 49399.25
##2018 tax: 45689.50
##Difference: -3709.75
##Difference (percent): 7.51
## 
##Enter income as an integer with no commas: 500000
##Income: 500000.00
##2017 tax: 153818.85
##2018 tax: 150689.50
##Difference: -3129.35
##Difference (percent): 2.03
## 
##Enter income as an integer with no commas: 1000000
##Income: 1000000.00
##2017 tax: 351818.85
##2018 tax: 335689.50
##Difference: -16129.35
##Difference (percent): 4.58
## 
##Enter income as an integer with no commas: 10000000
##Income: 10000000.00
##2017 tax: 3915818.85
##2018 tax: 3665689.50
##Difference: -250129.35
##Difference (percent): 6.39
## 
##Enter income as an integer with no commas: -1
##>>> 


##Test run 2
##Enter income as an integer with no commas: -1
##>>> 


##Test run 3
##Enter income as an integer with no commas: 9600
##Income: 9600.00
##2017 tax: 973.75
##2018 tax: 961.50
##Difference: -12.25
##Difference (percent): 1.26
## 
##Enter income as an integer with no commas: 10500
##Income: 10500.00
##2017 tax: 1108.75
##2018 tax: 1069.50
##Difference: -39.25
##Difference (percent): 3.54
## 
##Enter income as an integer with no commas: 150655
##Income: 150655.00
##2017 tax: 35165.15
##2018 tax: 30446.70
##Difference: -4718.45
##Difference (percent): 13.42
## 
##Enter income as an integer with no commas: 2476250
##Income: 2476250.00
##2017 tax: 936413.85
##2018 tax: 881902.00
##Difference: -54511.85
##Difference (percent): 5.82
## 
##Enter income as an integer with no commas: 487532
##Income: 487532.00
##2017 tax: 148881.52
##2018 tax: 146325.70
##Difference: -2555.82
##Difference (percent): 1.72
## 
##Enter income as an integer with no commas: -1
##>>> 

##Test run 4
##Enter income as an integer with no commas: 56897
##Income: 56897.00
##2017 tax: 9963.00
##2018 tax: 8456.84
##Difference: -1506.16
##Difference (percent): 15.12
## 
##Enter income as an integer with no commas: 126785
##Income: 126785.00
##2017 tax: 28481.55
##2018 tax: 24717.90
##Difference: -3763.65
##Difference (percent): 13.21
## 
##Enter income as an integer with no commas: 4215890
##Income: 4215890.00
##2017 tax: 1625311.29
##2018 tax: 1525568.80
##Difference: -99742.49
##Difference (percent): 6.14
## 
##Enter income as an integer with no commas: 125486031
##Income: 125486031.00
##2017 tax: 49648287.13
##2018 tax: 46395520.97
##Difference: -3252766.16
##Difference (percent): 6.55
## 
##Enter income as an integer with no commas: -1
##>>> 


##Test run 5
##Enter income as an integer with no commas: 3684
##Income: 3684.00
##2017 tax: 368.40
##2018 tax: 368.40
##Difference: 0.00
##Difference (percent): 0.00
## 
##Enter income as an integer with no commas: 52489
##Income: 52489.00
##2017 tax: 8861.00
##2018 tax: 7487.08
##Difference: -1373.92
##Difference (percent): 15.51
## 
##Enter income as an integer with no commas: 1238569
##Income: 1238569.00
##2017 tax: 446292.17
##2018 tax: 423960.03
##Difference: -22332.14
##Difference (percent): 5.00
## 
##Enter income as an integer with no commas: 9845723
##Income: 9845723.00
##2017 tax: 3854725.16
##2018 tax: 3608607.01
##Difference: -246118.15
##Difference (percent): 6.38
## 
##Enter income as an integer with no commas: 2584361
##Income: 2584361.00
##2017 tax: 979225.81
##2018 tax: 921903.07
##Difference: -57322.74
##Difference (percent): 5.85
## 
##Enter income as an integer with no commas: -1
##>>> 
