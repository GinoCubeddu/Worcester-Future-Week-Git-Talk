

# Introduction To Git & GitHub

## Getting Started

Before we start anything locally we need to get a remote repo set up on GitHub. In order to do this we need [sign in](https://github.com/login) to GitHub. Once signed in and on GitHub's home page you should be able to see a button that says "New Repository" or "Start a project". If you are unable to see these buttons simply go [here](https://github.com/new).

Once on this page you will be able to decide a few things about your new project.
1. The name of your repo
2. A brief description of what the repo holds
3. Decide to make it Public or Private
4. Decide to initialize the repo with a README

In this case we want to name the new project something like "MyFirstRepo", give it a one line description, make it public and choose to initialize it with a README. At this point we are able to set things up on your local machine. 

## Setting Up Locally

This introduction will be covering how to interact with Git and GitHub through the terminal and not the GitHub Desktop application. The reasoning behind this is that you have more control over what you can do and to give you a brief introduction to the terminal, a tool that will be useful throughout your career as a developer.

### Installing Git

The university machines already have the tools needed to do the required tasks however these instructions provide a point of interest for installing git at home.

#### Windows

Git for windows can be downloaded at their website [here](https://git-scm.com/downloads). This will install both git bash and the git GUI tool.

#### Mac

Git is easily installed on mac through a [Brew](https://brew.sh/) command. To do this simply open the terminal and type the following command.

```shell
brew install git
```

If you do not have Brew installed you can download it by following the instructions on their [website](https://brew.sh/).

#### Linux (Debian Based)

Again as on Mac Git is easily installed on Linux through the terminal but without the help of a 3rd party installer. On Linux simply open the terminal and type the following commands.

```shell
sudo apt-get update
sudo apt-get install git
```

Command Breakdown

* `sudo` - This tells the terminal to run the command with admin privileges
* `apt-get` - apt is the package manager for Debian based Linux systems.  

## Exercise one

Please complete the [Getting Started](#getting-started) section first.

### Setting Up Git

Now that git has been installed on your local machine the first thing that we need to do is tell git who you are. To start open the terminal (Git Bash for windows) and type the following commands.

```shell
git config --global user.name "Your Username"
git config --global user.email "Your Email"
```

 **Command Breakdown**

* `git` - The tool that we are using

* `config` - The sub command of the tool which handles its config

* `--global` - An Argument telling git that this information should be used in every session

* `user.name` - The config option for telling git what your name is

* `user.email` - The config option for telling git what your email is



Now that git knows who you are it is time for us to set up authorisation between your computer and GitHub. For this we are going to use a SSH key as discussed within the presentation. To do this enter the following command into your terminal and press the return key for each step.

```shell
ssh-keygen -t rsa -b 4096 -C "YOUR_EMAIL"
```

**Command Breakdown**

* `ssh-keygen` - The tool for creating ssh keys

* `-t` - This stands for the type of encryption we want to use

* `-b` - This stands for how strong we want to make our encryption (4096 is the standard)

Once the key has been generated you will be able to find it in your newly created ssh directory. To access the key use the following command which will output it to the terminal. Once you have the key go [here](https://github.com/settings/keys), click "New SSH key" and add the key.

```shell
cat ~/.ssh/id_rsa.pub
```

**Command Breakdown**

* `cat` - The tool for outputting the contents of a file to your screen

* `~/.ssh/id_rsa.pub` - The location of the file to be read


If everything went according to plan we should now be able to move onto cloning your repo.

### Cloning your Repository

To clone your repo type the following into the terminal.

```shell
cd ~/Desktop
mkdir repos
cd repos
git clone git@github.com:YOUR_GITHUB_USERNAME/REPO_NAME
```

**Command Breakdown**

* `cd ~/Desktop` - cd stands for "change directory" and the `~/Desktop` means go to the desktop
* `mkdir repos` - `mkdir` stands for "make directory" and `repos` is the name of the directory we will make
* `cd repos` - tells the terminal to enter the directory we just created on the desktop.
* `git clone` - This tells git to "clone" your remote repo which pulls it down for local use
* `git@github.com:YOUR_GITHUB_USERNAME/REPO_NAME` - This is the location of your remote repo

### Making A Change

Now that we have cloned the repo it is time to make our first change! To do so follow the instructions below.

1. Change directory to the repo we just cloned.

   ```shell
   Gino@Gino-PC ~/Desktop/repos
   $ cd MyFirstRepo/
   ```

2. Create a file called "aboutme.txt" using the `touch` command. The `touch` command creates an empty file with the name we provide.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ touch aboutme.txt
   ```

3. `echo` a short sentence into the file or edit the file by navigating to it in the explorer. `echo` is a command that tells the terminal to input a line of text into a file.
   **NOTE**: When using `echo` with one `>` it will overwrite everything in the file however if you use two `>>` it will append the echo to the end of the file.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ echo "Hello my name is Gino" > aboutme.txt
   ```

4. Now that we have made a change to the repo we can check its status through the `git status` command. The status command will tell us what is "staged" and what is not. When something is staged it means it will be included in your next commit.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Untracked files:
     (use "git add <file>..." to include in what will be committed)

           aboutme.txt

   nothing added to commit but untracked files present (use "git add" to track)
   ```

   Notice that it tells us that our file is untracked this means that it will not be included within our commit.

5. To fix this we need to use the `git add` command to "add" it to the next commit.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ git add aboutme.txt
   ```

6. Now that we have added the file lets check the status again.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ git status
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

           new file:   aboutme.txt
   ```

   Notice that this time the file comes under the "Changes to be committed" list and git has noticed that it was a totally new file.

7. Since we are now sure that the file will be committed we can use the `git commit` command in order to "commit" the changes with a message. A "commit" is a record of the changes that you have just made. A commit can be made up of a single file or hundreds of files.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ git commit -m "Added my bio to a text file"
   [master 763e052] Added my bio to a text file
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 aboutme.txt
   ```

8. Now that we have committed our change lets push it back to the remote repo on GitHub. To do this we will use the `git push` command. This command tells git to push it back to the remote repository.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ git push origin master
   Counting objects: 3, done.
   Delta compression using up to 8 threads.
   Compressing objects: 100% (2/2), done.
   Writing objects: 100% (3/3), 298 bytes | 0 bytes/s, done.
   Total 3 (delta 0), reused 0 (delta 0)
   To git@github.com:GinoCubeddu/MyFirstRepo
      0904c1f..763e052  master -> master
   ```

   Notice that I added the words `origin master`. The word `origin` means push to where we got the repo from (Which was your repo on GitHub) and the word `master` is the branch we are pushing to which in this case is called master. **NOTE**: When working on projects you should be working on separate branches and not on the master branch.

9. Now that we have created the file and pushed it you should be able to see it within your GitHub repo.

## Exercise two

In this exercise we will experience working on a repository with other people. This includes doing your work on your own branches that will be merged into master at a later date instead of everyone just working on the master branch as that can get messy. It will also introduce you to opening a pull request on a repo and the code review process.

To start with everyone should have filled out the [google form](https://docs.google.com/forms/d/e/1FAIpQLSfORqcDrZuOXfYstzrBHPvG4768ha4K7BDQqw9dEd1FQ0pAKw/viewform?usp=sf_link) informing me of your GitHub username so I can give you write permissions.

Since we have already setup your local git instance we can jump straight into cloning the repo to your local machine.

 ```shell
Gino@Gino-PC MINGW64 ~/Desktop/repos
$ git clone git@github.com:GinoCubeddu/Worcester-Future-Week-Git-Talk
Cloning into 'Worcester-Future-Week-Git-Talk'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
Checking connectivity... done.
 ```

It is important to note that you need to use my username for the cloning and not your own. This is because the remote repository is stored under my personal account.

Now that we have the repository cloned we should `checkout` to a new branch. When I say `checkout` that means we want to swap to a different branch to work on. There are two ways to do this:

**Way 1**

```shell
git branch $BRANCH_NAME
git checkout $BRANCH_NAME
```

**Command breakdown**

* `git branch $BRANCH_NAME` - This tells git that we want to create a branch with the passed in branch_name
* `git checkout $BRANCH_NAME` - This tells git to checkout to the branch that we just created.

**Way 2**

The second way only requires a single command which allows you to save time.

```shell
git checkout -b $BRANCH_NAME
```

Notice the `-b` after the `git checkout` this is basically telling git to create a new branch before checking out to it. Note that if you attempt to change to a branch that exists when using the `-b` argument you will receive an error.

When you are on your own branch (You can check what branch you are on by typing `git branch`) open the project directory in your favroute text editor and create a file with any extension (such as `html`, `css`, `php`, `cs`, `py`, etc) in the `submissions` folder called "USERNAME_YEAR" and add some context to it.

**Helpful Hint:** If you have a text editor such as atom installed on your machine you are able to open the project directory from the command line through this command:

```shell
atom .
```

**Command Breakdown**

* `atom` - Tells the terminal to use the atom text editor to open a file/folder
* `.` - This means open the current directory, this can be switched out with a file or folder name

Once you have created your folder we are ready to commit and push the file as we did in steps `4-8` in the previous exercise. The process was as follows:

1. Check the current status of your local repo
2. Add the files that you want to commit that are unstaged
3. Check the status again to ensure the correct files have been added
4. Commit the file(s) with a useful message
5. Push your files to the remote repository (**NOTE:** Push to your branch and not the master branch)

If everything went well you should be able to see your branch on the remote GitHub Repository and be able to open a pull request against the master branch in order to merge your changes. To do this follow these steps:

1. Open the GitHub Repo and switch branch by clicking on the branch dropdown and select your branch name as shown below:

   ![Image of Branch Dropdown](images/change_branch.png)

2. Once you are on your branch you should be able to see your file within the `submissions` folder. If you are indeed able to see your file you are ready to make a pull Request. In order to do this click the button that says "New pull request" next to the branch name drop down.

3. This should take you to a page to open a pull request where you are able to review your changes, name the pull request and give a brief description before opening the pull request.
   ![Image of opening a pull request](images/open_pull_request.png)

4. Once you click "Create pull request" you will be taken to the pull request page where people will be able to comment, approve or deny your request. If you go away from this page it is easily accessible again through the pull requests tab.

The final part of this exercise requires to open up the Pull Request of the person sat next to you, look at the files they have changed and leave a comment on their code. Once you have done that approve their pull request. This can be done by clicking on the "review changes" button on the files tab. **Note:** You are able to leave a comment on a certain line of code by clicking on the `+` at the beginning of the line.

![Showing how to approve a pull request](images/approve_pull_request.png)

Once your request has been approved go ahead and merge it.

## Further Reading

That's the end of this introduction to Git & GitHub. I hope you have enjoyed it! If you are interested in learning more read up on the following:

1. Rebasing
2. Conflict Resolution
3. Forking
4. Reverting Changes
5. Releases
6. And everything else!