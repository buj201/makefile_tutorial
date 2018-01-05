# ch2/makefile
# Objective: Understand how make variable expansion works, and
# compare the two flavors of make variables

#########################
# Referencing variables #
#########################

# Variables are referenced using $(VAR). Ex:

VAR = 'hello world'

first_example:
	echo $(VAR)

#####################################
# Defining variables -- two flavors #
#####################################

# Recursively expanded variables are defined by lines using ‘=’.
# The value you specify is installed verbatim; if it contains references to other variables,
# these references are expanded whenever this variable is substituted (in the course of expanding some other string).
# When this happens, it is called recursive expansion.

foo = $(bar)
bar = $(ugh)
ugh = Huh?

recursively_expanded_example:
	echo $(foo)


# Simply expanded variables are defined by lines using ‘:=’
# The value of a simply expanded variable is scanned once and for all, expanding any references to other variables and functions,
# when the variable is defined. The actual value of the simply expanded variable is the result of expanding the text that you write.
# It does not contain any references to other variables; it contains their values as of the time this variable was defined.

x := foo
y := $(x) bar
x := later

simply_expanded_example:
	echo x = $(x)
	echo y = $(y)

###########################
# Appending to variables  #
###########################

# Imagine you have a variable representing a list of files

list = file1 file2 file3

# Appending to this list is easy in make:

list += file4

append_example:
	echo $(list)
