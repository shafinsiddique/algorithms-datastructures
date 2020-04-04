# The Observer Design Pattern
The observer pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

There's two types of entities involved in the observer design pattern: 'Subject' and 'Observers.' The 'subject' maintains some collection of 'observers.' When a change happens in the subject, the subject notifies all of its observers.

The benefit of this design pattern is that it allows objects to have a relationship while being loosely coupled. How?
Through the use of the observer and subject interfaces.

Each observer implements the observer interface and each subject implements the subject interface. What this results in is that even though the observers are an attribute of the subject, the subject does not need to anything more than the fact that the observer implements a certain interface.

We can add new observers at any time. Because the only thing the subject depends on is a list of objects that implements the Observer interface, we can add new observers whenever we want.

We also never need to modify the subject in order to add new observers.

This is why the observer design pattern is so powerful. 

"Loosely coupled designs allow us to build flexible OO systems that can handle change because they minimize the interdependency between objects." - Head First Design Patterns, O'Reily

# Interfaces 

    interface Observer {
        public void update();
    }
    
    interface Subject {
        public void registerObserver();
        public void removeObserver();
        public void notifyObserver();
        
    }



# An example

This example is taken from Head First Design Patterns by O'Reily.

Imagine this: You are responsible for building the backend of a weather application. You have a class 'WeatherData' that communicates with a physical device that can get the weather data (humidity, temperature) for you. However, your backend code will be used by multiple front-end sources to display the data. Basically, there's multiple display devices.

When the temperature changes and the weatherData class receives that data, it must ensure that all the sources that are relying on this class are notified of this changed. We don't want a display where the temperature is not updated.

An intuitive approach would simply be to have an attribute for each source that has to display the data and then update each accordingly.

    public class WeatherData {
        ForecastDisplay fd = new ForecastDisplay();
        StatisticsDisplay sd = new StatisticsDisplay();
        RegularDisplay rd = new RegularDisplay();
        PhysicalDevice temperatureRecorder;
    
    public float getTemperature(){ 
        // get it from physical device.
    }
    
    public float getHumidity() {
        // get it from physical device
    }
    public float getPressure() {
        // get it from physical device.
    }
    
    /*
    Let's just assume that this method will be called whenever the physical device that records the temperature notices a change in temperature.
    */
    
    public void measurementsChanged() {
        float temp = getTemperature(); 
        float humidity = getHumidity();
        float pressure = getPressure();
        fd.update(getTemperature(), getHumidity(), getPressure())
        
    }


    }
    
This approach would work but there's huge flaws in it. Anytime we add a new front-end source, we have to go back into the WeatherData class, add an attribute and then update the measurementsChanged method to handle that new device. This can get tedious quite fast and makes our code extremely coupled and unextendable.

With the Observer Design Pattern, we could solve this problem in no time.

    
    interface WeatherDisplay {
        // this is the observer interface.
        public void update(float temperature, float humidity, float pressure);
    }
    
    interface Subject {
        public void addObserver(WeatherDisplay o);
        public void removeObserver(WeatherDisplay o);
        public void notifyObservers();


        
    
    }
    public class ForecastDisplay implements WeatherDisplay {
    
    }
    
    public class StatisticalDipslay implements WeatherDisplay {
    
    }
    
    public class RegularDisplay implements WeatherDisplay {
    
    }
    public class WeatherData implements Subject {
        PhysicalDevice temperatureRecorder;
        ArrayList<WeatherDisplay> observers;

        public float getTemperature(){ 
            // get it from physical device.
        }

        public float getHumidity() {
            // get it from physical device
                }
        public float getPressure() {
            // get it from physical device.
                }

        /*
        Let's just assume that this method will be called whenever the physical device that records the temperature notices a change in temperature.
        */

        public void notifyObservers() {
            float temp = getTemperature(); 
            float humidity = getHumidity();
            float pressure = getPressure();
            
            for (WeatherDisplay observer: observers) {
                observer.update(temp, humidity, pressure);
            }

        }

    }






