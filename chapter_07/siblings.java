// Author: Daisy Hardwick
// Class: CIS-170
// Program: Kilometer Converter Java Program

import java.util.Scanner;

public class siblings {
  public static void main(String[] args)
  {
    try {
      System.out.println("Enter number of siblings:");
      Integer size;
      Scanner keyboard = new Scanner(System.in);

      size = keyboard.nextInt();
      keyboard.nextLine(); 
      if (size == 0)
      {
        System.out.println("Ah, you are an only child");
      } else
      {
        String[] siblingsArray = new String[size];
        for (int i = 0; i < siblingsArray.length; i++ )
        {
          System.out.println("\nEnter sibling " + (i + 1));
          siblingsArray[i] = keyboard.nextLine();
        }

        System.out.println("\nYour siblings are:");
        for (int i = 0; i < siblingsArray.length; i++ )
        {
          System.out.println(siblingsArray[i]);
        }

      }
      keyboard.close();      
    }
    catch(Exception e) {
      System.out.println("Invalid type detected, exiting now!");
    }


  }
}
