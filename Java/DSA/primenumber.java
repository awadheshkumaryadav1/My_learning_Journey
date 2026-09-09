public class primenumber {
    public static void main(String[] args) {
        int count2=0;
        for(int n=2; n<=100;n++){
            int count=0;
            for (int i = 1; i <= n; i++) {
                if(n%i==0){
                    count++;
                }
                
            }
            if(count==2){
                System.out.println(n+"");
                count2++;
                
            }
            

        }
        System.out.println();
            System.out.print(count2);
    }
    
}
