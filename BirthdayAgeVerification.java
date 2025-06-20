// party entry program ( Birthday Bash )
// user will enter his name.
// our program will greet the user first and then ask for age
// if age is 18+ then he will be allowed otherwise not allowed.
// if age is above 80 not allowed, and negative age is also not allowed.


//--------------Issue to fix-----------------
// 1. We need to restrict name to String and Age to number.
// 2. We need to handle wrong inputs
// 3. Program is crashing when unexpeced input is given.

import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("---------Birthday Bash--------");
        System.out.println("Please enter your name");
        String name = sc.nextLine();

        if(name==""){
            System.out.println("You cannot proceed without name");
            return;
        }
        else{
        System.out.println("Welcome " + name);

        }
        System.out.println("Please enter your age");
        int age = sc.nextInt();
        boolean entry = isValidAge(age);
        if(entry){
            System.out.println("Welcome to the party, You are allowed " + name);
        }
        else{
            System.out.println("Sorry, you age critera does not meet the requirement");
        }
    }
    public static boolean isValidAge(int age){

        if(age>=18 && age<=80){
            return true;
        } else if (age<18) {
            return false;
        }
        else if(age<0){
            return false;
        }
        return false;
    }
}
