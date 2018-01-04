# ch6/makefile
# Objective: Find basic makefile functions in docs

# Make supports a number of functions for text/filename manipulation.
# The function call syntax is $(function arguments)
# For example, the $(info ...) function simply prints its arguments
# to standard output:

$(info example function call)

# This function is useful for debugging (and examples).
# To illustrate other functions, we'll wrap them in $(info $(function arguments))

############################
# Example string functions #
############################

# $(subst from,to,text)
# 	Replace from with to in text.
# 	Note there is also a basic pattern substitution function, patsubst,
#   which uses % as a wildcard.

subst_example = hello world!
$(info $(subst world,CLNY,$(subst_example)))

# $(firstword names...)
#	The argument names is regarded as a series of names, separated by whitespace.
#	The value is the first name in the series.
#	The rest of the names are ignored.
list = word1 word2 word3
$(info $(firstword $(list)))

##############################
# Example filename functions #
##############################

# $(dir names…)
#   Extracts the directory-part of each file name in names.
#	The directory-part of the file name is everything up through (and including)
#	the last slash in it. If the file name contains no slash, the directory part
#	is the string ‘./’.

$(info $(dir input/raw_data.csv makefile))

# $(basename names…)
#   Extracts all but the suffix of each file name in names.
#	If the file name contains a period, the basename is everything starting up to (and not including)
#	the last period. Periods in the directory part are ignored.
#	 If there is no period, the basename is the entire file name.

$(info $(basename input/raw_data.csv makefile))

# There are many others -- the basic idea is that you can use these built-in
# functions to easily manipulate filenames.
