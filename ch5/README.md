# Chapter 5 -- `$(foreach ...)` and `$(eval)`

### foreach:

The `foreach` function is very different from other functions. It causes one piece of text to be used repeatedly, each time with a different substitution performed on it. It resembles the for command in the shell `sh`. The syntax of the foreach function is:

`$(foreach var,list,text)`

The first two arguments, *var* and *list*, are expanded before anything else is done; note that the last argument, *text*, is not expanded at the same time. Then for each word of the expanded value of *list*, the variable named by the expanded value of *var* is set to that word, and *text* is expanded. Presumably *text* contains references to that variable, so its expansion will be different each time.

The result is that *text* is expanded as many times as there are whitespace-separated words in list. The multiple expansions of *text* are concatenated, with spaces between them, to make the result of `foreach`.

### eval:

The `eval` function is very special: it allows you to define new makefile constructs that are not constant; which are the result of evaluating other variables and functions. **The argument to the eval function is expanded, then the results of that expansion are parsed as makefile syntax**. The expanded results can define new make variables, targets, implicit or explicit rules, etc.

The result of the eval function is always the empty string; thus, it can be placed virtually anywhere in a makefile without causing syntax errors.

It’s important to realize that the eval argument is expanded twice; first by the eval function, then the results of that expansion are expanded again when they are parsed as makefile syntax. This means you may need to provide extra levels of escaping for “$” characters when using eval. The value function (see Value Function) can sometimes be useful in these situations, to circumvent unwanted expansions.

**One key application**: `eval` lets you define makefile templates, which you can then expand for each item in a list.

### Exploration

1. Run `make`. Note the section dividers in stdout are intended to divide the sections of the makefile.
2. How are user-defined functions being used in this makefile?
3. How is variable appending useful when using eval?
4. How do info/eval compare?


