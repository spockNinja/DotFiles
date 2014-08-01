#!/usr/bin/env python
# encoding: utf-8
import getpass

def main():
    username = getpass.getuser()
    if username == 'vagrant':
        import gitconfig
        print("You are running a vagrant so we need to check your .gitconfig")
        config = gitconfig.config("~/.gitconfig")
        if not config.user.name or config.user.name == "YourName":
            from subprocess import Popen
            print("Your DotFiles is misconfigured in BriteCore-Up:")
            print("You are still using the IntuitiveWebSolutions branch.")
            print("For now, we are just going to fix your .gitconfig on your Vagrant.")
            config.user.name = raw_input('Enter your first and last name: ')
            config.user.github = raw_input('GitHub username: ')
            config.user.email = raw_input('GitHub email address: ')
            Popen("touch ~/.config/git_check", shell=True)
            Popen("expand -t 4 ~/.gitconfig > ~/.gitconfig.new && mv ~/.gitconfig.new ~/.gitconfig", shell=True)
        else:
            print("Everything looks good!")

if __name__ == '__main__':
    main()
