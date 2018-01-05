# ch6/makefile1
# Objective: Understand and avoid potential issues with parallelization -- in particular, multiple targets produced by the same recipe.

.PHONY = all clean
.DEFAULT_GOAL: all

all: output/output1.txt output/output2.txt output/output3.txt

output/output1.txt output/output2.txt output/output3.txt:
	python make_outputs.py

clean:
	rm output/output*.txt
