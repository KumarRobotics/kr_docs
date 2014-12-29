Git Workflow
============

===================
Git Branching Model
===================

For simplicity, we use `GitHub Flow <http://scottchacon.com/2011/08/31/github-flow.html>`_, which will be summarized here.

GitHub Flow
-----------

- Anything in the ``master`` branch is deployable
- To work on something new, create a descriptively named branch off the master (ie: ``feature/handle-frame-drops``)
- Commit to that branch locally and regularly push your work to the same named branch on the server
- When you need feedback or help, or you think the branch is ready for mergin, open a pull request
- After someone else has reviewed and signed off on the feature, you can merge it into master
- Once it is merged and pushed to `master`, you can and should deploy immediately


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

We follow the `shared repository <https://help.github.com/articles/using-pull-requests>`_ model.
You do not need to fork the repository. Simply use topic branches to sandbox new work.
Use the following workflow for development:

1. Create a topic branch off of ``master`` for new work::

    $ git checkout -b fix/handle-frame-drops

2. Develop your code inside the branch. Commit liberally to track your changes.

3. Regularly push your branch to the server (``origin``)::

    $ git push origin fix/handle-frame-drops

4. When you are ready for a code review, or simply want some feedback, initiate a `pull request <https://help.github.com/articles/using-pull-requests>`_. Go to the repository that you are working on on Github, switch to your branch, and click the Pull Request button.

5. Github defaults to merging into ``master``. You can click the Edit button and change the merge target to ``some-other-branch``.

6. Get someone else to review your changes. Revise & iterate until convergence.

7. `Merge your branch <https://help.github.com/articles/merging-a-pull-request>`_. You can merge directly through Github by clicking the ``Merge pull request`` button.

  To merge locally::

    # Checkout the changes if you don't already have the branch locally
    git fetch origin
    git checkout fix/handle-frame-drops

    # Make sure the branch is up-to-date and resolve any conflicts
    git merge master

    # Fast-forward master, and update the server
    git checkout master
    git merge fix/handle-frame-drops
    git push origin master

8. Optionally, tidy up defunct branches you do not intend to develop anymore.

  Delete local topic branch::

    git branch -d fix/handle-frame-drops

  If you are dealing with pull request on Github, it will prompt you whether to delete the branch or not after merging. Otherwise, you can do this to clean up the remote topic branch::

    # assume remote branch not deleted by Github
    git push origin --delete fix/handle-frame-drops
    git remote prune origin
