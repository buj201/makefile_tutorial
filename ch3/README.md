# Chapter 3 -- Function Basics

### Intro:

A function call resembles a variable reference. It can appear anywhere a variable reference can appear, and it is expanded using the same rules as variable references. A function call looks like this:

`$(function arguments)`

 Here function is a function name; one of a short list of names that are part of make. The functions built-in to make are documented at https://www.gnu.org/software/make/manual/make.html#Functions.


 The arguments are the arguments of the function. They are separated from the function name by one or more spaces or tabs, and if there is more than one argument, then they are separated by commas. 

### Exploration 

1. Run `make`. Note there are no rules in this makefile -- instead, we're using the helpful `$(info arguments)` function, which simply evaluates the arguments and prints them to standard output, to explore some basic functions.

