# ch4/makefile
# Objective: Use $(call) to create new, user-defined functions

#########################################
# Example 1: Using single line variable #
#########################################

reverse = $(2) $(1)

return = $(call reverse,first,second)

$(info $(return))

#######################################
# Example 2: Using multiline variable #
#######################################

# Note here we introduce multiline variables.
# Previously, we've used single line variables
# defined using "=" and ":="
# To define multi-line varibles, use define/endef
# Note you can use the assignment operators "=" and ":="
# after "define <var_name>", but they are optional.
# If you don't include them, make implicitly uses "="
# (i.e. recursively expanded variable assignment).

define multiline_var
inner_first = $(1)
inner_second = $(2)
endef

$(info $(call multiline_var,first,second))
