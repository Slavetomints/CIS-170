import java.util.Scanner;
// Author: Daisy Hardwick
// Class: CIS-170
// Program: Miles-Per-Gallon Java Program

public class MilesPerGallon
{
  public static void main(String[] args)
  {
    // Declare variables
    Integer milesDriven;
    Integer gasUsed;
    float gasMileage;
    Scanner keyboard = new Scanner(System.in);

    // Prompt user for miles driven
    System.out.println("How many miles have you driven?");
    milesDriven = keyboard.nextInt();

    // Prompt user for gallons of gas used
    System.out.println("How many gallons of gas did you use?");
    gasUsed = keyboard.nextInt();

    // Calculate miles-per-gallon
    gasMileage = (float)milesDriven / (float)gasUsed;

    // Display results
    System.out.println("You drove " + gasMileage + " miles per gallon of gas");
  }
}