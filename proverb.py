"""

Instructions
For want of a horseshoe nail, a kingdom was lost, or so the saying goes.

Given a list of inputs, generate the relevant proverb. For example, given the list ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"], you will output the full text of this proverbial rhyme:

For want of a nail the shoe was lost.
For want of a shoe the horse was lost.
For want of a horse the rider was lost.
For want of a rider the message was lost.
For want of a message the battle was lost.
For want of a battle the kingdom was lost.
And all for the want of a nail.
Note that the list of inputs may vary; your solution should be able to handle lists of arbitrary length and content. No line of the output text should be a static, unchanging string; all should vary according to the input given.

In unpacking-and-multiple-assignment, you learned multiple techniques for working with lists/tuples of arbitrary length as well as function arguments of arbitrary length. This exercise would be a great place to practice those techniques.

How this exercise is implemented for Python
The test cases for this track add an additional keyword argument called qualifier. You should use this keyword arguments value to modify the final verse of your Proverb.
"""

def proverb(*verb, qualifier=None):
    if len(verb) == 0:
        return []
    
    [elements] = verb
    output = []

    if len(elements) == 1 and qualifier:
        return ["And all for the want of a " + qualifier + " " + elements[0] + "."]
    
    if len(elements) == 1:
        return ["And all for the want of a " + elements[0] + "."]
    
    for index, element in enumerate(elements):
        output.append("For want of a " + element + " the " + elements[index + 1] + " was lost.")
        if len(elements) - 2 == index:
            break
    
    if qualifier:
        output.append("And all for the want of a " + qualifier + " " + elements[0] + ".")
    else:
        output.append("And all for the want of a " + elements[0] + ".")

    return output


if __name__ == "__main__":
    #print(proverb(["nail", "shoe", "horse"]))
    print(proverb(["nail"]))