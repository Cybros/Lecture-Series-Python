Java
statically typed
In Java, all variable names (along with their types) must be explicitly declared. Attempting to assign an object of the wrong type to a variable name triggers a type exception.That’s what it means to say that Java is a statically typed language.

Java container objects (e.g. Vector and ArrayList) hold objects of the generic type Object, but cannot hold primitives such as int. To store an int in a Vector, you must first convert the int to an Integer. When you retrieve an object from a container, it doesn’t remember its type, and must be explicitly cast to the desired type.

Python
dynamically typed
In Python, you never declare anything. An assignment statement binds a name to an object, and the object can be of any type. If a name is assigned to an object of one type, it may later be assigned to an object of a different type. That’s what it means to say that Python is a dynamically typed language.

Python container objects (e.g. lists and dictionaries) can hold objects of any type, including numbers and lists. When you retrieve an object from a container, it remembers its type, so no casting is required.

Java
not compact

Python
compact
In The New Hacker’s Dictionary, Eric S. Raymond gives the following definition for “compact”:

Compact adj. Of a design, describes the valuable property that it can all be apprehended at once in one’s head. This generally means the thing created from the design can be used with greater facility and fewer errors than an equivalent tool that is not compact.

Java Example
*public class HelloWorld
{
    public static void main (String[] args)
    {
        System.out.println("Hellold!");
    }
}

*int    myCounter = 0;
String myString = String.valueOf(myCounter);
if (myString.equals("0")) ...

*// print the integers from 1 to 9
for (int i = 1; i < 10; i++)
{
   System.out.println(i);
}

Python Example
*print "Hello, world!"

*print("Hello, world!") # Python version 3

*myCounter = 0
myString = str(myCounter)
if myString == "0": ...

*print the integers from 1 to 9
for i in range(1,10):
    print i

Example:
Your application has 15 classes. (More precisely, it has 15 top-level public classes.)
 Java
 Each top-level public class must be defined in its own file. If your application has 15 such classes, it has 15 files.

 Python
 Multiple classes can be defined in a single file. If your application has 15 classes, the entire application could be stored in a single file, although you would probably want to partition it sensibly into perhaps 4, 5, or 6 files.