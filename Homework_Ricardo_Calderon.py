# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:11:34 2017

@author: rcalde1
"""

# The Black Scholes Formula
# This program calculated the value of an European call and put
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility

import sys
import math
from scipy.stats import norm

while True:

    print("This program calculates the price of an European call and put")
    try:
        K = input("What is the strike? ")
    except EOFError:
        sys.exit(1)

    try:
        K = float(K)
    except ValueError:
        print("Sorry,",K, "is not a number.")
        sys.exit(1)

    try:
        S = input("What is the spot? ")
    except EOFError:
        sys.exit(1)

    try:
        S = float(S)
    except ValueError:
        print("Sorry,", S, "is not a number.")
        sys.exit(1)

    try:
        T = input("Time to maturity in years? ")
    except EOFError:
        sys.exit(1)

    try:
        T = float(T)
    except ValueError:
        print("Sorry,", T, "is not a number.")
        sys.exit(1)

    try:
        r = input("What is the risk free rate? ")
    except EOFError:
        sys.exit(1)

    try:
        r = float(r)
    except ValueError:
        print("Sorry,", r, "is not a number.")
        sys.exit(1)

    try:
        v = input("What is the volatility? ")
    except EOFError:
        sys.exit(1)

    try:
        v = float(v)
    except ValueError:
        print("Sorry,", v, "is not a number.")
        sys.exit(1)

    try:
        d = input("What is the dividend? ")
    except EOFError:
        sys.exit(1)

    try:
        d = float(d)
    except ValueError:
        print("Sorry,", r, "is not a number.")
        sys.exit(1)
                   
    d1 = (((math.log((S)/K))+(((r-d)+v*v/2.)*T)))/(v*math.sqrt(T))
    d2 = d1-v*math.sqrt(T)
    call = (S*(math.exp((-d*T)))*norm.cdf(d1))-(K*(math.exp((-r*T)))*norm.cdf(d2))
    put = (K*(math.exp((-r*T)))*norm.cdf(d1))-(S*(math.exp((-d*T)))*norm.cdf(d2))

    print("The call price is $ ", round(call,2), " and the put price is $",
        round(put,2), sep = "")

    print() #Skip a line (i.e., output one newline character and nothing else).


sys.exit(0)