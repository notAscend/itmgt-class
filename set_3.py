#先苦後甜
import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

def relationship_status(from_member, to_member, social_graph):
    social_graph[from_member] #from credentials
    social_graph[to_member] #to credentials
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    cnt = len(board)
    winner = "NO WINNER"
    for row in board:
        if row[0]!="":
            x = True 
            for cell in row:
                if cell!=row[0]: 
                    x = False
                    break
            if x: 
                winner = row[0]
    for col in range(cnt):
        if board[0][col]!="":
            x = True 
            for row in range(cnt):
                if board[row][col] != board[0][col]: 
                    x = False
                    break 
            if x: 
                winner = board[0][col]  
    #diag
    if board[0][0]!="":
        x = True 
        for i in range(cnt):
            if board[i][i]!=board[0][0]:
                x = False
                break 
        if x: winner = board[0][0]
    #opp diag
    if board[0][cnt-1]!="":
        x = True 
        for i in range(cnt):
            if board[i][cnt-i-1]!=board[0][cnt-1]: 
                x = False
                break
        if x: winner = board[0][cnt-1]
    return winner 


def eta(first_stop, second_stop, route_map):
    time = 0
    curr = first_stop
    while curr!=second_stop:
        for (start, end),i in route_map.items():
            if start==curr:
                time+=i["travel_time_mins"]
                curr=end
                break
    return time
  