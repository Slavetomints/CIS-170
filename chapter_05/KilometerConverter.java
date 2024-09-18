// Author: Daisy Hardwick
// Class: CIS-170
// Program: Kilometer Converter Java Program

import java.util.Scanner;

public class KilometerConverter
{
  public static void main(String[] args) 
  {
    displayIntro();
    kilometerToMileConverter();
  }

  public static void displayIntro() 
  {
    System.out.println("Welcome to the Kilometer to Miles Converter!");
  }

  public static void kilometerToMileConverter() 
  {
    // Declare variables
    float kilometers;
    double miles;
    final double KILOMETER_TO_MILE_CONVERSION_RATE = 0.6214;
    Scanner keyboard = new Scanner(System.in);

    // Gathering input from user
    System.out.println("Please enter the amount in kilometer(s)"); 
    kilometers = keyboard.nextInt();

    // Calculating miles
    miles = kilometers * KILOMETER_TO_MILE_CONVERSION_RATE;

    // Displaying output
    System.out.println( kilometers + " kilometer(s) is equal to " + miles + " mile(s)."); 

    // Close keyboard
    keyboard.close();
  }
}