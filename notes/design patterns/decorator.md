# Decorator Design Pattern

"Classes should be open for extension, but closed for modification." - The Open Closed Principle

The decorator pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

Instead of creating several subclasses, the decorator pattern tells us to create 'decorator classes.' A decorator class is a wrapper class that has the exact same interface as your base class. However, the constructor of a decorator class takes in a object of the same type and when we call any methods, we can use that attribute to modify that method or add further responsibilities.

It's a little tricky to wrap your head this particular design pattern (pun intended). So let's get right down to an example of when and why we use the decorator pattern.


# Example

Imagine that you are building the software for the Starbucks ordering system. You have different types of beverages and they all have a description and a cost. This is what your code base looks like.

    public abstract class Beverage {
        public String getDescription() {
        
        }
        
        public float getCost() {
        
        }

    }
    
    public class Coffee extends Beverage() {
        public String getDescription() {
            return "Coffee"";
        }
        
        public float getCost() {
            return 2;
        }
        
        
    }
    
Now, your code was working fine and everything. But then you realize you didn't account for the fact that customers can get several condiments (milk, soy, mocha) and have it all topped off with their beverage. Starbucks charges a bit for each of these, so they really need to get them built into their order system.

Your first instinct might be to create subclasses for each case. DecafCoffee, DecafCoffeeWithMocha, CoffeeWithJustSoy. But you can easily see the nightmare you will have dealing with all these subclasses.

Another approach you might be considering is having instance attributes. So you would include attributes for each condiment in the superclass and then have methods such as setMocha(), hasMocha(), hasMilk(), setMilk().

This approach seems fine at first but a closer look reveals several flaws. Price changes for condiments will force us to alter existing code. New condiments will force us to add new methods and alter the code method in the superlcass. We may have new beverages. For some beverages (iced tea), the condiments may not be appropriate. The tea subclass will be inheriting useless methods such as hasWhip. What if a customer wants a double mocha?

# Decorator to the rescue

For a problem like this, the decorator pattern is an extremely natural choice. What we will do is have classes for beverage classes and then 'decorate' them with condiments. What does this mean? Well, let's see.

Well, we will have our original beverage classes.
    
    public interface Beverage {
        public String getDescription();
        public float getCost();
        
    }
    public abstract class Beverage implements Beverage{
        public String getDescription() {

        }

        public float getCost() {

        }

    }

    public class Coffee extends Beverage() {
        public String getDescription() {
            return "Coffee"";
            }

        public float getCost() {
            return 2;
            }

    }
    
Then, we create Decorator classes for the condiments. The decorator class will have the same interface as the Beverage classes.

    public class Mocha implements Beverage {
        Beverage bev;
        public Mocha(Beverage bev) {
    
        }
        
        public String getDescription() {
            return "Mocha" + bev.getDescription();
        }
        
        public float getCost() {
        return 0.90 + bev.getCost();
        }
    }

It might be a little difficult to see the impact of what we just did. So, let's look at some client code. In order to calculate the price of a Coffee, a beverage, with double mocha and whip, all we have to do is the following.

    public static void main() {
        System.out.println(new Whip(new Mocha(new Mocha(new Coffee()))).getCost());
    }
    
We can add as many mochas, whips, toppings as we want to the coffee. All we have to do is wrap it around the coffee. For any new condiments, we don't have to change any existing code in the beverage classes. This brings us to the design principle we mentioned at the beginning, "classes should be open for extension, but closed for modification."
