QUESTION

We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

  {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
  
Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed 
(here they are 'match1','match2','match3'), nor are the names of the players. A player need not have a score recorded in all matches.

Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. 
Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score,
and topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total score.

For instance:

  >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)

  >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)


PROGRAM/SOLUTION

def orangecap(d):
    total = {}
    for n in d.keys():
        for i in d[n].keys():
            total[i] = 0
            for match in d.keys():
                if i in d[match].keys():
                    total[i] = total[i] + d[match][i]
    temp = list(total.values())
    topscore = max(temp)
    for name, score in total.items():
        if score == topscore:
            playername=name
    return (playername,topscore)
    
    
