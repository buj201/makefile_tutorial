# Chapter 4 -- `$(call variable,param,param,...)`

### Intro:

The call function is unique in that it can be used to create new parameterized functions. You can write a complex expression as the value of a variable, then use call to expand it with different values.

The syntax of the call function is:

`$(call variable,param,param,…)`

When make expands this function, it assigns each param to temporary variables `$(1)`, `$(2)`, etc. The variable `$(0)` will contain *variable*. There is no maximum number of parameter arguments. There is no minimum, either, but it doesn’t make sense to use call with no parameters.

Then variable is expanded as a make variable in the context of these temporary assignments. Thus, any reference to `$(1)` in the value of variable will resolve to the first *param* in the invocation of call.

Note that variable is the name of a variable, not a reference to that variable. Therefore you would not normally use a ‘$’ or parentheses when writing it. (You can, however, use a variable reference in the name if you want the name not to be a constant.)

If variable is the name of a built-in function, the built-in function is always invoked (even if a make variable by that name also exists).


### Exploration 

1. Run `make`. Note there are no rules in this makefile -- instead, we're using the helpful `$(info arguments)` function, which simply evaluates the arguments and prints them to standard output, to explore some basic functions.

