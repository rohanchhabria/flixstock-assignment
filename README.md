# Flixstock Assignment [Associate Software Development Engineer]

The PDF consists of 3 problem statements, you can find a folder for each of these problem statements respectively.

### Problem Statement 1: Numpy
* Write python code to create the smallest bounding rectangle of all non zero values in a numpy array
    - Consider a 2D numpy array which is filled with zeros
    - Few random cells have non zero values
    - Find the coordinates(x,y,height,width) of the smallest rectangle that contains all non zero values
* Deliverables
    - Code in Python
```
cd problem-statement-1
python bbox.py
```

### Problem Statement 2: Multithreading
* Write a python code to do the following:
    - It should be able to launch 3 different thread
    - Each thread should print this every 5 second:
        * Thread <thread number> is running at <time elapsed>
        * E.g.
            - "Thread 2 is running at 0"
            - "Thread 2 is running at 5"
            - "Thread 2 is running at 10"

    - Initially start thread 1 and 3
    - After 20 second stop thread 1 start thread 2
    - Again after 18 second stop thread 3 and start thread 1
* Deliverables
    - Code in Python
```
cd problem-statement-2
python threads.py
```
### Problem Statement 3 : Create Required Image
* Given the image input.jpg and mask.png create the image result.jpg.
* Link to images
    > https://drive.google.com/drive/folders/1DB60KVzGCFe1d1_V2aAIRMSwNOS9939i?usp=sharing
* Deliverables
    - Code in Python
    - Resulting image
* Hint
    > https://learnopencv.com/alpha-blending-using-opencv-cpp-python
```
cd problem-statement-3
python blender.py
```
