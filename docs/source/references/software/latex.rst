LaTeX
=====

=================
Tikz and PGFPlots
=================

Subsample plots
---------------

If you have too much data to plot, your document may take quite a while to compile. To speed things up, you can subsample the data. To plot only a subset, you can follow the discussion `here <http://tex.stackexchange.com/questions/47787/how-to-select-a-finite-number-of-samples-from-the-file-when-plotting-using-pgfpl>`_ and modify the ``addplot`` command in your ``tikz`` file.
::

    \addplot[<your options here>,each nth point={100}] ...

