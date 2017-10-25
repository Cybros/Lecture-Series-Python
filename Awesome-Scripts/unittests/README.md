# Python Unit Tests 


Unit testing is part of a formal process of development with
 proper documentation and proper schedule/efforts allocated to it.
 
Unit testing is the prime candidate for automation. The xUnit style  is the collective 
 name for several unit testing frameworks for various languages. In our case Python has nose, pytest and Nose2 apart from
 unittest.
 
 ## Using unittest
 You can fin the script called [**test_my_code.py**](test_my_code.py) to execute the test, from console type:
 
```commandline
python3 -m unittest test_my_code -v
```

And you will see the test results, in this case we are testing fixtures. You can find the official documentation [here](https://docs.python.org/3/library/unittest.html).

## Using nose & nose2
If we compare with unittest this is not extending from a parent class and makes the test cleaner.
To run the example provided in **test_nose.py** from terminal run:

```commandline
nosetests test_nose.py -vs
``` 
Nose and Nose2 are pretty much the same framework, but nose has been deprecated so its recommended to install nose2.