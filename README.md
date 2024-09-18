<div align="Center" style="height: 250px">
    <img src="https://media.giphy.com/media/9d1Fo0XyIYXzW/giphy.gif?cid=ecf05e47zh2jss789s34ywvq1u7tjfbz54rku9a7n2qynngx&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Spongebob dancing">
</div>

# A case study of implementing OOP and procedural programming paradigm in Python
A programming paradigm is kind of style/architecture to write a program. There are a lot of programming paradigm out there. Let I mention here, object-oriented-programming (usually call as OOP), procedural, functional, visual programming, logic programming, and many more. There is not the best programmning out there. A programming paradigm might be the best for some case but not in other case. 

> 💡Anyway, not all programming language support all programming paradigm. Some of them already design to focus on specific task. So, it might not suitable to try implement another programming paradigm to that programming language.

## Why I do this ?
The top 2 most popular programming paradigm from what I already know are OOP and procedural. Most programmer may learn basic programming in procedural way. A program will run step by step instruction from what programmer want to be. The side effect of this is a program will have many lines of code. It will hard to maintenance that program. 

I started my first programming in Java. I hear a little about OOP paradigm from my simple question. Why there is code that I don't know what function of it.
```java
public class MyProgram {
    public static void main (String[] args) {
        System.out.println("Hello World!");
    }
}
```
Above code is basic Java program to print text "Hello World!". You can see it is must to define class and its main method. It's really difference when I try to code in other programming language like JavaScript, Python, C, C++. I curious why that happen. And then  I did simple research, I found new term "OOP". Java by default is try to make a program at least it wrapped inside of class. This class concept only found in OOP paradigm. 

Time after time I curious how it looks like to write the same program but have different style. One program written in OOP style and the other written in procedural way. I am not satisfied if I just build a simple program. 

<div align="Center" style="height: 200px">
    <img src="https://preview.redd.it/8jcj2z7h61741.png?auto=webp&s=a1203f8e8328777aac3869d6eab79171e24e3659" alt="Spongebob dancing">
</div>

> That picture illustrates how complex managing OOP can be; it's not as simple as it seems.

<div align="Center" style="height: 250px">
    <img src="https://asset-2.tstatic.net/travel/foto/bank/images/Suasana-penumpang-turun-dari-kereta-api.jpg" alt="Departure moment in the station">
</div>

I got the idea of this program is come from my travel with train of **PT KAI** (a train state company in Indonesia). When I try to get on the train, I do not go as simple I can directly go my desire train. There is a small system to manage the departure passenger. From what I can see, the steps looks like this:

1. Prospective passengers need to check their identity
2. If checking valid, the operator check will check their stuff
3. If the passenger stuff over the limit, they will got fine
4. After the train ready, operator will open the departure gate
5. Passenger will go to the train
6. The train is ready to go

I look that so interesting if I can make a simple program to manage the departure in the station. Without further ado, I START THE PROJECT!

## Why Python ?
<div align="Center" style="height: 200px">
    <img src="https://programmerhumor.io/wp-content/uploads/2021/05/programmerhumor-io-python-memes-backend-memes-aafb163a45bb7a5.jpg" alt="Spongebob dancing">
</div>

You see that meme ? It's because Python is quite easy to learn (especially if you compare it with Java). Even a pseudocode can be a program in Python :). 

Anyway, the real answer is I can clearly see a program in both in procedural and OOP without mixing them up. In Java, you need to write at least a single class and single method (main) to run the program. I don't like it because it still looks like OOP because there is a define class right there even I try to write code in procedural way. I do little research and I found Python is my best choice to make OOP program and procedural. If I want to write in procedural, just write that code top to down. If I want to write in OOP, just write that code inside of class. It's as simple as that.

## Development
I divided into 2 folders. The first folder is for oop and the other one is procedural. Firstly, I try to make the program in procedural. After I finish it, I will make another program with have same functionality but in OOP way. 

When I make program in procedural, I think it's easy and it will done so fast. And yup, that's right. But, when I try to do that in OOP, I a little bit confuse because I need to identify the object first to make the program. One more thing, because I can make a class, I think, "Why I do not make a data structure for it using class?". Because of that, you can see many class that actually have different name. Example: `Stuff` - `Stuffs`, `User` - `Users`, and `Ticket` - `Tickets`. I try to make a singular class name and plural. Singular is for blueprint a single object and plural is for blueprint an object that contain many object singular. 

The development is rapid. I built all of them only 3 days. Due to short development time, you might find bugs if you run it in your computer. I didn't have time to fix them, as my focus was on demonstrating how to build a program using both procedural and object-oriented programming. This way, I can compare the two approaches.

## Conclusion
<div align="Center" style="height: 250px">
    <img src="https://media.giphy.com/media/xT9DPCU60mRbtGw7Ys/giphy.gif?cid=790b7611wxlmtax5ysfefxum47nup6jzkb0qqiqa26evr60a&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Spongebob dancing">
</div>

FINALLY! The project is done. In my opinion, both programming paradigms—procedural and OOP—have their strengths. But you need to pay attention. In procedural programming, managing your functions properly is key. Functions often call other functions, and if you’re not careful, managing them can become stressful. Since one function can call another freely, there's always the risk of calling the wrong one, which can lead to errors in your program.

In OOP, I created many classes, but more classes don’t always mean better. Too many can also add complexity, making it hard to manage which class to use. If you design custom data structures using classes, it can make your program even more complicated and harder to maintain.

Overall, I’m happy I had the chance to work with both procedural and OOP approaches. It gave me insight into how each paradigm feels during development. This experience taught me how to approach similar cases in the future. That’s it for my simple case study! I hope you find some value in this and feel inspired to experiment like I did. Happy coding! :

---

---