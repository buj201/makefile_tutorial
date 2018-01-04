# ch5/makefile
# Objective: Understand the $(foreach ...) and $(eval ...) functions.

# $(foreach var,list,text)
#	Make first examples var and list, setting var to the first
#   word in the the expanded list.
#   Then it expands text, which presumably references $(var),

# $(eval expression)
#   The argument to the eval function is expanded, then the
#   results of that expansion are parsed as makefile syntax.
#	The expanded results can define new make variables, targets,
#   rules, etc.

#####################################
# Note this section uses skills and #
# concepts we've seen in previous   #
# section -- it's review            #
#####################################

# Create a recursively expanded variable listing string model names.
list = model1 model2 model3

# Create user defined functions for generating input and output filenames.
# They use two new string functions -- addprefix and addsuffix.

input_name = $(addsuffix .csv,$(addprefix input/,$(1)))
output_name = $(addsuffix .csv,$(addprefix output/,$(1)))

# Instantiate an empty list of targets

target_list :=

# Create a multiline variable that (i) generates a makefile rule
# and (ii) appends to the empty list of targets

define rule_template
$(call output_name,$(1)): $(call input_name,$(1)) main.py
	python main.py \
		   --input=$(call input_name,$(1)) \
		   --output=$(call output_name,$(1))

target_list += $(call output_name,$(1))
endef

########################
# This is new material #
########################

#####################
# foreach example 1 #
#####################

# Here's a simple example of foreach, calling input_name. Note
# the $(call ...) is wrapped in info to print to stdout.

$(info ---------------------------) # Hack to get divider
$(info Example1 -- foreach)
$(info ---------------------------) # Hack to get divider
$(foreach model,$(list),$(info $(call input_name,$(model))))

############################
# foreach + eval example 2 #
############################


# In this example, we use eval to expand rule_template for each
# item in "list". Since rule_template is a multiline variable
# containing $(1), it is best understood as a function with one
# positional argument.

# To make it easier to understand what is happening, we first
# call info, which just expandes the $(call ...) and prints to
# stdout.

$(info ---------------------------) # Hack to get divider
$(info Example2 -- foreach + eval, using info to explain)
$(info ---------------------------) # Hack to get divider

$(foreach model,$(list),$(info $(call rule_template,$(model))))
$(info ) # Hack to get newline

# Then we call eval, to actually expand into makefile syntax
# which is evaluated by make.

$(foreach model,$(list),$(eval $(call rule_template,$(model))))

########################
# Define default goal  #
########################


$(info ---------------------------) # Hack to get divider
$(info Actual execution of recipes)
$(info ---------------------------) # Hack to get divider

.DEFAULT_GOAL = all

all: $(target_list)

