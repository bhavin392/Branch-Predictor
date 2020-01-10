# Branch-Predictor
Various branch predictors are implemented to demonstrate their output readings. This simulator provides the misprediction done by different branch predictor on different trace files

It contains predictors:
1) One Level Branch Predictor:- 1Level.py
2) Two Level Global Branch Predictor:- global.py
3) Two Level Gshare Branch Predictor :- gshare.py
4) Two Level Local Branch Predictor:- local.py
5) Two Level Hybrid Branch Predictor:- hybrid.py
6) N-bit Gshare Branch Predictor:- nbitgshare.py
7) N-bit Local Branch Predictor:- nbitlocal.py

N-bit means the program takes input from users to determine number of levels

To run the n bit python file: Type " python filename numberOfLevels
For eg: python nbitgshare.py 4
