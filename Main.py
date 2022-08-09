class Evaluate:
  
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    # Write your code here
    if self.top == -1:
      return 1
    else:
      return 0
      
      


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if  not self.isEmpty():
      
      
      self.stack.pop()
      self.top-=1
      
    # Write your code here


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    if not self.top == (size -1):
      self.stack.append(operand)
      
      self.top+=1
    # Write your code here


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    for i in expression:
      if i.isnumeric() or i in "+-*/^":
        return True
      else:
        return False
        
    
    
    # Write your code here


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    for i in expression:
      
      if i == '+':
        op2 = self.stack.pop()
        op1 = self.stack.pop()
        result = op1+op2
        self.push(result)
      elif i == '*':
        op2 = self.pop()
        op1 = self.pop()
        result = op1*op2
        self.push(result)
      elif i  == '-':
        op2 = self.pop()
        op1 = self.pop()
        result = op1-op2
        self.push(result)
      elif i == '/':
        op2 = self.pop()
        op1 = self.pop()
        result = op1/op2
        self.push(result)
      else:
        self.push(int(v))
if len(self.stack) >1:
  return False
else:
  return self.stack[0]
      
    
      
     
    # Write your code here


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
