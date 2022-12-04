# Introduction

GPTLang is a general-purpose, high-level programming language designed for ease of use and readability. It is an interpreted language, meaning that the code is executed directly by the interpreter, without the need for a separate compilation step.

GPTLang has a simple and intuitive syntax that is easy to learn and understand, making it a great language for beginners and experienced programmers alike. It supports a wide range of data types, including numbers, strings, arrays, and user-defined data types.

GPTLang has a rich set of built-in functions and features that make it easy to write powerful and efficient programs. It also has a flexible and extensible architecture that allows users to create their own functions and data types.

# Basic Syntax

## Comments

A comment in GPTLang starts with a hash character (#) and extends to the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax and are used to provide explanatory notes and documentation for the code.

Here is an example of a comment in GPTLang:

```gptlang
# This is a comment
```

## Variables

A variable in GPTLang is a named storage location that holds a value. A variable must be declared with a VAR keyword before it can be used in the code. The syntax for declaring a variable is:

```gptlang
VAR <variable_name>:<data_type> <value>
```

The <variable_name> field specifies the name of the variable. The <data_type> field specifies the data type of the variable. The <value> field specifies the initial value of the variable.

Here are some examples of variable declarations in GPTLang:

```gptlang
# Declare a string variable named "message" with the initial value "Hello, world!"
VAR message:str "Hello, world!"

# Declare an integer variable named "count" with the initial value 0
VAR count:int 0

# Declare a float variable named "pi" with the initial value 3.14
VAR pi:float 3.14
```

## Functions

A function in GPTLang is a self-contained block of code that performs a specific task and optionally returns a value. A function must be defined with a FUNC keyword before it can be called in the code. The syntax for defining a function is:

```gptlang
FUNC <function_name>(<arguments>) -> <return_values>:
    <function_body>
```

The <function_name> field specifies the name of the function. The <arguments> field specifies the input parameters of the function. The <return_values> field specifies the data type of the value returned by the function. The <function_body> field contains the code that makes up the body of the function.

Here is an example of a function definition in GPTLang:

```gptlang
# Define a function named "add" that takes two integer arguments and returns an integer value
FUNC add(a:int, b:int) -> int:
    # Calculate the sum of the two arguments
    VAR result:int = a + b

    # Return the result
    return result
```

## Conditional Execution

GPTLang supports conditional execution using the IF and ELSE keywords. The syntax for conditional execution is:

```gptlang
IF <condition>:
    <statements>
ELSE:
    <statements>
```

The <condition> field specifies a Boolean expression that determines whether the <statements> in the IF clause or the ELSE clause are executed. If the <condition> is true, the <statements> in the IF clause are executed. If the <condition> is false and an ELSE clause is present, the <statements> in the ELSE clause are executed.

Here is an example of conditional execution in GPTLang:

```gptlang
# Define a variable named "num" with the initial value 10
VAR num:int 10

# Check if the value of "num" is less than 8
IF num < 8:
    # If the value of "num" is less than 8, print "Ping"
    PT("Ping")
ELSE:
    # If the value of "num" is greater than or equal to 8, print "Pong"
    PT("Pong")
```

In this example, the IF clause will be executed and the string "Ping" will be printed to the screen, because the value of the num variable is 10, which is greater than 8.

## Loops

GPTLang supports looping using the LOOP keyword. The syntax for looping is:

```gptlang
LOOP <iterable_object> -> <element>:
    <statements>
```

The <iterable_object> field specifies an object that can be iterated over, such as a string, tuple, or list. The <element> field specifies a variable that will be assigned the value of each element in the <iterable_object> as the loop progresses. The <statements> field contains the code that is executed for each iteration of the loop.

Here is an example of looping in GPTLang:

```gptlang
# Define an array named "numbers" with the initial values [5, 8, 6, 3, 9, 1]
VAR numbers:arr [5, 8, 6, 3, 9, 1]

# Loop over the elements in the "numbers" array
LOOP numbers -> num:
    # Print the value of each element in the "numbers" array
    PT(num)
```

In this example, the LOOP statement will iterate over the elements in the numbers array, and the value of each element will be assigned to the num variable in turn. For each iteration, the PT(num) statement will be executed, which will print the value of the num variable to the screen.

## Arrays

GPTLang supports arrays, which are ordered collections of elements of the same data type. An array can be declared with the VAR keyword and the arr data type. The syntax for declaring an array is:

```gptlang
VAR <array_name>:arr [<element1>, <element2>, ...]
```

The <array_name> field specifies the name of the array. The <element1>, <element2>, ... fields specify the initial values of the array elements.

Here is an example of declaring an array in GPTLang:

```gptlang
# Declare an array named "numbers" with the initial values [5, 8, 6, 3, 9, 1]
VAR numbers:arr [5, 8, 6, 3, 9, 1]
```

An array can be iterated over using the LOOP statement, as shown in the previous section. The length of an array can be obtained using the LEN() function. Elements of an array can be accessed using their index, which is the position of the element in the array, starting at 0. The syntax for accessing an array element is:

```gptlang
<array_name>[<index>]
```
