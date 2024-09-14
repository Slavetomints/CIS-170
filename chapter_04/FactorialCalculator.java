// Author: Daisy Hardwick
// Class: CIS-170
// Program: Factorial Calculator Java Program

import java.util.Scanner;

public class FactorialCalculator 
{
  public static void main(String[] args) 
  {
    // Declare variables  
    Integer total = 1;
    Integer currentValue = 1;
    Integer maxValue;
    Scanner keyboard = new Scanner(System.in);

    // Collect value
    System.out.println("Please select a number to get the factorial of");
    maxValue = keyboard.nextInt();

    // Calculate factorial
    while (currentValue <= maxValue)
    {
      total *= currentValue;
      currentValue += 1;
    }

    // Display results
    System.out.println(maxValue + "! is equal to " + total);

    keyboard.close();
  }
  
}