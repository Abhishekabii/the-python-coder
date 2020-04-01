'''4. Develop a program to calculate the total and individual player scores
in a cricket match. 
Input would be an array with the index representing the ball number
and the value representing the runs scored of that ball.

Assumptions/Tips:
1.	No Extras bowled
2.	Batsman has to be rotated after ever over
3.	Bowler can bowl any number of overs
4.	Assume Batsman 1 is on strike for the first ball.


Below is an example:

Input : [1,2,0,0,4,1,6,2,1,3];

Output:
Total Score: 20
Batsman 1 Score : 4 (1 + 3)
Batsman 2 Score : 16 (2 + 4 + 1 + 6 + 2 + 1)'''





scored=[1,2,0,0,4,1,6,2,1,3]


def swapPositions(my_List): 
      my_List[0], my_List[1] = my_List[1], my_List[0] 
      return my_List



bat1=[]
bat2=[]
batsman = [bat1, bat2]
odd=[1,3,5]
even=[0,2,4,6]

def score_card(scores):
      
      for i in range(1,len(scores)+1):
    
          if scores[i-1] in odd and i%6==0 :
              batsman[0].append(scores[i-1])
   
          elif scores[i-1] in odd:
              batsman[0].append(scores[i-1])
              if i%6!=0 :
                  swapPositions(batsman)
       
          elif scores[i-1] in even and i%6!=0 :
              batsman[0].append(scores[i-1])
    
          elif scores[i-1] in even:
              batsman[0].append(scores[i-1])
              if i%6==0 :
                  swapPositions(batsman)
      
      total_Score=0
      for i in scores:
          total_Score+=i
      print('Total Score :',total_Score)
      print('Batsman 1 Score : ',sum(bat1),[i for i in bat1 if i>0 ])
      print('Batsman 1 Score : ',sum(bat2),[i for i in bat2 if i>0 ])




score_card(scored)
