
class ABC{
    int add(int a ,int b){
        return a+b;
    }

    void add(int a,int b,int c){
        System.out.println(a+b+c);
    }
}
public class polymorphismcompile {
    public static void main(String args[]){
        ABC obj=new ABC();
        System.out.println(obj.add(4,5));
        obj.add(4,5,6);

    }
    
}
