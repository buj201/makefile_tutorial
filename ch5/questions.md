# Chapter 4 -- $(foreach ...)

### Intro:

The `foreach` function is very different from other functions. It causes one piece of text to be used repeatedly, each time with a different substitution performed on it. It resembles the for command in the shell `sh`. The syntax of the foreach function is:

`$(foreach var,list,text)`

The first two arguments, *var* and *list*, are expanded before anything else is done; note that the last argument, *text*, is not expanded at the same time. Then for each word of the expanded value of *list*, the variable named by the expanded value of *var* is set to that word, and *text* is expanded. Presumably *text* contains references to that variable, so its expansion will be different each time.

The result is that *text* is expanded as many times as there are whitespace-separated words in list. The multiple expansions of *text* are concatenated, with spaces between them, to make the result of `foreach`.


### Exploration 

1. Run `make`. Note there are no rules in this makefile -- instead, we're using the helpful `$(info arguments)` function, which simply evaluates the arguments and prints them to standard output, to explore some basic functions.

