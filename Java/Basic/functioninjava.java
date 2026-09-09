public class functioninjava {

    // static void thisisfunction(){
    void thisisfunction(){
        System.out.println("This is a function");
    }

    void add(int a,int b){
        System.out.println(a+b);
    }
    int add1(int a,int b,int c){
        return a+b+c;
    }
    public static void main(String [] args){
        functioninjava obj=new functioninjava();
        obj.thisisfunction();
        obj.add(5,3);
        int abc=obj.add1(5,3,4);
        System.out.println(abc);


    }


    
    
    
}
