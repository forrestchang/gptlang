# Introduction

GPTLang is a general-purpose, high-level programming language designed for ease of use and readability. It is an interpreted language, meaning that the code is executed directly by the interpreter, without the need for a separate compilation step.

GPTLang has a simple and intuitive syntax that is easy to learn and understand, making it a great language for beginners and experienced programmers alike. It supports a wide range of data types, including numbers, strings, arrays, and user-defined data types.

GPTLang has a rich set of built-in functions and features that make it easy to write powerful and efficient programs. It also has a flexible and extensible architecture that allows users to create their own functions and data types.

# How to use

Copy the raw content of [README.md](https://raw.githubusercontent.com/forrestchang/gptlang/main/README.md) and paste it to ChatGPT. Now you can write GPTLang in ChatGPT.

# Example: Selection Sort

```gptlang
FUNC selection_sort(array:arr) -> arr:
    # Iterate over the elements of the array
    LOOP array -> elem:
        # Find the minimum value in the remaining unsorted portion of the array
        VAR min_index:int = array.index(elem)
        LOOP array[min_index+1:] -> other_elem:
            IF other_elem < array[min_index]:
                min_index = array.index(other_elem)

        # Swap the minimum value with the current element
        array[array.index(elem)] = array[min_index]
        array[min_index] = elem

    # Return the sorted array
    return array
```

# Basic Syntax

##  1. <a name='Comments'></a>Comments

A comment in GPTLang starts with a hash character (#) and extends to the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax and are used to provide explanatory notes and documentation for the code.

Here is an example of a comment in GPTLang:

```gptlang
# This is a comment
```

##  2. <a name='Variables'></a>Variables

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

##  3. <a name='Functions'></a>Functions

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

##  4. <a name='ConditionalExecution'></a>Conditional Execution

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

##  5. <a name='Loops'></a>Loops

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

##  6. <a name='Arrays'></a>Arrays

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

Here is an example of accessing an array element in GPTLang:

```
# Define an array named "numbers" with the initial values [5, 8, 6, 3, 9, 1]
VAR numbers:arr [5, 8, 6, 3, 9, 1]

# Print the second element of the "numbers" array
PT(numbers[1])
```

In this example, the PT(numbers[1]) statement will print the value of the second element in the numbers array, which is 8, to the screen.

##  7. <a name='User-DefinedDataTypes'></a>User-Defined Data Types

GPTLang supports user-defined data types, which allow users to create their own custom data structures. A user-defined data type can be declared with the TYPE keyword. The syntax for declaring a user-defined data type is:

```gptlang
TYPE <type_name>(<field1>:<data_type1>, <field2>:<data_type2>, ...):
    <field_initialization>
```

The <type_name> field specifies the name of the user-defined data type. The <field1>, <field2>, ... fields specify the fields of the data type, and the <data_type1>, <data_type2>, ... fields specify the data type of each field. The <field_initialization> field specifies the initial values of the fields of the data type.

Here is an example of declaring a user-defined data type in GPTLang:

```
# Define a user-defined data type named "point" with fields "x" and "y" of type int
TYPE point(x:int, y:int):
    # Initialize the fields of the "point" data type
    x = 0
    y = 0
```

Once a user-defined data type has been declared, it can be used to create variables of that data type. The syntax for declaring a variable of a user-defined data type is:

```
VAR <variable_name>:<type_name>
```

The <variable_name> field specifies the name of the variable, and the <type_name> field specifies the name of the user-defined data type.

Here is an example of declaring a variable of a user-defined data type in GPTLang:

```
# Define a user-defined data type named "point" with fields "x" and "y" of type int
TYPE point(x:int, y:int):
    # Initialize the fields of the "point" data type
    x = 0
    y = 0

# Declare a variable named "origin" of type "point"
VAR origin:point
```

In this example, the origin variable will be of type point, and it will have the fields x and y with initial values of 0.

# Built-in Functions and Features

GPTLang has a rich set of built-in functions and features that make it easy to write powerful and efficient programs. Some of the notable built-in functions and features of GPTLang are described below.

##  8. <a name='PTFunction'></a>PT() Function

The PT() function is a built-in function that prints the specified value to the screen. The syntax for the PT() function is:

```
PT(<value>) -> None
```

The <value> field specifies the value to be printed. The PT() function does not return any value.

Here is an example of using the PT() function in GPTLang:

```
# Define a variable named "message" with the initial value "Hello, world!"
VAR message:str "Hello, world!"

# Print the value of the "message" variable to the screen
PT(message)
```

In this example, the PT(message) statement will print the value of the message variable, which is "Hello, world!", to the screen.

##  9. <a name='LENFunction'></a>LEN() Function

The LEN() function is a built-in function that returns the length of a specified value. The syntax for the LEN() function is:

```
LEN(<value>) -> int
```

The <value> field specifies the value for which the length is to be calculated. The LEN() function returns an integer value representing the length of the specified value.

Here is an example of using the LEN() function in GPTLang:

```
# Define an array named "numbers" with the initial values [5, 8, 6, 3, 9, 1]
VAR numbers:arr [5, 8, 6, 3, 9, 1]

# Print the length of the "numbers" array to the screen
PT(LEN(numbers))
```

In this example, the PT(LEN(numbers)) statement will print the length of the numbers array, which is 6, to the screen.

## Implicit Line Joining

GPTLang supports implicit line joining, which allows multiple physical lines of code to be treated as a single logical line. This can be useful for making long lines of code more readable by breaking them up into multiple physical lines.

Implicit line joining is performed by ending a physical line with a backslash (\) character. The next physical line will be treated as part of the same logical line. This continues until a physical line is encountered that does not end with a backslash character.

Here is an example of implicit line joining in GPTLang:

```
# Define a variable named "message" with the initial value "Hello, world!\
# This is a long message that spans multiple physical lines."
VAR message:str "Hello, world!\
This is a long message that spans multiple physical lines."

# Print the value of the "message" variable to the screen
PT(message)
```

In this example, the VAR statement defining the message variable uses implicit line joining. The message variable will have the initial value "Hello, world! This is a long message that spans multiple physical lines.", which is the concatenation of the two physical lines on which the VAR statement is written.

The PT(message) statement will print the value of the message variable to the screen, which is "Hello, world! This is a long message that spans multiple physical lines."
