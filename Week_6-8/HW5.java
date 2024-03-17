import java.util.Scanner;

public class Homework5 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // Task 1: Rectangle Area
        double length = getInput("Enter rectangle length: ");
        double width = getInput("Enter rectangle width: ");
        double area = calculateArea(length, width);
        displayRectangleData(length, width, area);

        // Task 2: Conversion Program
        double distance;
        do {
            distance = getInput("Enter distance in meters: ");
            if (distance < 0) {
                System.out.println("Distance cannot be negative. Please enter a valid distance.");
            } else {
                showConversionMenu(distance);
            }
        } while (distance >= 0);

        // Task 3: isPrime Method
        int number = getInput("Enter a number (1-100) to check for primality: ");
        if (isPrime(number)) {
            System.out.println(number + " is a prime number");
        } else {
            System.out.println(number + " is not a prime number");
        }

        scan.close();
    }

    private static double getInput(String prompt) {
        System.out.print(prompt);
        return new Scanner(System.in).nextDouble();
    }

    // Task 2: Conversion Program
    private static void showConversionMenu(double meters) {
        int choice;
        do {
            System.out.println("1. Convert to kilometers\n2. Convert to inches\n3. Convert to feet\n4. Quit the program");
            System.out.print("Enter your choice: ");
            choice = new Scanner(System.in).nextInt();

            switch (choice) {
                case 1:
                    showConvertedValue(meters * 0.001, "kilometers", meters);
                    break;
                case 2:
                    showConvertedValue(meters * 39.37, "inches", meters);
                    break;
                case 3:
                    showConvertedValue(meters * 3.281, "feet", meters);
                    break;
                case 4:
                    System.out.println("Bye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        } while (choice != 4);
    }

    private static void showConvertedValue(double value, String unit, double meters) {
        System.out.println(meters + " meters is " + value + " " + unit + ".");
    }

    // Task 3: isPrime Method
    private static int getInput(String prompt) {
        System.out.print(prompt);
        return new Scanner(System.in).nextInt();
    }

    private static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
