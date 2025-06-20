//all divisors of a number

public class Main {
    public static void main(String[] args) {
        int a = 100;
//Logic is that to go to that number one by one and dive and print.
        for(int i = 1;i<=a;i++){
            if(a%i==0){
                System.out.print(i+" ");
            }
        }
    }
}
