# Seedgen

Seeding algorithm to generate new random numbers

- Credits to @fermatslibrary on https://twitter.com/fermatslibrary/status/1667517252768333825/photo/1
- Define the length of your random number (n) and how many number you want to generate (k)
- Algorithm will generate k random numbers from a root number following the following algorithm

1. Start with a seed number of length n
2. Square the number
3. Extract the middle n numbers, this is the new seed
4. Repeat the process
