# Linux (bash) Arrays

## Array declaration

```

my_array=(1 2 3 4 5 100)

declare -A AssociativeArray # array index is in named form
declare -a NumbericArray # array index is in numeric form

# local array
function foo() {

    local -a LocalArray # numeric array which only exists in this function

}

```

## Access and Read Arrays

```

echo "First element of my array is: ${my_array[0]}"
echo ${my_array[@]:1:3} # outputs: 2 3 4

# local array
function foo() {

    local -a LocalArray # numeric array which only exists in this function

    LocalArray[0]="Hi"
    LocalArray[1]="There"
    LocalArray[9]=15 # no need to be consecutive or string

    # read specific items in array
    echo "${LocalArray[0]} ${LocalArray[1]}" # output: Hi There

    # read whole array
    echo "${LocalArray[@]}" # output: Hi There 15
    
}

# set values in associative array
AssociativeArray[Var1]="Var1"
AssociativeArray[Variable2]="Variable2"
AssociativeArray[Linux]="LinuxIsTheBest"

# check if values exist in associative array
if [ "${AssociativeArray[Var1]}" ]; then
    echo "Var1 exists"
else
    echo "No"
fi
# output: Var1 exists

# check if values exist in associative array
Test="Var1"
if [ "${AssociativeArray[$Test]}" ]; then
    echo "Var1 exists"
else
    echo "No"
fi
# output: Var1 exists

```

## Add Values to Arrays

```

my_array+=(1 7)

for i in ${my_array[*]}; do
    echo $i
done

# add string into numeric array
NumericArray+=("All work")
NumericArray+=("and no play")

echo "Writing NumericArray to File /tmp/test.txt"
printf "%s\n "${NumericArray[@]}" > /tmp/test.txt

echo
echo "Reading File /tmp/test.txt"
cat /tmp/test.txt

```

## Length of Array
```

# length of array
echo "Array Length: ${#my_array[@]}" # output: 8

# length of an element
echo "Index 3 Length: ${#my_array[3]}" # output: 1

```

## Sort Array

```

# sort array
sorted_array=($(for i in "${my_array[@]}"; do

    echo $i;

done | sort))

```

## Delete Array / Element

```

# delete an element from an array
unset 'my_array[1]'

# delete whole array
unset my_array
```
