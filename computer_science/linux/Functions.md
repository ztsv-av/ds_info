# Linux Functions

## What is a function?

A function is a group of statements designed to perform a specific task. Functions provide a way to organize a program so it is manageable or easy to read and easy to maintain. A function can be used multiple times in a program. For example, if a function prints a value, that function can be used to print different values in different points across the program. Another important advantage of functions is reuse. For example, when a function is designed to sum two numbers, that function can be reused in different programs.

## Structure of a Function

Generally, a function has the following structure: The function header includes the function return type, function name, and parameters, which are optional. The function body includes the statements to be executed when the function is called.

## How to use a Function

Using a function in a program is referred to as calling the function. The function can be called by using its name. The required arguments need to be passed along with the function name. Functions can return a value to the caller. If the function is not returning a value, the function type will be void, which means the function does not return a value. If the function returns a value, the returned value can be stored. Functions can use parameters to allow the caller to pass information to a function.

It is important to understand the difference between a parameter and an argument. A function parameter is a variable declared in the declaration of a function, while an argument is the value that is passed to the function when it is called in the program.

There are two ways to pass parameters, as follows:

- Passing parameters by value: In this method, the actual value of the argument is copied into the parameter of the function. If the value of the parameter changes inside the function, this will not affect the value of the argument.
- Passing parameters by reference: In this method, the reference of an argument is copied into the parameter. The reference is used to access the actual argument, and thus any changes that are made on the parameter will affect the argument. 

Functions may be referred to as methods or procedures, as well, in other programming languages. They are basically subroutines that run their specific task when called upon.

## Initializing function

```
# create boo function
function boo {
    
    echo "Boo"

# boo
# output: boo

}

function welcome {
    echo $1
}    

# welcome Welcome!

function sum {

      return $1 + $2

}

# sum 10 20
# result = $? # $? is used to receive the value returned from the last command executed in the script, which in this case was the return command of the sum function.

If you save this function in a .sh file, you need to first call .sh file, then call function name.

```

## Functions and User Input

Data can be received from user input by using the internal shell’s “read” function. Now, that is not true for all of the shell types, but it is true for the BASH shell.

```

sum(){
    result = $1 + $2
    return $result
}

read -p "Enter a number: "  number1
read -p "Enter a number: "  number2

sum $number1 $number2

echo "The sum of your two numbers is: " $?

```
