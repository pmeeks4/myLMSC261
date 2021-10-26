I knew I'd need a counter, so I went back into an old README to find the command I wanted to start with.

    while (count < 3): 	
    count = count + 1
    print("Happy Monday")

I now know I need to connect this somehow to my other idea of the parameters.

  if count % 3:
	  print("fizz")
  if count % 5:
    print("buzz")
  if count % 3 and count % 5:
	  print("fizzbuzz")

Rachel: "The ordering of these is going to be a problem."
Patrick: "Oh ok ok ok, I think i get it."

Now I'm thinking I need to put the last condition first and turn it into an if else statement somehow.

Rachel: "The counter is the most important part. Then figure out how to replace the numbers."

So I switched focus to creating a counter. I tweaked the command from before, and then ran it and it worked.

  count = 0
  while(count < 100):
    count = count + 1
    print(count)

This gave me my list of numbers. Now I need to add fizz, buzz and fizzbuzz. I tried adding onto the end of my previous command, "if count % 3 and count % 5: print("fizzbuzz")" but that didn't work, giving me random fizzes and buzzes and fizzbuzzes.
I then tried something I found on stackoverflow.com written by user "Jean-François Fabre

  if count % 3 == 0 or count % 5 == 0:
      print("fizzbuzz")

This worked, except it put the word after each integer instead of replacing it. Also, by using "or", it would put fizzbuzz after every integer divisible by 3, or 5. So I changed or to and, and I got a much better result, with fizzbuzz coming after every integer I want it to replace.
My new command was

  while(count < 100):
    count = count + 1
    print(count)
  if count % 3 == 0 and count % 5 == 0:
    print("fizzbuzz")
  elif count % 3 == 0:
    print("fizz")
  elif count % 5 == 0:
    print("buzz")

I'm so close, this gives me the exact answer that I want, the words just won't replace the numbers.
My next idea was to change the command so that I tell it that when the count is divisible by 3, the count = fizz and so on, but that didn't work. I was given NameError: name 'fizz' is not defined
Then I found a website called compciv.gov, which told me that in order to get the words to replace the numbers, I need to use an else statement. So then I tried this command.

while(count < 100):
  count = count + 1
  print(count)
if count % 3 == 0 and count % 5 == 0:
  print("fizzbuzz")
else:
  print(count)
if count % 3 == 0:
  print("fizz")
else:
  print(count)
if count % 5 == 0:
  print("buzz")
else:
  print(count)

This didn't work, sadly. I ended up getting a big string of repeated numbers with words where they should be for the most part.
I then realized my mistake, I needed to use an if, then an elif, then another elif, then an else. My command ended up looking like this:

count = 0
>>> while(count < 100):
count = count + 1
if count % 3 == 0 and count % 5 == 0:
  print("fizzbuzz")
elif count % 3 == 0:
  print("fizz")
elif count % 5 == 0:
  print("buzz")
else:
  print(count)

and it worked!
