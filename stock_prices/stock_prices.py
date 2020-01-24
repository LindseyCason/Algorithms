#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # print(prices[0])
  value=prices[0] #10
  #set current value
  profit=prices[1]-prices[0]
  # print(profit)
  #set first profit
  index=2
  #set where to start
  while len(prices) >index:
    #Until we get to the end of the list
    for i in prices[index-1:]:
      #for every item in prices from 1-end of the array
      if i - value > profit:
        profit = i-value
        # print("profit", profit)
    #if the item  - current set value is larger than profit, reset profit to the new value amount
    value=prices[index-1]
    # print("value",value)
    index=index + 1
    # print(index)
  print(profit)
  return profit

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))