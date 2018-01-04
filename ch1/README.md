# Chapter 1 -- Make Basics

### Intro:

The real value of make/makefiles is avoiding unnecessarily rerunning programs to build output files. Make keeps track of the last time files were updated and only updates those files which are out-of-date. If you have a large project with many tasks (steps with intermediate input/output files), when you change a file on which others depend, you must rebuild all the dependent outputs. Without a makefile, this is an extremely time-consuming task. 

### Exploration 

1. Run `make`. Which order are the recipes executed? Why?
2. Run `touch file2`. Then run `ls --full-time`. Notice the modification times of each file. Which targets will be rebuilt when we next run make?
3. Run `make` to confirm.

