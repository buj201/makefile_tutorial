# Chapter 2 -- Variable basics

### Intro:

A variable is a name defined in a makefile to **represent a string of text**, called the variable’s value. These values are substituted by explicit request into targets, prerequisites, recipes, and other parts of the makefile. (In some other versions of make, variables are called macros.) This is called variable "expansion". Variables can represent lists of file names, options to pass to compilers, programs to run, directories to look in for source files, directories to write output in, or anything else you can imagine.

**Key takeaway**: Think of make variables using what you already know about text substitution (I.e: sprintf, python string.format, etc.) 

## Defining and referencing variables

#### Defining variables -- two flavors:

There are two ways that a variable in GNU make can have a value; we call them the two flavors of variables. The two flavors are distinguished in how they are defined and in what they do when expanded. For **simply expanded variables**, the RHS is expanded when the variable is defined. For **recursively expanded variables**, the RHS is expanded when the variable is called.

### Exploration 

1. Look at the makefile.
2. Run `make first_example` to see the first example of variable definition and use.
3. Recall that '=' defines a variable recursively, such that the RHS is only expanded when the variable is called. Predict what `make recursively_expanded_example` will print. Then run it. 
4. Recall that ':=' defines a variable simply, such that the RHS is expanded when the variable is defined. Predict what `make simpy_expanded_example` will print. Then run it. 
5. Note we can append to a variable using '+='. Run `append_example` to see this in action.
