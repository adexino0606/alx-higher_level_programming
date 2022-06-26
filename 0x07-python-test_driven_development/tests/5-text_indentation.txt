# doctest_5-text_indentation.py
===============================
Tests to 5-text_indentation.py
===============================

This library search in a text the delimitors (?, : and .) if find this characters insert two new lines that.
Finally print the new text
``text_indentation(text)``.

File ``5-text_indentation.py``

Return: None

Importing the function:

	  >>> text_indentation = __import__('5-text_indentation').text_indentation

Test to realize:

     >>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
     ... Quonam modo? xUtrum igitur tibi litteram videor an totas paginas commovere? \
     ... Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
     ... Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
     ... Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
     ... rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
     ... stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
     ... cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
     ... beatiorem! Iam ruinas videres""")
     Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     <BLANKLINE>
     Quonam modo?
     <BLANKLINE>
     xUtrum igitur tibi litteram videor an totas paginas commovere?
     <BLANKLINE>
     Non autem hoc:
     <BLANKLINE>
     igitur ne illud quidem.
     <BLANKLINE>
     Fortasse id optimum, sed ubi illud:
     <BLANKLINE>
     Plus semper voluptatis?
     <BLANKLINE>
     Teneo, inquit, finem illi videri nihil dolere.
     <BLANKLINE>
     Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
     <BLANKLINE>
     Si id dicis, vicimus.
     <BLANKLINE>
     Inde sermone vario sex illa a Dipylo stadia confecimus.
     <BLANKLINE>
     Sin aliud quid voles, postea.
     <BLANKLINE>
     Quae animi affectio suum cuique tribuens atque hanc, quam dico.
     <BLANKLINE>
     Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

     >>> text_indentation("::::")
     :
     <BLANKLINE>
     :
     <BLANKLINE>
     :
     <BLANKLINE>
     :
     <BLANKLINE>

     >>> text_indentation("\nabc\n\n")
     <BLANKLINE>
     abc
     <BLANKLINE>

     >>> text_indentation("")


     >>> text_indentation("     ")


     >>> text_indentation("    a  ")
     a

     >>> text_indentation("    a         b    ")
     a         b

     >>> text_indentation(131651)
     Traceback (most recent call last):
     	       ...
     TypeError: text must be a string

     >>> text_indentation(None)
     Traceback (most recent call last):
     	       ...
     TypeError: text must be a string

     >>> text_indentation("10.50")
     10.
     <BLANKLINE>
     50

     >>> text_indentation()
     Traceback (most recent call last):
     	       ...
     TypeError: text_indentation() missing 1 required positional argument: 'text'
