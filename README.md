# Introduction

The purpose of this exercise is to learn regular expressions in Python by
working with sequences of nucleotide.


# Getting set up

At this point, you should have
(1) an account on [Github](https://github.com/) and
(2) been introduced to the very basics of [Git](https://git-scm.com/).

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/joaks1/python-translation-project), by
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

    At this point, you should be in your own local copy of the repository.

1.  Next, create a new 'homework' branch for working on this exercise:

        $ git checkout -b homework origin/dev

    This will get you to a point where we left off from the Python translation
    homework. Confirm that all the translation code is working:

        $ python3 test_translate.py
        $ python3 translate.py

1.  Create a remote 'homework' branch that you can 'push' to as you work on the
    exercise:

        $ git push origin homework:homework

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* 'homework' branch. Don't enter
    these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin homework


# Exercise

## The goal

The goal of this exercise is for you to practice using regular expressions in
Python to find open-reading frames (ORFs) in sequences of nucleotides.

## Part 1

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

Read the error and failure messages reported by `test_find_orf.py` carefully
to help you get the regular expressions in `find_orf.py` working correctly.

You can run the tests for each function separately:

    $ python3 test_find_orf.py TestVetNucleotideSequence
    $ python3 test_find_orf.py TestVetCodon
    $ python3 test_find_orf.py TestFindFirstOrf

These will run the tests for the functions `vet_nucleotide_sequence`,
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

-   Make sure you are using Git to commit and push your work often as you work
    on Part 1.
-   Work on 'mini examples' in the python interpreter.

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
    paste) the same genetic code that is in `translate.py` (just after `if
    __name__ == '__main__':`).

A `main` function similar to the one in `find_orf.py` should be all you need to
get this working, because you can do the ORF searching and translation within
the `main` function using the functions you imported from `find_orf.py` and
`translate.py` and the genetic code you pasted in.


### Suggestions

-   Make sure you are using Git to commit and push your work often as you work
    on part 2.


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
