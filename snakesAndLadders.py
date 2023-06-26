#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:53:09 2022

@author: michalskalsky
"""
import random, pylab

worm_hole = {
  1: 37,
  4: 10,
  9: 22,
  16: -10,
  28: 56,
  37: 6,
  47: -21,
  49: -37,
  51: 17,
  56: -8,
  62: -43,
  64: -4,
  69: 22,
  80: 20,
  87: -63,
  92: -19,
  96: -20,
  98: -19
}


def simulate_snakes(n = 1000):
    rolls_in_trial = []
    min_roll_seq = [1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    for _ in range(n):
        x = 0
        rolls = 0
        min_roll_sequence = []
        while True:
          roll = random.randint(1, 6)
          min_roll_sequence.append(roll)
          rolls += 1
          if x + roll <= 100:
            x += roll
          else:
            continue
          if x  == 80 or x  == 100:
            rolls_in_trial.append(rolls)
            if len(min_roll_sequence) < len(min_roll_seq):
                min_roll_seq = min_roll_sequence
            break
          if x in worm_hole:
            x += worm_hole[x]
    return [rolls_in_trial, min_roll_seq]

if __name__ == "__main__":
    data = simulate_snakes(100000)
    pylab.hist(data[0], bins=100)
    pylab.xlabel('Number of rolls')
    pylab.ylabel('Count')
    pylab.title('Number of rolls to finish game')
    print(f'Average: {sum(data[0])/len(data[0])}, min: {min(data[0])}, max: {max(data[0])}')
    print(f'Shortest path to victory: {data[1]}')
    