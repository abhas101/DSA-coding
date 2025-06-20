public class Main {
    public static void main(String[] args) {
        int a = 4, b = 8;
        System.out.println(gcd(a,b));
    }

  // function to find GCD
    public static int gcd(int a, int b){
        int max = Math.max(a, b);
        int res = 1;
        for(int i = 1;i<=max;i++){
            if(a%i==0  && b%i==0){
                if(res<i){
                    res = i;
                }
            }
        }
        return res;
    }
}
