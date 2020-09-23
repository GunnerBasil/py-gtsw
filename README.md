i stopped working on this and removed the pip install option.
# py-gtsw
GTSW, or Google translate string warp, is a python script meant to mess up strings. That's all. This is not meant to be serious, so do whatever you want, just give me credit. If you need help, put down an issue
# How to use
**Casual use:**

First, you will want to run the following command in your terminal once. If you already have the googletrans module, then ignore this step:

```
pip install googletrans
```

Download the warp.py file, and run it with Python. You will get two prompts. One you will ask you for the text you want to warp, and the other will ask you how much you want to warp it. Keep in mind, the larger the warp power, the longer it will take.

**Use with other projects:**

For use with other scripts, run the following commands in your terminal, but if you already have the modules, ignore this step:

```
pip install googletrans
pip install gtsw
```


# Api documentation

###### warp(text,power)

  Warps a string n amount of times and returns it.
  
  Text is the string to be warped.
  
  Power is the amount of times that it should be warped.
  
###### warpstat(text,power)

  Same as above, but displays status updates.
  
###### warp_once(text)

  Warps a string once and returns it.
  
  Text is the string to be warped.

###### smiley()
  
  prints out a smiley face ":D"

# Update log

v2.0 Uploaded to pip

v1.0 Created this project
