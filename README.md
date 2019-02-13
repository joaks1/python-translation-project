# Introduction

The purpose of this exercise is to learn some basics of Python by manipulating
RNA sequences.


# Contents

-   [Getting set up](#getting-set-up)
-   [Exercise](#exercise)
    -   [The goal](#the-goal)
    -   [The script](#the-script)
        -   [Input](#input)
        -   [Output](#output)
        -   [Examples](#examples)
        -   [Some hints to get you coding](#some-hints-to-get-you-coding)
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

    As you work on the exercise below, be sure to frequently `commit` your work
    and `push` changes to the *remote* copy of the repo hosted on Github.


# Exercise

## The goal

The goal of this exercise is for you to practice Python coding by editing a
script (or module) for manipulating RNA sequences until it runs and passes a
suite of tests.

Type `ls` in the directory of the repo you just cloned. You should see
something like:

    $ ls
    LICENSE.txt
    README.md
    test_translate.py
    translate.py
    
The file `translate.py` is where you will write your Python code.  Go ahead and
open it with your preferred text editor.
You will see that the file is mostly filled with functions and their
docstrings.
Currently these functions don't do anything;
they only call the `pass` statement, which does nothing and causes them to
return `None`.

The file `test_translate.py` is a Python script that runs a series of tests on the
`translate.py` script. Since that code doesn't exist yet, all of these
tests currently fail. Try it:

    $ python3 test_translate.py

Your goal is to add Python code to `translate.py` until these tests pass.
Based on the functions' docstrings and the messages reported by failing tests,
it should be clear what the functions in `translate.py` should be doing to pass
the tests.

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
