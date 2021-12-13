#For my final project, I'll be attempting to create a virtual environment using a program called A-Frame. I have several goals for myself going into this project. By the end of the project I would like for the virtual environment to achieve several things:

#1. The player should be able to move around within the environment
#2. The player should be able to interact with something within the environment.
#3. The environment should be accessible by anybody, not just whoever has the file.
#4. The environment should work over several platforms, including mobile phone, computer, and VR headset.

#I plan to eventually move my code into a text editor to make the process of generating a link to the environment easier, but to start, I'll be using a program called Glitch, an in browser text editor that displays your environment in real time. This makes experimenting with the code of the environment much easier for the time being. I found this through the A-Frame website

https://aframe.io
https://glitch.com/

#In glitch, you're automatically started with n environment with three objects. I first want to delete these objects and try and import my own environment, just to see what will happen. I found a website that talks about creating A-Frame environments and took a pre-made environment from there just to test whether it would work.

https://www.htmlgoodies.com/javascript/creating-a-better-environment-in-web-based-vr-using-a-frame/

<html>
  <head>
    <script src="https://aframe.io/releases/1.0.2/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-environment-component@1.1.0/dist/aframe-environment-component.min.js"></script>
  </head>
  <body>
    <a-scene environment="preset: forest; dressingAmount: 500" >

      <a-box position="-1 0.5 -3" rotation="0 45 0" color="#FFFF00" shadow></a-box>
      <a-sphere position="1 1.25 -5" radius="1.25" color="#FFFFFF" shadow></a-sphere>
      <a-sphere position="1 3.00 -5" radius="1.00" color="#FFFFFF" shadow></a-sphere>
      <a-sphere position="1 4.50 -5" radius=".75" color="#FFFFFF" shadow></a-sphere>
      <a-sphere position="1 3.00 -4.01" radius=".05" color="#000000" shadow></a-sphere>
      <a-sphere position="1 3.20 -4.04" radius=".05" color="#000000" shadow></a-sphere>
      <a-sphere position="1 2.80 -4.05" radius=".05" color="#000000" shadow></a-sphere>
      <a-sphere position="1.05 4.30 -4.05" radius=".06" color="#000000" shadow></a-sphere>
      <a-sphere position=".80 4.30 -4.05" radius=".06" color="#000000" shadow></a-sphere>
      <a-cylinder position="1 4.75 -5" radius="0.5" height="1.5" color="#000000" shadow></a-cylinder>
      <a-cylinder position="1 4.75 -5" radius="1.0" height=".01" color="#000000" shadow></a-cylinder>
    </a-scene>
  </body>
</html>

#I put this code into Glitch and I was able to render a forrest scene with a snowman and a box at the center. The player is able to look around at the scene, but not allowed to move, so my next goal was to give movement to the player. I found a creator on youtube by the name of Danilo Pasquariello that created a playlist about A-Frame techniques that I'll be referencing a lot for help. In his video entitled "Movement controls component (A-Frame Tutorial - WebVR)", I was able to find code that would allow the player to move freely.

https://www.youtube.com/watch?v=YJkHOQXVA1w&list=PL8MkBHej75fJD-HveDzm4xKrciC5VfYuV&index=35
Timestamp - 1:40

<a-scene environment="preset: forest; dressingAmount: 500" >
      <a-entity movement-controls position="0 0 0">
        <a-entity camera position="0 1.6 0"
                  look-controls="pointerLockEnabled: true">
          <a-cursor></a-cursor>
        </a-entity>

#This successfully gave the player movement within the environment, which checks off one of my goals for the environment, and it should work with both WASD controls as well as VR controllers.
#Now I'd like to change the environment itself and import a fun scene instead of the forrest. I was able to import a pretty sky using an image I found on google as an asset. Now I want an object in the environment. I tried putting an object into the environment using glitch, but I came across a problem where I couldn't upload folders into the assets folder, so from here I'll be switching to a text editor to try and solve this issue. This might make things easier in the long run since I'll have everything in the same place.
#Several hours later, I cannot get the program to run out of a text editor so I'm just going to stay within glitch, because I figured out how to upload objects into my environment. I learned it from this website:

https://learn.framevr.io/project1/part3

#I had to convert the gltf file that I downloaded the objects as into glb files and put those into my assets folder and it finally worked. These are the objects I used

https://sketchfab.com/3d-models/sheep-2-5e52b176b573484ca31f709ec1c441a5#download

https://sketchfab.com/3d-models/hiih-13db62b151a44bed840b3502858cdcb7#download

#The last thing I wanted was for the player to be able to interact with something. I found a website with code to enlarge an object when looked at, so I applied it to the sheep. When the player looks at the sheep, the sheep should enlarge slightly.

https://glitch.com/edit/#!/gorgeous-badge?path=index.html%3A30%3A60

<a-mixin id="scaleUpMixin" animation__scale="property: scale; dur: 500; easing: easeInOutQuad; to: 1.5 1.5 1.5;"></a-mixin>
        <a-mixin id="scaleDownMixin" animation__scale2="property: scale; dur: 500; easing: easeInOutQuad; to: 1 1 1;"></a-mixin>

        <a-mixin id="fadeInText" animation__opacity="property: text.opacity; dur: 500; to: 1"></a-mixin>
        <a-mixin id="fadeOutText" animation__opacity2="property: text.opacity; dur: 500; to: 0"></a-mixin>

        mixin="scaleUpMixin scaleDownMixin"
                        animation__scale="startEvents: mouseenter;"
                        animation__scale2="startEvents: mouseleave;">

#I finally took the link to the environment and made it into a QR code so everyone can try it on their phones! It worked on my phone and a couple other friends of mine tested it with me, and it's playable on mobile, as well as computer and VR Headset, which was my final goal.

#This is the final link to the project:
https://dog-understood-mandrill.glitch.me

#And this is the code:
https://glitch.com/edit/#!/dog-understood-mandrill
