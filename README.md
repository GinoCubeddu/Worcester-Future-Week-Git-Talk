

# Introduction To Git & GitHub

## Getting Started

Before we start anything locally we need to get a remote repo set up on GitHub. In order to do this we need [sign in](https://github.com/login) to GitHub. Once signed in and on GitHub's home page you should be able to see a button that says "New Repository" or "Start a project". If you are unable to see these buttons simply go [here](https://github.com/new).

Once on this page you will be able to decide a few things about your new project.
1. Name Your Repo
2. Give It a Description
3. Decide to make it Public or Private
4. Decide to initialize the repo with a README

In this case we want to name the new project something like "MyFirstRepo", give it a one line description, make it public and choose to initialize it with a README. At this point we are able to set things up on your local machine. 

## Setting Up Locally

This introduction will be covering how to interact with Git and GitHub through the terminal and not the GitHub Desktop application. The reasoning behind this is that you have more control over what you do and to give you a brief introduction to the terminal, a tool that will be useful throughout your career as a developer.

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

Please complete the [Getting Started](#Getting Started) section first.

### Setting Up Git

Now that git has been installed on your local machine the first thing that we need to do is tell git who you are. To start off open the terminal (Git Bash for windows) and type the following commands.

```shell
git config --global user.name "Your Name"
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

* `~/.ssh/id_rsa.pub` - The location of the file to be read.


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

2. Create a file called "aboutme.txt" using the `touch` command. The `touch` command just tells the terminal to create a new file.

   ```shell
   Gino@Gino-PC MINGW64 ~/Desktop/repos/MyFirstRepo (master)
   $ touch aboutme.txt
   ```

3. `echo` a short sentence into the file or edit the file by navigating to it in the explorer. `echo` is a command that tells the terminal to input a line of text into a file. **NOTE**: When using `echo` with one `>` it will overwrite everything in the file however if you use two `>>` it will append the echo to the end of the file.

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

9. Now that we have made that change you should be able to view it on GitHub.

## Exercise two

**INSERT EXERSICE TWO HERE**

