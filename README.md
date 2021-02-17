# Introduction

This project comprises two exercises to help you learn some basics of Python
(Exercise 1) and regular expressions (Exercise 2) by manipulating nucleotide
sequences.

# Contents

-   [Getting set up](#getting-set-up)
-   [Exercise 1](#exercise-1)
-   [Exercise 2](#exercise-2)
    -   [Part 1](#part-1)
    -   [Part 2](#part-2)
-   [Acknowledgments](#acknowledgments)
-   [License](#license)


# Getting set up

At this point, you should have
(1) an account on [Github](https://github.com/) and
(2) been introduced to the very basics of [Git](https://git-scm.com/).

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/joaks1/python-translation-exercise), by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master

---

# Exercise 1

## Learning objective 

Learn some basics of Python by filling in code for functions that manipulate
nucleotide sequences.

## The goal

The goal of this exercise is for you to practice Python coding by editing a
script (or module) for manipulating nucleotide sequences until it runs and
passes a suite of tests.

Type `ls` in the directory of the repo you just cloned. You should see
something like:

    $ ls
    find_orf.py
    LICENSE.txt
    README.md
    test_find_orf.py
    test_translate.py
    test_util.py
    translate.py
    
The file `translate.py` is where you will write your Python code for this
exercise.
Go ahead and open it with your preferred text editor.
You will see that the file is mostly filled with functions and their
docstrings.
Currently these functions don't do anything;
they only call the `pass` statement, which does nothing and causes them to
return `None`.

The file `test_translate.py` is a Python script that runs a series of tests on the
`translate.py` script. Since that code doesn't exist yet, all of these
tests currently fail. Try it:

    $ python3 test_translate.py

You can also run the tests for only one of the functions in `translate.py`.
For example, to run only the tests for the `get_reverse` function, try:

    $ python3 test_translate.py TestGetReverse


For each function, your goal is to delete the `pass` statement and add your own
Python code until all the tests of the function pass.
Based on the functions' docstrings and the messages reported by failing tests,
it should be clear what the functions in `translate.py` should be doing to pass
the tests.

Because the functions range from relatively simple to challenging, and the more
challenging functions might use the simpler ones, I *strongly* recommend that
you get all the tests working for one function before moving onto another, and
do so in the following order:

1.  Get tests of `get_reverse` function working:

        $ python3 test_translate.py TestGetReverse

1.  Get tests of `get_complement` function working:

        $ python3 test_translate.py TestGetComplement

1.  Get tests of `reverse_and_complement` function working:

        $ python3 test_translate.py TestReverseAndComplement

1.  Get tests of `translate_sequence` function working:

        $ python3 test_translate.py TestTranslateSequence

1.  Get tests of `get_all_translations` function working:

        $ python3 test_translate.py TestGetAllTranslations

1.  Get tests of `get_longest_peptide` function working:

        $ python3 test_translate.py TestGetLongestPeptide


**NOTE: You do NOT need to know how the tests work! You only need to add code
to `translate.py`.**
The tests only care about what each function returns, not *how* the functions
work.

**NOTE: You do NOT need to change the code below the `if __name__ ==
'__main__':` line. Only the functions themselves need work.**

## Suggestions

-   Make sure you are using Git to commit and push your work often as you work
    on this exercise.
-   `print` statements are your friend while you are debugging.
-   `assert` statements are also your friend.
-   If a function is getting long, define your own new functions to keep the
    code as modular as possible.
-   Once you get the script working and all the tests passing, think about how
    you might improve the script. For example:
    -   What happens if a DNA sequence is passed to your functions? How would
        you want to handle this?
    -   Should your functions only accommodate strings for the sequence
        argument? What if someone passes a list? a tuple? How do you want your
        functions to behave?
    -   Should you have a default genetic code, so the caller doesn't always
        have to create and pass a big dictionary to your functions? How would
        you do this in a way that does not rely on *global* variables? How
        could you avoid globals *and* avoid creating multiple instances of the
        genetic code?  This is a bit advanced, but a good solution might
        involve creating a class that manages genetic codes.

Good luck!

---

# Exercise 2

## Part 1

**_Learning Objective_**: The goal is for you to practice using regular
expressions in Python to find open-reading frames (ORFs) in sequences of
nucleotides.

Open the file `find_orf.py` with your preferred text editor.
In this file you will find functions with detailed docstrings, and three
places in the code marked with comments like:

    ##########################################################################
    ############################ EDIT CODE BELOW #############################
    # `codon_pattern_str` needs to be a regular expression that will match any
    # codon (but only one codon).
    # Currently, `codon_pattern_str` is only a string of literal characters.
    # This is a valid regular expression, but it will only match 'AUG' exactly.
    # Change `codon_pattern_str` so that it will match any valid codons, and
    # only valid codons.
    # Read the docstring above for additional clues.
    codon_pattern_str = r'AUG'
    ##########################################################################

Here is where you will need to edit the code to get a regular expression that
accomplishes the task at hand. In the example above, `codon_pattern_str`
is the regular expression that you would need to edit.
Read the function's docstring *and* the comments *carefully* to help guide your
composing of the regular expression.

Once you have successfully composed the regular expressions in `find_orf.py`,
all the tests in `test_find_orf.py` will pass.

    $ python3 test_find_orf.py

Read the error and failure messages reported by `test_find_orf.py` (and the
docstrings in `find_orf.py`) **carefully** to help you get the regular
expressions in `find_orf.py` working correctly.

You can run the tests for each function separately:

    $ python3 test_find_orf.py TestVetNucleotideSequence
    $ python3 test_find_orf.py TestVetCodon
    $ python3 test_find_orf.py TestFindFirstOrf

These commands will run the tests for the functions `vet_nucleotide_sequence`,
`vet_codon`, and `find_first_orf`, respectively.
It can be helpful to only run the tests for the function your working on.

**Start with the** `vet_nucleotide_sequence` **and** `vet_codon` **functions
first**.
These regular expressions are easier, and the `find_first_orf` function depends
on them (i.e., it uses them), so working on `find_first_orf` will be easier if
the tests for `vet_nucleotide_sequence` and `vet_codon` are passing.

**NOTE: You do NOT need to know how the tests work! You only need to add code
to** `find_orf.py`.
The tests only care about what each function returns, not *how* the functions
work.

### Suggestions

-   Make sure you are using Git to add, commit, and push your work often as you
    work on Part 1 of this exercise.
-   Play around with 'mini examples' of the regular expressions in the python
    interpreter.

### Some fun with argparse

Once all the tests are passing, you can use `find_orf.py` as a script
to find the first open reading frame in a nucleotide sequence.
Check out the help menu:

    $ python3 find_orf.py -h

This help menu is created automatically by the `argparse` package using the
information provided by the code in the `main` function in `find_orf.py`.

You can give the script a nucleotide sequence to search at the command line:

    $ python3 find_orf.py AUGGUAUAA

The sequence can also be provided in a file if you specify the `-p` flag:

    $ python3 find_orf.py -p path-to-a-file-with-a-sequence.py 

You can also specify start and stop codons with `-s` and `-x` arguments,
respectively:

    $ python3 -s AUG -x UAA UAG find_orf.py AUGGUAUAA

All of this command-line interface is specified and handled in the `main`
function of `find_orf.py` using the `argparse` package.

This package can be very useful for making your scripts portable and user
friendly.
You will use it in Part 2!


## Part 2

**_Learning Objective_**: The goal is for you to practice writing your own
scripts in Python "from scratch" (from the shebang line to the command-line
interface).

Create a new script (file) called `translate_orf.py`.
Now, add code to `translate_orf.py` so that it can translate the first ORF
found in a nucleotide sequence.
This script will have a command-line interface very similarly to `find_orf.py`.
The only difference is that it will translate the ORF that it finds and report
the amino acid sequence (to standard output).

Some tips that might be helpful:

-   Write a `main` function *very* similar to the one in `find_orf.py` to set
    up the command-line interface and process command-line arguments.
-   `import` and use the `find_first_orf` function in `find_orf.py` to find the
    first ORF.
-   `import` and use the `translate_sequence` function in `translate.py` to
    translate the ORF.
-   `import` and use the `parse_sequence_from_path` function in `find_orf.py`,
    just like it is currently used in the `main` function of `find_orf.py`.
-   Don't worry about accommodating genetic codes; just use (i.e., copy and
    paste) the same genetic code that is defined in `translate.py`; you
    will need it in your `main` function.

A `main` function similar to the one in `find_orf.py` should be all you need to
get this working, because you can do the ORF searching and translation within
your `main` function using the functions you imported from `find_orf.py` and
`translate.py` and the genetic code you pasted in.


### Suggestions

-   Make sure you are using Git to commit and push your work often as you work
    on Part 2 of this exercise.


## Extra challenges (i.e., not required)
After completing Part 2, you likely have code in the `main` functions of
`find_orf.py` and `translate_orf.py` that is largely redundant.

Can you think of a way of reorganizing the code to avoid this redundancy?

Also, can you update `translate_orf.py` so that it can accommodate any genetic
code?


# Acknowledgments

## Material
This exercise was inspired by, and borrowed heavily from, the class notes and
Python scripts written by
[Mark Holder](http://phylo.bio.ku.edu/content/mark-t-holder),
which can be found at <https://github.com/mtholder/eebprogramming>.

## Support
This work was made possible by funding provided to [Jamie
Oaks](http://phyletica.org) from the National Science Foundation (DEB 1656004).


# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.
