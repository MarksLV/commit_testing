import java.util.Scanner;

public class SimpleAdditionCalculator {
    public static void main(String[] args) {
        // Create a scanner object to take input from the user
        Scanner scanner = new Scanner(System.in);

        // Take the first number as input
        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();

        // Take the second number as input
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();

        // Perform addition
        double result = num1 + num2;

        // Display the result
        System.out.println("The result of addition is: " + result);
        
        // Close the scanner
        scanner.close();
    }
}
