# Chapter 1 -- Make Basics

### Intro:

Make/makefiles are useful for data science for two primary reasons:

1. Avoiding unnecessarily rerunning programs to build output files. Make keeps track of the last time files were updated and only updates those files which are out-of-date, thus helping avoid unnecessarily rebuilding intermediate files that are up-to-date.
2. Reproducibility: If you have a large project with many tasks (i.e. intermediate steps with input/output files), when you change a file on which others depend, you must rebuild all the dependent outputs. Without a makefile, this is an extremely time-consuming task, and prone to error. Make also allows other users to rerun your analyses by providing a high-level hook (`make all` from the project root).

To introduce make, this chapter and the remaining chapters include example makefiles and exploration questions intended to highlight some of the main features of make/makefiles. The instructions for each exploration section assume you're comfortable on the command line, and commands are run in the chapter directory (so, for example, the first command you run in this chapter should be `make` run in the `.../make_tutorial/ch1/` directory).

### Exploration

1. Run `make`. Which order are the recipes executed? Why?
2. Run `touch file2`. Then run `ls --full-time`. Notice the modification times of each file. Which targets will be rebuilt when we next run make?
3. Run `make` to confirm.

