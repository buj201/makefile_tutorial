# ch5/makefile
# Objective: Understand the $(foreach ...) function.

# $(foreach var,list,text)
#	Make first examples var and list, setting var to the first
#   word in the the expanded list.
#   THen it expands text, which presumably references $(var),

#####################################
# Note this section uses skills and #
# concepts we've seen in previous   #
# section -- it's review            #
#####################################

# Here's our example list variable
list = model1 model2 model3

# These are user defined functions for generating input
# and output filenames.
# They use two new string functions -- addprefix and addsuffix.

input_name = $(addsuffix .csv,$(addprefix input_, $(1)))
output_name = $(addsuffix .csv,$(addprefix ouput_, $(1)))

# Here's a multiline variable that generates a rule!

define rule_template = 
$(call output_name,$(1)): $(call input_name,$(1)) main.py
	python main.py \
		   --input=$(call input_name,$(1)) \
		   --output=$(call output_name,$(1)) \ 
endef

########################
# This is new material #
########################

$(info $(foreach model,$(list), $(call rule_template, $(model)))))
