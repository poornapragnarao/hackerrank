def minion_game(string):
    # your code goes here
    str_len = len(string)
    winner = ''
    score = stuart_score = kevin_score = 0
    vowels = ['A','E','I','O','U']
    for i,char in enumerate(string):
        if char in vowels:
            kevin_score+=str_len-i
        else:
            stuart_score+=str_len-i
    if stuart_score > kevin_score:
        winner = 'Stuart'
        score = stuart_score
        print(winner, score, sep=' ')
    elif kevin_score > stuart_score:
        winner = 'Kevin'
        score = kevin_score
        print(winner, score, sep=' ')
    else:
        winner = 'Draw'
        score = kevin_score
        print(winner)

    

if __name__ == '__main__':
    s = input()
    minion_game(s)
