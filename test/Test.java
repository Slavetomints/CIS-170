import java.util.Scanner;
// Author: Daisy Hardwick

public class Test 
{
  public static void main(String[] args)
  {
    // Declare variables
    Integer atBats;
    Integer numberOfHits;
    float battingAverage;
    Scanner keyboard = new Scanner(System.in);

    // Prompt user for number of at bats
    System.out.println("How many at bats have you had?");
    atBats = keyboard.nextInt();

    // Prompt user for number of hits
    System.out.println("How many hits have you had?");
    numberOfHits = keyboard.nextInt();

    // Calculate batting average
    battingAverage = (float)numberOfHits / (float)atBats;

    // Display results
    System.out.println("With " + numberOfHits + " hits at " + atBats + " at bats, your batting average is " + battingAverage + ".");
  }
}