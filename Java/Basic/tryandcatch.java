public class tryandcatch{
    public static void main(String[] args) {
        try{
            int a=10;
            int b=5;
            System.out.println(a/b);
        }catch(ArithmeticException e){
            System.out.println("cannot divide by zero");

        }
        finally{
            System.out.println("always execute");
        }
        
    }
}