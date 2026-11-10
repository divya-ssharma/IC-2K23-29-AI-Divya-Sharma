# Lab 4

Name: Divya Sharma  
Roll No: IC-2K23-29

This lab implements two forms of knowledge representation: a rule based system and a semantic network.

The rule based program accepts symptoms one at a time and then performs forward chaining over a small set of rules. Starting from the given facts, it checks every rule, adds any new conclusion that follows, and repeats until no further facts can be inferred. For example, fever and cough together infer flu, which in turn infers rest.

The semantic network is stored as a nested dictionary with Student, Course and Faculty as nodes. Each node lists its relations to the others, and the program prints them out one by one. An additional Institute node was planned but not completed in this submission.
