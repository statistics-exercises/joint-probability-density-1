# Manipulating joint probability densities in python

Consider the following problem that you have just solved:

The joint probability density function for the pair of continuous random variables (X,Y) is:

![](https://render.githubusercontent.com/render/math?math=f(x,y)=k(x^2y^2%2Bxy^3)\quad\textrm{if}\quad\1<x<2\quad\textrm{and}\quad\0<y<3)

(1) Show that this is a valid probability density function by taking suitable partial derivatives of ![](https://render.githubusercontent.com/render/math?math=f(x,y))
etc.

Now if you are anything like me you probable found doing the integration and differentiation involved in this problem rather tedious.  When I go through mathematical deviations like these I am also quite error-prone.  I often find that I have got a wrong answer when I get to the end of the derivation because of a careless mistake. 

We can use Python to avoid these types of mundane exercises.  In one of the first sets of exercises, I gave you to complete I showed you how we can use SymPy to do both integration and differentiation of functions for you.  In this series of exercises, you are thus going to use this tool to solve all the parts of the problem above.

Let's start with the first part of the question, which is written above.  Look at the Functions exercise that you completed in week 0 and use SymPy to calculate the partial derivates of the probability density function with respect to x and y and the two cross (second) derivatives.  You need to set the variables as follows:

1. `dfdx` = first partial derivative of ![](https://render.githubusercontent.com/render/math?math=f(x,y)) with respect to x
2. `dfdy` = first partial derivative of ![](https://render.githubusercontent.com/render/math?math=f(x,y)) with respect to y
3. `d2fdxdy` = ![](https://render.githubusercontent.com/render/math?math=\frac{\partial^2f}{\partial\x\partial\y}) 
4. `d2fdydx` = ![](https://render.githubusercontent.com/render/math?math=\frac{\partial^2f}{\partial\y\partial\x}) 
