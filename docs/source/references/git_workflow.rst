Git Workflow
============

===================
Git Branching Model
===================

At KumarRobotics, we use a simplified `git branching model <http://nvie.com/posts/a-successful-git-branching-model/>`_,  which is inspired by ``Tailmix/Redwood``.
The central repository holds two main branches under ``origin``:

- ``master``
- ``develop``

``master`` branch
-----------------

The ``origin/master`` is the main branch where the code of ``HEAD`` always reflects a *demo-ready* state. We treat the ``master`` branch as **read-only**, such that no code should be directly committed to it. Instead, the ``master`` branch moves forward only by merging from ``develop`` branch.

``develop`` branch
------------------

The ``origin/develop`` is the main branch where the code of ``HEAD`` always reflects a *stable* state of development. You should not commit to ``develop`` directly as well. It advances by merging in pull requests from topic branches, after review.

When the source code in the ``develop`` branch reaches a stable point and is ready to be released, all of the changes should be merged back into ``master`` and then tagged with a release number.


Topic branches
--------------

The topic branches always have a limited life time, since they will be removed eventually.
Try to keep the commits in a single branch tightly related, and give it a descriptive name. 

We recommend using the following prefixes in branch names:

- ``feature/`` - New features.
- ``fix/`` - Bug fixes.
- ``refactor/`` - Code movement or restructuring.

Pull requests and code review
-----------------------------

We follow the `hared repository <https://help.github.com/articles/using-pull-requests>`_ model.
You do not need to fork the repository. Simply use topic branches to sandbox new work.
Use the following workflow for development:

1. Create a topic branch off of ``develop`` for new work::

    $ git checkout -b fix/handle-frame-drops

2. Develop your code inside the branch. Commit liberally to track your changes.

3. Regularly push your branch to the server (``origin``)::

    $ git push origin fix/handle-frame-drops

4. When you are ready for a code review, or simply want some feedback, initiate a `pull request <https://help.github.com/articles/using-pull-requests>`_. Go to the repository that you are working on on Github, switch to your branch, and click the Pull Request button.

5. Github defaults to merging into ``master``. Click the Edit button and change the merge target to ``develop``.

6. Get someone else to review your changes. Revise & iterate until convergence.

7. `Merge your branch <https://help.github.com/articles/merging-a-pull-request>`_. You can merge directly through Github by clicking the ``Merge pull request`` button.

  To merge locally::

    # Checkout the changes if you don't already have the branch locally
    git fetch origin
    git checkout fix/handle-frame-drops

    # Make sure the branch is up-to-date and resolve any conflicts
    git merge develop

    # Fast-forward develop, and update the server
    git checkout develop
    git merge fix/handle-frame-drops
    git push origin develop

8. Optionally, tidy up defunct branches you do not inted to develop anymore.

  Delete local topic branch::

    git branch -d fix/handle-frame-drops

  If you are dealing with pull request on Github, it will prompt you whether to delete the branch or not after merging. Otherwise, you can do this to clean up the remote topic branch::

    # assume remote branch not deleted by Github
    git push origin --delete fix/handle-frame-drops
    git remote prune origin
