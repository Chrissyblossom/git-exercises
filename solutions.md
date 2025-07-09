## Exercise 1
Linus Torvalds created git in 2005.

The essence of git is to :
-track changes to code or files over time.
- collaborate with others without overwriting each other's work.
- branch and experiment without breaking the main project.
- rollback to any point in history.

## Exercise 2
The difference between the three  is that git is a command line tool installed locally to manage your source code history, whilst github is a cloud-based platform for hosting git repositories and gitlab is another git hosting platform such as github but includes CI/CD issue tracking.

## Exercise 3
Yes.
- Subversion
- Mercurial
- Perforce
- Bazaar
- CVS

## Exercise 4
git  init - initilizes a new Git repository in your current folder. It creates a hidden .git/ directory that tracks all your changes.
git status - shows the current state of your working directory and staging area.

## Exercise 5
Commit is a snapshot of your code at a particular point in time.

## Exercise 6 *
To ignore in git you make use of .gitignore.

## Exercise 7
git log shows the commit history of your git repository.

## Exercise 8 
to git add to means to change stages , preparing them for the next commit. It informs git of the changes you want to include in the commit.

## Exercise 9*
The staging area is where changes are placed before commiting them to the repository.
You get items into the staging area by using git add <file> to move the files from the working directory to the staging area.

## Exercise 10
To commit in git with a amessage on the same line, you use the -m flag followed by the message in quotes.

## Exercise 11
The differences between pull, push and fetch commands in git is :
git pull : fetches changes from a remote repository and merges them into the local branch.
git push : sends your local commits to a remote repository.
git fetch: fetches changes from the remote repository without merging them into your local branch.

## Exercise 12
You use the git remote show origin.
explanation of output
- * remote origin - shows thats im inspecting the remote named origin.
- fetch URL - the URL git to download changes from github.
- push URL - the URL git uses to push changes.
- HEAD branch - default branch.
- Remote branch - a list of all branches on existing on the remote.
- "christine Tracked" - indicates the local branch Christine is connected to the remote christine.
-local branch configured for 'git pull' - which remote branch will be merged when i run git pull.
- christine merges with remote christine - means running git pull on my local christine branch will pull from the christine branch on github .
- local ref configured for 'git push' - notifies where my branch will push to when i run git push.
christine pushes to christine (up to date) - shows that thw local branch christine pushes to the remote christine branch and they are in sync.

## Exercise 13*
Merge - preserves history, creates a merge commit.
Rebase - Rewrites history, linearizes the commit history without a merge.
## Exercise 14*
-git checkout is used to switch branches, restore files in your working directory, create a new branch by using -b.
- git switch


## Exercise 15
Tags are used to mark specific points in the repository's history usually for releases.
Tags are immutable.
Types of Tags:
- Lightweight tags - do not store more information.
- Annotated tags - Full object in Git, storing the tagger's details.
## Exercise 16
Deleting with -d is to safe delete, which will refuse to delete if the branch has unmerged changes.

Deleting with -D is to force delete, even if the branch isnt fully merged.

## Exercise 17*
 Yes you can change a branch name 

## Exercise 18
Reverting a commit resetting to a previous commit means to create a new commit that undoes the changes introduced by a previous commit without changing the commit history.
To reset a previous commit is to move the current branch to a specific commit and optionally modify the working directory or staging area.
Revert is to create a new commit that undoes the changes of a previous commit.Revert does not change the commit history.
Reset is to move current branch to a previous commit. Reset changes the history by removing commits. however reset can change the working directory and staging area.

