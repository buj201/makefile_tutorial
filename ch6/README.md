# Chapter 6 -- Potential issues with data analytic makefiles

### Make with multiple targets:

Data analysis scripts often produce more than one output -- while this can be viewed as problematic (i.e. failing to do one thing), it is common, as an analyst might avoid IO costs of loading large data sets multiple times if they're (for example) just producing a couple of summary statistics or crosstabs.

When thinking about rules with multiple targets, note make actually parses the following equivalently:


```
target1 target2: input1
   run_something
```

and

```
target1: input1
   run_something

target2: input1
   run_something
```

As such, here are a couple of traps you can fall into when multiple outputs are built on the same prerequisites and recipes.

##### Sequential vs. parallel execution

By default, `make` runs recipes for out-of-date targets sequentially. This both (a) makes recipes with multiple outputs run once (since the are all updated the first time the recipe is executed), but also makes the makefile brittle (in the sense that other users might run `make` in parallel).

##### Exploration

1. Run `make --just-print` to see the recipes to be executed. Note the dependency graph requires all three targets be updated, so the recipe prints three times.
2. Now run `make` -- the recipe is only run once, since all three outputs are updated the first time.
3. Now run `make clean` to remove the output files.
4. Now rerun `make` in parallel, with `make -f makefile1 -j3` (three jobs). Note the difference between parallel and sequential execution.

Note this implies a tradeoff: ignoring all but one output of an analysis script allows for easy parallelization, breaks the workflow graph. Note *you can enforce sequential runs using the target `.NOTPARALLEL`, but it applies to the entire makefile*.

