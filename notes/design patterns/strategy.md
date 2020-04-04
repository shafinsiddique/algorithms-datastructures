# Strategy Design Pattern

The strategy design pattern is a design pattern that encapsulates a set of algorithms and selects one from the pool during runtime. The algorithms are interchangeable, meaning that they can be substituted for each other during run time.

Strategy design pattern is extremely valuable for solving inheritance issues.

The basic idea is that if we have a bunch of subclasses and suddenly we have a feature that certain subclasses will have and the others will not, we take those varying factors out and encapsulate them on its own.

The classes then have an attribute on which we can call an interface method.

# Example

Imagine you are making a video game with various types of characters. Now all characters can walk, run, eat, sleep. However, your boss introduces the idea of superheroes in the game. Superheroes are exactly like regular characters except they can fly and fight. Not only this but your boss also says that certain types of characters (CartoonCharacter) that are not superheroes can also fly and fight.

Now, initially this is what your code base looked like.

    public class Character {
        public void walk() {
        }
    
        public void run() {
    
        }
        
        public void eat() {
        
        }
    }
    
    public class CartoonCharacter extends Character {
    
    }
    
    public class RealLifeCharacter extends Character {
    
    }
    
Now, in order to implement the new features, we need to make cartoon characters be able to fly and fight. And have a superhero class that extends Character but also has the methods fly and fight.

Our first instinct would be to simply add the methods into the 2 classes and then because its only two, just implement them there. But wait, what if down the line, 50 types of characters have to implement these methods. Do we copy paste the implementations everywhere? And then when we have to change something, do we go back into all 50 of those classes and change the methods?

As you can see, this would be extremely inefficient and time consuming. 

# Strategy to the Rescue

The idea behind the Strategy pattern is to encapsulate algorithms that are varying. In this case, we encapsulate Flying and Fighting into its own classes using interfaces that model its behavior. 
What does this mean?

Well, let's create a Flyable and Fightable interface first.

    interface Flyable {
        public void fly();
    }
    
    interface Fightable {
        public void fight();
    }
    
Then, we create classes for concrete implementation of these behaviors.

    public class NoFly implements Flyable {
        public void fly() {
            // do nothing, this is for the characters that dont fly.
    }
    }
    public class FlyWithWings implements Flyable {
        public void fly() {
            // do something. fly with wings. This is for characters that do fly.
            }
        }
        
Then in our character superclass, we add an attribute and a method.

    public class Character {
        Flyable flier;
        
        public void fly() {
            flier.fly();
        }

    }
    
If we use this approach, we no longer have to go to each seperate class and write an implementation for flying. We can just set the attribute in the constructor based on whether a character flies or not. If they do fly, we can set the attribute to an instance of the NoFly class else we can set the attribute to an instance of the FlyWithWings class.

We would do the same for fighting.

Now, you might be thinking, why didn't we use a simple boolean variable in the super class. Well, the idea is that in our current version, characters can either fly or they cant fly. They can either fight or they can't fight. However, in the future, characters who might be able to fly might have different types of flying. For each type, there would need to be a different class. But that wouldn't matter to the rest of our code because our superclass instantiates the flier attribute based on the Flyable interface.

Always remember that it is much better to code to interfaces rather than to concrete implementations.


    
    
    

