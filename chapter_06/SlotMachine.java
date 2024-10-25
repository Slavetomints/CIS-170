// Author: Daisy Hardwick
// Class: CIS-170
// Program: Slot Machine Java Program

import java.util.*;

public class SlotMachine
{
  public static void main(String[] args)
  {
    Scanner keyboard = new Scanner(System.in);
    int money = enterAmountOfMoney(keyboard);
    String firstWord = getChoice();
    String secondWord = getChoice();
    String thirdWord = getChoice();
    checkWinnings(money, firstWord, secondWord, thirdWord);
    playAgain(keyboard);
    keyboard.close();
  }

  public static int enterAmountOfMoney(Scanner keyboard)
  {
    int money;
    System.out.println("\n\nPlease enter the amount of money you wish to bet");
    money = keyboard.nextInt();
    if (money < 0) {
      System.out.println("Please enter a while number greater than zero");
      money = enterAmountOfMoney(keyboard);
    }
    return money;
  }

  public static String getChoice()
  {
  int number = (int) (Math.random()*6);
  String choice = new String [] {"Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"}[number];
  System.out.println(choice);
  return choice;
  }

  public static void checkWinnings(int money, String firstWord, String secondWord, String thirdWord)
  {
    if (firstWord == secondWord && firstWord == thirdWord)
    {
      money *= 3;
      System.out.println("You won $" + money + "!");
    } else if (firstWord == secondWord || firstWord == thirdWord || secondWord == thirdWord)
    {
      money *= 2;
      System.out.println("You won $" + money + "!");
    } else
    {
      System.out.println("You loose!");
    }
  }

  public static void playAgain(Scanner keyboard)
  {
    System.out.println("Do you want to play again? Please enter 'Y' or 'y' to do so.");
    String answer;
    answer = keyboard.next();

    if (answer.charAt(0) == 'Y' || answer.charAt(0) == 'y')
    {
      System.out.println("Have fun!\n\n");
      main(new String[0]);
    } else
    {
      System.out.println("Bye Bye!");
    }
  }
}