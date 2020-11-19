# Car_Price_EDA

1. In each segment mechanics transmission gives better mileage than auto transmission 
2. small segments cars gives less mileage compared to large segment one 
3.In case of fully executive and executive cars, executive cars have better avg mileage
4.Looks like Auto transmission car need large tanks of fuel. S segment and F segment car need large tanks
5.People prefer to use petrol as fuel over diesel But for M segment mechanics transmission people prefer diesel
6.after 2007 almost every segment price has increased Executive, Fully executive , sports,J-segment has increased exponentially

Made Function to get segment missing value
function to get missing value

def segment(i,vol, price):       
            
    if vol[i] < 1.3 and price[i] < 34000:
        return 'A'
    elif vol[i] >= 1.3 and vol[i] <= 1.4 and price[i] < 25000:
        return 'B'
        
    elif vol[i] > 1.4 and vol[i] <= 1.6 and price[i] < 41000:
        return 'C'
    elif vol[i] > 1.6 and vol[i] < 2 and price[i]  < 55000:
        return 'D'
    
    elif vol[i] >= 2 and vol[i] < 2.5 and price[i]  < 82000:
        return 'E'
    elif vol[i] > 3 and vol[i] <= 3.7 and price[i]  < 110000:
        return 'F'
    elif vol[i] > 2.3 and vol[i] < 3 and price[i]  < 170000:
        return 'J'
    elif vol[i] > 1.8 and vol[i] < 2.1 and price[i]  < 51000:
        return 'M'
    elif vol[i] > 3.3 and price[i]  < 120000:
        return 'S'
     
     
   1.LabelBinaraizer works better than one hot encoder
   2. randomforest baseline model worked best, i tried tuning accuracy did not improve much
