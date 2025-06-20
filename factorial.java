public class Main{
    public static void main(String[] args) {
        int n = 5;

        System.out.println(factorial(n));
    }

//    function
    public static int factorial(int n){
        int res = 1;
      // mulitplying all the number with res.
      // we are taking i =1 as any number mulitplited by 0 will be 0.
        for(int i = 1;i<=n;i++){
            res *=i;
        }

        return res;
    }
}
