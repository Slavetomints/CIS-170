// Author: Daisy Hardwick
// Class: CIS-170
// Program: Leap Year Detector Java Program

import java.util.Scanner;

public class LeapYearDetector
{
  public static void main (String[] args)
  {
    // Declare variable
    Integer year;
    Scanner keyboard = new Scanner(System.in);

    // Prompt user for year
    System.out.println("Please select a year.");
    year = keyboard.nextInt();

    // Test to see if year is a leap year and display results
    if (((year % 100 == 0) && (year % 400 == 0)) || ((year % 4 ==0) && (year % 100 != 0)))
    {
      System.out.println(year + " is a leap year.");
    }
    else
    {
      System.out.println(year + " is not a leap year.");
    }

    keyboard.close();
  }
}