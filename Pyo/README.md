# I believe I copy and pasted eveything into terminal correctly, however I'm getting an error message still. This is what the error message says:
error: implicit declaration of function
      'AudioGetCurrentHostTime' is invalid in C99
      [-Werror,-Wimplicit-function-declaration]
    now.mHostTime = AudioGetCurrentHostTime();
# I genuinely have no idea how to fix this / what this means. This is what the end of the message says.
error: command '/usr/bin/gcc' failed with exit code 1
# Dom says to install these dependencies
brew install libsndfile

brew install portaudio

brew install portmidi

brew install liblo
# I tried this and yet I still got the same error message.
# This is now a week later and I'm going to attempt the same thing with a fresh mind. I ran every step while skipping the optional one, and yet again, it yielded the same result with the same error message.

warning: 'AudioDeviceRemoveIOProc' is
      deprecated: first deprecated in macOS 10.5
36 warnings and 1 error generated.
      error: command '/usr/bin/gcc' failed with exit code 1

# I looked everywhere for a solution but everything I've found has either been not relevant to the problem I have or too complicated for me to understand. I did find a post on stackoverflow.com that describes my exact problem, but it didn't have any responses and I'm 99% sure it was Courtney's post.


For my programming class I need to install pyo through the terminal and successfully run a few files.

I ran into an error while trying to download it and I have no idea how to fix it.

The error message is rather long but the most important line (to me) appears to be

implicit declaration of function 'AudioGetCurrentHostTime' is invalid in C99 [-Werror,-Wimplicit-function-declaration]

another seemingly important line is

error: command '/usr/bin/gcc' failed with exit code 1

This happens when I try running the code

sudo python3 setup.py install --use-coreaudio --debug

I have tried reinstalling homebrew as well as the portaudio, portmidi, libsndfile, and liblo dependencies.

I really don't know where to go from here

# I've been trying for a while now and I haven't gotten any closer to figuring it out, so unfortunately I think it has stumped me.
