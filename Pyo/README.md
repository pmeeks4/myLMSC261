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
