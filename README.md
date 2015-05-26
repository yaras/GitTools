# GitTools 

Tools for git. 

Requirements:

* python
* git

## git-intersection

Finds intersection of files between commits or commit ranges

**Usage**

Create alias:

```
git config --global alias.intersection '!python /path/to/git-intersection.py'
```

**Examples:**

Find intersection between last two commits:

```
git intersection master master~1
```

Find intersection between two commit ranges

```
git intersection e9b5c58..master e9b5c58..feat-1234
```
