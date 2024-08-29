import java.util.Scanner;
  
public class MilesPerGallon
{
  public static void main(String[] args)
  {
    Integer milesDriven;
    Integer gasUsed;
    float gasMileage;
    Scanner keyboard = new Scanner(System.in);

    System.out.println("How many miles have you driven?");
    milesDriven = keyboard.nextInt();

    System.out.println("How many gallons of gas did you use?");
    gasUsed = keyboard.nextInt();

    gasMileage = (float)milesDriven / (float)gasUsed;

    System.out.println("You drove " + gasMileage + " miles per gallon of gas");
  }
}