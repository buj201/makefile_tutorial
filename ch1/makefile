# ch1/makefile
# Objective: Describe the basic structure of a rule, and understand how make constructs
#   a dependency graph based on mtimes

# Running 'make' from the CL will run either (i) .DEFAULT_GOAL (if set) or the first target
# if .DEFAULT_GOAL is not set.

.DEFAULT_GOAL = all

all: file3

# Basic makefiles have the structure
# target: prerequisites ...
#     recipe 


file3: file2
	echo 'Updating file3'

file2: file1
	echo 'Updating file2'

file1:
	echo 'Updating file1'